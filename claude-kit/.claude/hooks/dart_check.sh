#!/usr/bin/env bash
# После каждого изменения .dart-файла: форматирование и анализ этого файла.
# Ошибки анализа возвращаются агенту (exit 2), и он исправляет их сразу.
input=$(cat)
file=$(printf '%s' "$input" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("file_path",""))')

case "$file" in
  *.dart) ;;
  *) exit 0 ;;
esac
[ -f "$file" ] || exit 0

dart format "$file" >/dev/null 2>&1

if ! out=$(dart analyze --fatal-infos "$file" 2>&1); then
  echo "dart analyze нашёл проблемы в $file:" >&2
  echo "$out" >&2
  exit 2
fi
exit 0
