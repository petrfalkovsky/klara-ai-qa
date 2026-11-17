---
paths:
  - "lib/ui/**/*.dart"
---

# UI-кит и вёрстка

- Shared-компоненты — в `lib/ui/core/ui/`: `AppScaffold`, `AppSheet`, `AppButton`, `AppSwitch`, `AppToast`, `AppDropdown`, `ConsentCheckbox`. Перед созданием нового виджета проверь этот каталог.
- Новый вариант компонента — новый опциональный параметр существующего виджета. Копировать виджет под задачу запрещено.
- `AppScaffold` отвечает за фон (`Positioned.fill` на нижнем слое), прокрутку тела и safe area. Нижний слот действий оборачивается в `SafeArea(top: false, minimum: EdgeInsets.only(bottom: tokens.screenBottom))`: SafeArea берёт максимум из системного inset и minimum, поэтому отступ корректен и на iPhone SE, и на iPhone с Face ID.
- Токены (отступы, радиусы, цвета, длительности анимаций) — в `lib/ui/core/themes/` через `ThemeExtension`. В экранах — только обращение к токенам.
- Цвет иконок — из `IconTheme` или `ColorScheme`; SVG окрашиваются через `colorFilter` из темы.
- Выпадающие меню — `AppDropdown` на `OverlayPortal`: перед удалением из дерева вызывается `reverse()` анимации.
- Текст в ограниченных фигурах — `maxLines` и `FittedBox(fit: BoxFit.scaleDown)`.
- Декоративные элементы — в `ExcludeSemantics`.
- Прямое использование `Switch`, `CupertinoSwitch`, `showModalBottomSheet`, `ScaffoldMessenger` и сторонних UI-пакетов вне `lib/ui/core/` запрещено.
