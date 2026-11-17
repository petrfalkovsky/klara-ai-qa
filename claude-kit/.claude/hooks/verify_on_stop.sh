#!/usr/bin/env bash
# Перед завершением задачи: полная проверка, если в рабочей копии менялись .dart-файлы.
# При падении агент получает отчёт (exit 2) и продолжает работу вместо завершения.
input=$(cat)
active=$(printf '%s' "$input" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("stop_hook_active", False))')
# Защита от бесконечного цикла: повторный Stop после неудачной проверки пропускается.
[ "$active" = "True" ] && exit 0

cd "$CLAUDE_PROJECT_DIR" || exit 0
changed=$( { git diff --name-only HEAD; git ls-files --others --exclude-standard; } 2>/dev/null | grep -E '\.dart$' )
[ -z "$changed" ] && exit 0

if ! out=$(./tool/verify.sh 2>&1); then
  echo "tool/verify.sh не прошёл. Исправь ошибки перед завершением задачи:" >&2
  echo "$out" | tail -n 80 >&2
  exit 2
fi
exit 0
