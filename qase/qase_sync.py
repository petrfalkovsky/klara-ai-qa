# -*- coding: utf-8 -*-
"""Заливает qase_data.py в Qase через REST API и пересобирает test-cases.md / defects.md.
Запуск из корня: python3 qase/qase_sync.py [--dry] [--update]
Код проекта: переменная QASE_PROJECT_CODE (по умолчанию KLARA)   (токен в .env: QASE_TOKEN=...)
Идемпотентен: созданные сущности запоминаются в qase_state.json."""
import json, os, subprocess, sys
from qase_data import PROJECT, ENV, SUITES, C, D

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # корень репозитория
STATE_F = os.path.join(ROOT, "qase_state.json")
API = "https://api.qase.io/v1"
SEV = {"blocker": 1, "critical": 2, "major": 3, "normal": 4, "minor": 5, "trivial": 6}
PRI = {"high": 1, "medium": 2, "low": 3}
TYPE = {"other": 1, "smoke": 2, "regression": 3, "security": 4, "usability": 5,
        "performance": 6, "acceptance": 7, "functional": 8, "compatibility": 9}
BEH = {"positive": 2, "negative": 3, "destructive": 4}
CODE = os.environ.get("QASE_PROJECT_CODE", PROJECT["code"])


def token():
    for line in open(os.path.join(ROOT, ".env")):
        if line.startswith("QASE_TOKEN="):
            return line.split("=", 1)[1].strip()


TOKEN = token()


def call(method, path, body=None):
    cmd = ["curl", "-s", "-X", method, API + path, "-H", f"Token: {TOKEN}",
           "-H", "Content-Type: application/json", "-H", "Accept: application/json"]
    if body is not None:
        cmd += ["--data-binary", "@-"]
    out = subprocess.run(cmd, input=json.dumps(body).encode() if body is not None else None,
                         capture_output=True, check=True).stdout
    d = json.loads(out)
    if not d.get("status"):
        raise SystemExit(f"{method} {path} -> {out.decode()[:500]}")
    return d


def upload(path):
    out = subprocess.check_output(["curl", "-s", "-X", "POST", f"{API}/attachment/{CODE}",
                                   "-H", f"Token: {TOKEN}", "-F", f"file=@{path}"])
    d = json.loads(out)
    if not d.get("status"):
        raise SystemExit(f"upload {path}: {d}")
    return d["result"][0]["hash"]


def load_state():
    if os.path.exists(STATE_F):
        return json.load(open(STATE_F))
    return {"project": False, "suites": {}, "cases": {}, "attachments": {}, "defects": {}}


def save(st):
    json.dump(st, open(STATE_F, "w"), ensure_ascii=False, indent=1)


def defect_key(d):
    return f"{d['screen']}|{d['title']}"


def defect_body(d, case_ref, img=lambda f: None):
    steps = "\n".join(f"{i}. {s}" for i, s in enumerate(d["steps"], 1))
    cases = ", ".join(case_ref(k) for k in d["cases"]) or "—"
    parts = [f"**Экран:** {d['screen']}", f"**Окружение:** {ENV}", "",
             "**Шаги воспроизведения**", steps, "",
             "**Ожидаемый результат**", d["expected"], "",
             "**Фактический результат**", d["actual"], "",
             "**Предлагаемое решение**", d["solution"], ""]
    if d.get("refs"):
        parts += ["**Референсы**"] + [f"- [{t}]({u})" for t, u in d["refs"]] + [""]
    parts += [f"**Связанные кейсы:** {cases}"]
    shots = [(f, img(f)) for f in d["files"]]
    if shots:
        parts += ["", "**Скриншоты**"] + [f"![{os.path.basename(f)}]({u or '../' + f})" for f, u in shots]
    if d["note"]:
        parts += ["", f"_Примечание: {d['note']}_"]
    return "\n".join(parts)


def defect_title(d, did=None):
    base = f"[{d['kind']}] {d['screen']}: {d['title']}"
    return f"#{did} {base}" if did else base


