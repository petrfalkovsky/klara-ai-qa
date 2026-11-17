#!/usr/bin/env bash
# Единая команда проверки. Её используют разработчики, CI и hook Claude Code.
# Запуск: ./tool/verify.sh          — быстрая проверка
#         ./tool/verify.sh --e2e    — плюс E2E-сценарии Patrol на запущенном симуляторе
set -euo pipefail

step() { printf '\n▶ %s\n' "$1"; }

step "Форматирование"
dart format --output=none --set-exit-if-changed lib test

step "Анализ"
flutter analyze --fatal-infos

if grep -q "custom_lint" pubspec.yaml; then
  step "Lint-правила проекта"
  dart run custom_lint
fi

step "Генерация локализаций"
flutter gen-l10n

step "Unit-, Bloc-, widget- и golden-тесты"
flutter test

if [ "${1:-}" = "--e2e" ]; then
  step "E2E-сценарии"
  patrol test
fi

printf '\n✅ verify пройден\n'