def sync(st):
    if not st["project"]:
        existing = call("GET", "/project?limit=100")["result"]["entities"]
        if not any(p["code"] == CODE for p in existing):
            call("POST", "/project", {"title": PROJECT["title"], "code": CODE,
                                      "description": PROJECT["description"], "access": "all"})
            print("project created", CODE)
        st["project"] = True; save(st)

    for key, (title, parent, desc) in SUITES.items():
        if key in st["suites"]:
            continue
        body = {"title": title, "description": desc}
        if parent:
            body["parent_id"] = st["suites"][parent]
        st["suites"][key] = call("POST", f"/suite/{CODE}", body)["result"]["id"]
        save(st)
    print("suites:", len(st["suites"]))

    for key, c in C.items():
        if key in st["cases"]:
            continue
        body = {"title": c["title"], "preconditions": c["pre"], "suite_id": st["suites"][c["suite"]],
                "severity": SEV[c["sev"]], "priority": PRI[c["pri"]], "type": TYPE[c["type"]],
                "behavior": BEH[c["behavior"]], "layer": 1, "automation": 0, "status": 0,
                "steps": [{"action": a, "expected_result": e} for a, e in c["steps"]]}
        st["cases"][key] = call("POST", f"/case/{CODE}", body)["result"]["id"]
        save(st)
    print("cases:", len(st["cases"]))

    for d in D:
        for f in d["files"]:
            if f not in st["attachments"]:
                st["attachments"][f] = upload(os.path.join(ROOT, f)); save(st)

    st.setdefault("urls", {})
    for f, h in st["attachments"].items():
        if f not in st["urls"]:
            st["urls"][f] = call("GET", f"/attachment/{h}")["result"]["full_path"]; save(st)
    img = lambda f: st["urls"].get(f)
    ref = lambda k: f"{CODE}-{st['cases'][k]} ({C[k]['title']})"
    update = "--update" in sys.argv
    for d in D:
        k = defect_key(d)
        body = {"title": defect_title(d, st["defects"].get(k)), "actual_result": defect_body(d, ref, img),
                "severity": SEV[d["sev"]],
                "attachments": [st["attachments"][f] for f in d["files"]]}
        if k in st["defects"]:
            if update:
                call("PATCH", f"/defect/{CODE}/{st['defects'][k]}", body)
            continue
        st["defects"][k] = call("POST", f"/defect/{CODE}", body)["result"]["id"]
        save(st)
        call("PATCH", f"/defect/{CODE}/{st['defects'][k]}", {"title": defect_title(d, st["defects"][k])})
    print("defects:", len(st["defects"]))


def render_md(st):
    cid = lambda k: f"{CODE}-{st['cases'][k]}" if k in st.get("cases", {}) else k
    out = [f"# {PROJECT['title']} — тест-кейсы", "", f"Окружение: {ENV}", ""]
    children = {}
    for k, (t, p, _) in SUITES.items():
        children.setdefault(p, []).append(k)

    def walk(parent, level):
        for sk in children.get(parent, []):
            out.append(f"{'#' * level} {SUITES[sk][0]}"); out.append("")
            for ck, c in C.items():
                if c["suite"] != sk:
                    continue
                out.append(f"{'#' * (level + 1)} {cid(ck)}. {c['title']}")
                out.append(f"- Severity: {c['sev']} · Priority: {c['pri']} · Type: {c['type']} · Behavior: {c['behavior']}")
                if c["pre"]:
                    out.append(f"- Предусловия: {c['pre']}")
                for i, (a, e) in enumerate(c["steps"], 1):
                    out.append(f"  {i}. {a} → {e}")
                out.append("")
            walk(sk, level + 1)
    walk(None, 2)
    open(os.path.join(ROOT, "test-cases", "test-cases.md"), "w").write("\n".join(out))

    ref = lambda k: f"{cid(k)} ({C[k]['title']})"
    out = [f"# {PROJECT['title']} — дефекты", ""]
    for d in D:
        did = st.get("defects", {}).get(defect_key(d))
        out.append(f"## {defect_title(d, did)}")
        out.append(f"Severity: {d['sev']}" + (f" · Вложения: {', '.join(d['files'])}" if d["files"] else ""))
        out.append(""); out.append(defect_body(d, ref)); out.append("")
    open(os.path.join(ROOT, "defects", "defects.md"), "w").write("\n".join(out))
    print("markdown rendered")

if __name__ == "__main__":
    st = load_state()
    if "--dry" not in sys.argv:
        sync(st)
    render_md(st)
