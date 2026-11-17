# -*- coding: utf-8 -*-
"""Предлагаемые решения дефектов: причина в дереве виджетов, варианты, референсы.
Ключ — заголовок дефекта из qase_data.py. Причины — гипотезы внешнего тестировщика:
исходный код приложения недоступен, команде нужно их подтвердить."""

R = {
    # Архитектура и паттерны Flutter
    "compass_case": ("Flutter docs — Architecture case study (Compass app, shared-виджеты в ui/core)",
                     "https://docs.flutter.dev/app-architecture/case-study"),
    "compass_repo": ("GitHub flutter/samples — compass_app", "https://github.com/flutter/samples/tree/main/compass_app"),
    "optimistic": ("Flutter docs — Optimistic state", "https://docs.flutter.dev/app-architecture/design-patterns/optimistic-state"),
    "command": ("Flutter docs — Command pattern (состояния running / error)", "https://docs.flutter.dev/app-architecture/design-patterns/command"),
    "result": ("Flutter docs — Result pattern", "https://docs.flutter.dev/app-architecture/design-patterns/result"),
    "sealed": ("Dart — sealed classes", "https://dart.dev/language/class-modifiers#sealed"),
    "wonderous": ("GitHub gskinnerTeam/flutter-wonderous-app — эталонное open-source приложение", "https://github.com/gskinnerTeam/flutter-wonderous-app"),
    "wonderous_styles": ("Wonderous — lib/styles/styles.dart, класс _Insets (токены отступов $styles.insets)", "https://github.com/gskinnerTeam/flutter-wonderous-app/blob/main/lib/styles/styles.dart#L222"),
    "theme_ext": ("Flutter API — ThemeExtension (токены дизайн-системы)", "https://api.flutter.dev/flutter/material/ThemeExtension-class.html"),
    "colorscheme": ("Flutter API — ColorScheme (пары фон / контент)", "https://api.flutter.dev/flutter/material/ColorScheme-class.html"),
    "contrast_test": ("Flutter API — textContrastGuideline (проверка контраста в тестах)", "https://api.flutter.dev/flutter/flutter_test/textContrastGuideline-constant.html"),
    "custom_lint": ("pub.dev — custom_lint (свои lint-правила для команды)", "https://pub.dev/packages/custom_lint"),
    "claude_memory": ("Claude Code docs — CLAUDE.md, .claude/rules, skills", "https://code.claude.com/docs/en/memory"),
    # Каркас экрана и отступы
    "safearea": ("Flutter API — SafeArea", "https://api.flutter.dev/flutter/widgets/SafeArea-class.html"),
    "safearea_min": ("Flutter API — SafeArea.minimum (берётся максимум из inset и minimum)", "https://api.flutter.dev/flutter/widgets/SafeArea/minimum.html"),
    "scaffold_bottom": ("Flutter API — Scaffold.bottomNavigationBar (закреплённый нижний слот)", "https://api.flutter.dev/flutter/material/Scaffold/bottomNavigationBar.html"),
    "positioned_fill": ("Flutter API — Positioned.fill", "https://api.flutter.dev/flutter/widgets/Positioned/Positioned.fill.html"),
    "layoutbuilder": ("Flutter API — LayoutBuilder", "https://api.flutter.dev/flutter/widgets/LayoutBuilder-class.html"),
    "sliver_appbar": ("Flutter API — SliverAppBar", "https://api.flutter.dev/flutter/material/SliverAppBar-class.html"),
    "cupertino_sliver_nav": ("Flutter API — CupertinoSliverNavigationBar", "https://api.flutter.dev/flutter/cupertino/CupertinoSliverNavigationBar-class.html"),
    "sliver_header": ("Flutter API — SliverPersistentHeader", "https://api.flutter.dev/flutter/widgets/SliverPersistentHeader-class.html"),
    "cupertino_list": ("Flutter API — CupertinoListSection", "https://api.flutter.dev/flutter/cupertino/CupertinoListSection-class.html"),
    "ensure_visible": ("Flutter API — Scrollable.ensureVisible", "https://api.flutter.dev/flutter/widgets/Scrollable/ensureVisible.html"),
    # Sheets
    "modal_bs": ("Flutter API — showModalBottomSheet (showDragHandle, isDismissible)", "https://api.flutter.dev/flutter/material/showModalBottomSheet.html"),
    "cupertino_sheet": ("Flutter API — showCupertinoSheet", "https://api.flutter.dev/flutter/cupertino/showCupertinoSheet.html"),
    "cupertino_sheet_cookbook": ("Flutter cookbook — Cupertino sheets", "https://docs.flutter.dev/cookbook/design/cupertino-sheets"),
    "draggable_ctrl": ("Flutter API — DraggableScrollableController.animateTo", "https://api.flutter.dev/flutter/widgets/DraggableScrollableController-class.html"),
    "wolt": ("GitHub woltapp/wolt_modal_sheet — sheets из продакшена Wolt", "https://github.com/woltapp/wolt_modal_sheet"),
    "smooth_sheets": ("pub.dev — smooth_sheets (iOS-подобные sheets)", "https://pub.dev/packages/smooth_sheets"),
    # Анимации и состояния
    "animated_switcher": ("Flutter API — AnimatedSwitcher", "https://api.flutter.dev/flutter/widgets/AnimatedSwitcher-class.html"),
    "animated_size": ("Flutter API — AnimatedSize", "https://api.flutter.dev/flutter/widgets/AnimatedSize-class.html"),
    "overlay_portal": ("Flutter API — OverlayPortal", "https://api.flutter.dev/flutter/widgets/OverlayPortal-class.html"),
    "flutter_animate": ("pub.dev — flutter_animate (gskinner)", "https://pub.dev/packages/flutter_animate"),
    "skeletonizer": ("pub.dev — skeletonizer", "https://pub.dev/packages/skeletonizer"),
    "keepalive": ("Flutter API — AutomaticKeepAliveClientMixin", "https://api.flutter.dev/flutter/widgets/AutomaticKeepAliveClientMixin-mixin.html"),
    "indexed_stack": ("Flutter API — IndexedStack", "https://api.flutter.dev/flutter/widgets/IndexedStack-class.html"),
    "haptic": ("Flutter API — HapticFeedback", "https://api.flutter.dev/flutter/services/HapticFeedback-class.html"),
    # Компоненты
    "cupertino_switch": ("Flutter API — CupertinoSwitch", "https://api.flutter.dev/flutter/cupertino/CupertinoSwitch-class.html"),
    "switch_adaptive": ("Flutter API — Switch.adaptive", "https://api.flutter.dev/flutter/material/Switch/Switch.adaptive.html"),
    "scaffold_messenger": ("Flutter API — ScaffoldMessenger", "https://api.flutter.dev/flutter/material/ScaffoldMessenger-class.html"),
    "toastification": ("pub.dev — toastification", "https://pub.dev/packages/toastification"),
    "button_icon_color": ("Flutter API — ButtonStyle.iconColor", "https://api.flutter.dev/flutter/material/ButtonStyle/iconColor.html"),
    "widget_state": ("Flutter API — WidgetStateProperty (стили по состояниям кнопки)", "https://api.flutter.dev/flutter/widgets/WidgetStateProperty-class.html"),
    "icon_theme": ("Flutter API — IconTheme", "https://api.flutter.dev/flutter/widgets/IconTheme-class.html"),
    "icon_weight": ("Flutter API — IconThemeData.weight (толщина вариативных иконок)", "https://api.flutter.dev/flutter/widgets/IconThemeData/weight.html"),
    "flutter_svg": ("pub.dev — flutter_svg (colorFilter из темы)", "https://pub.dev/packages/flutter_svg"),
    "exclude_semantics": ("Flutter API — ExcludeSemantics", "https://api.flutter.dev/flutter/widgets/ExcludeSemantics-class.html"),
    "fitted": ("Flutter API — FittedBox", "https://api.flutter.dev/flutter/widgets/FittedBox-class.html"),
    "auto_size_text": ("pub.dev — auto_size_text", "https://pub.dev/packages/auto_size_text"),
    "context_menu": ("Flutter API — CupertinoContextMenu", "https://api.flutter.dev/flutter/cupertino/CupertinoContextMenu-class.html"),
    # Чат и ввод
    "textpainter": ("Flutter API — TextPainter (замер последней строки текста)", "https://api.flutter.dev/flutter/painting/TextPainter-class.html"),
    "flyer_status": ("Flyer Chat docs — timeAndStatusPosition.inline", "https://flyer-astro.pages.dev/docs/flutter/guides/status-indicators"),
    "flyer_text": ("pub.dev — flyer_chat_text_message", "https://pub.dev/packages/flyer_chat_text_message"),
    "focus": ("Flutter cookbook — Focus and text fields", "https://docs.flutter.dev/cookbook/forms/focus"),
    "tap_region": ("Flutter API — TextFieldTapRegion", "https://api.flutter.dev/flutter/widgets/TextFieldTapRegion-class.html"),
    "on_tap_outside": ("Flutter API — TextField.onTapOutside", "https://api.flutter.dev/flutter/material/TextField/onTapOutside.html"),
    "context_menu_builder": ("Flutter API — TextField.contextMenuBuilder", "https://api.flutter.dev/flutter/material/TextField/contextMenuBuilder.html"),
    "hint_max_lines": ("Flutter API — InputDecoration.hintMaxLines", "https://api.flutter.dev/flutter/material/InputDecoration/hintMaxLines.html"),
    "record": ("pub.dev — record (амплитуда для индикатора записи)", "https://pub.dev/packages/record"),
    # Платформа, контент, локализация
    "sign_in_apple": ("pub.dev — sign_in_with_apple", "https://pub.dev/packages/sign_in_with_apple"),
    "webview": ("pub.dev — webview_flutter (NavigationDelegate)", "https://pub.dev/packages/webview_flutter"),
    "md_plus": ("pub.dev — flutter_markdown_plus (преемник flutter_markdown)", "https://pub.dev/packages/flutter_markdown_plus"),
    "l10n": ("Flutter docs — Internationalization (gen-l10n, ARB)", "https://docs.flutter.dev/ui/accessibility-and-internationalization/internationalization"),
    "gdpr9": ("GDPR ст. 9 — особые категории данных (здоровье)", "https://gdpr-info.eu/art-9-gdpr/"),
}

DS = "Общий каркас решения — в дефекте #54 «Сквозное · дизайн-система»."

SOL = {}

def s(title, text, refs):
    SOL[title] = (text, refs)

# ===== Авторизация
s("Иконка телефона толще иконок Apple и Google",
  "Вероятная причина: иконки из разных наборов. Логотипы Apple и Google — брендовые SVG, телефон — шрифтовая иконка с другой толщиной.\n"
  "Решение: все иконки кнопок входа берутся из одного набора через общий виджет кнопки авторизации. Размер и цвет приходят из IconTheme. "
  "Для вариативных шрифтовых иконок толщина задаётся один раз в IconThemeData.weight на уровне темы — в коде экрана её не трогают.",
  ["icon_theme", "icon_weight"])
s("Фоновый текст перекрывает заголовок на iPhone SE",
  "Вероятная причина: декоративный фон и заголовок позиционированы в одном Stack абсолютными координатами от верха экрана, без учёта доступной высоты.\n"
  "Решение: развести слои. Декор — нижний слой Stack через Positioned.fill, вне SafeArea. Контент — в SafeArea, раскладка через Column и Spacer внутри LayoutBuilder, поэтому позиции зависят от высоты. "
  "Если высоты не хватает, второстепенный декоративный текст скрывается по правилу из токенов дизайн-системы — без проверок под конкретную модель айфона. "
  "Пример адаптивных размеров по устройству — масштабируемые токены в Wonderous.",
  ["positioned_fill", "layoutbuilder", "safearea", "wonderous_styles"])
s("Разная механика согласия: при входе неявная, в WoMoon — обязательный чекбокс",
  "Решение продуктовое и юридическое: выбрать одну политику согласий и реализовать её одним компонентом.\n"
  "Вариант А: явный чекбокс везде (регистрация, 18+, данные о здоровье). Один shared-виджет ConsentCheckbox с состоянием ошибки.\n"
  "Вариант Б: неявное согласие текстом там, где закон это позволяет, и явное для особых категорий данных (здоровье — ст. 9 GDPR). Тогда рядом с чекбоксом WoMoon нужно пояснение, почему здесь требуется отдельное действие.",
  ["gdpr9"])
s("Первая попытка входа зависает без сообщения об ошибке",
  "Вероятная причина: исключение из Sign in with Apple (например, SignInWithAppleAuthorizationException) или ошибка обмена токена на бэкенде не обрабатывается, и UI остаётся в ожидании.\n"
  "Решение: оформить вход как Command (паттерн из документации Flutter). Пока команда в состоянии running, кнопка показывает загрузку и заблокирована. "
  "Результат возвращается как Result: отмена пользователем — тихий возврат, ошибка — сообщение и кнопка «Повторить». "
  "Каждую ошибку логировать с кодом в Crashlytics или Sentry: так станет понятна причина нестабильного воспроизведения.",
  ["sign_in_apple", "command", "result"])
s("Нет тактильного отклика при успешном входе",
  "Решение: вызывать хаптику из одного сервиса приложения (обёртка над HapticFeedback), а не точечно на экранах. Успешное завершение команды входа вызывает событие success.\n"
  "Проверить: подтверждение Touch ID на iOS само даёт системный отклик. Возможно, его гасит кастомный экран-оверлей.",
  ["haptic"])
s("Ссылки на условия и политику открывают WebView с cookie-баннером сайта",
  "Вариант А (рекомендуемый): нативный экран документа. Текст хранится на сервере в Markdown — единый источник для сайта и приложения. "
  "Приложение рендерит его через flutter_markdown_plus и кэширует на устройстве для офлайн-доступа.\n"
  "Вариант Б: если WebView остаётся — открывать встраиваемую версию страницы без cookie-баннера и навигации сайта, "
  "а в webview_flutter через NavigationDelegate разрешить только домен myklara.ai.",
  ["md_plus", "webview"])

# ===== Главный экран
s("Текст карточки виртуальной карты перекрывает «Добро пожаловать» на iPhone SE",
  "Вероятная причина: карточки фиксированной высоты, текст позиционирован абсолютно.\n"
  "Решение: экран строится на CustomScrollView. Высоты карточек определяются контентом, адаптация — через LayoutBuilder и токены дизайн-системы. "
  "Второстепенный текст скрывается правилом компонента карточки при нехватке места.",
  ["layoutbuilder", "theme_ext"])
s("Тап по полю ввода открывает чат без активной клавиатуры",
  "Решение: передавать в маршрут чата намерение сфокусировать поле. После завершения анимации маршрута вызывать focusNode.requestFocus(), "
  "чтобы клавиатура не конфликтовала с анимацией открытия. "
  "Если анимация короткая — достаточно TextField.autofocus.",
  ["focus"])

# ===== AI-чат
s("Время и статус сообщения всегда переносятся на отдельную строку",
  "Вариант А: свой виджет текста сообщения. Последняя строка замеряется через TextPainter. Если справа хватает места под время и статус, блок рисуется в правом нижнем углу той же строки. "
  "Если не хватает — переносится на новую строку. Это приём Telegram.\n"
  "Вариант Б: взять готовую реализацию flyer_chat_text_message с timeAndStatusPosition.inline.",
  ["textpainter", "flyer_status", "flyer_text"])
s("Текст в пузыре заходит в зону скругления угла",
  "Решение: радиус скругления и внутренний отступ пузыря — один токен темы (ChatBubbleTheme через ThemeExtension). "
  "Отступ вычисляется из радиуса внутри токена, поэтому поменять одно без другого нельзя.",
  ["theme_ext"])
s("Лайк закрашивается с задержкой около 0,5 с",
  "Вероятная причина: иконка обновляется после ответа сервера.\n"
  "Решение: паттерн Optimistic state из документации Flutter. ViewModel меняет состояние сразу, запрос идёт в фоне, при ошибке состояние откатывается и показывается тост.",
  ["optimistic", "command"])
s("Реакции вынесены отдельным блоком под сообщением",
  "Решение: реакция становится частью виджета пузыря — бейдж в углу. Выбор реакции — по долгому тапу через контекстное меню, как в Telegram и iMessage.",
  ["context_menu"])
s("Подсказка «Разобрать мои траты» постоянно закреплена над полем ввода",
  "Вариант А: подсказки — последний элемент списка сообщений. Они прокручиваются вместе с историей и уходят из поля зрения.\n"
  "Вариант Б: плавающий SliverPersistentHeader, который прячется при прокрутке и появляется при обратном скролле.\n"
  "Отступы над подсказкой и под полем ввода берутся из одного токена.",
  ["sliver_header", "theme_ext"])
s("Список чатов закрывается без анимации",
  "Вероятная причина: меню удаляется из дерева сразу (if/else или OverlayEntry.remove) без обратной анимации.\n"
  "Вариант А: shared-виджет выпадающего меню на OverlayPortal и AnimationController. Перед скрытием вызывается reverse(), и только потом меню уходит из дерева. "
  "Этот же компонент используется для меню вложений.\n"
  "Вариант Б: одна общая конфигурация эффектов flutter_animate для появления и скрытия всех всплывающих элементов.\n" + DS,
  ["overlay_portal", "animated_switcher", "flutter_animate"])
s("Карточка «Я хочу: Отслеживать мое здоровье» непонятна пользователю",
  "Решение продуктовое: у карточек «Я хочу…» должен быть заголовок и контекст (зачем выбор, что даёт ✨). Сценарий здоровья — отдельный флоу WoMoon; в онбординге — только как явно помеченная опция.",
  [])
s("Плейсхолдер поля ввода переносится на две строки на iPhone SE",
  "Решение: InputDecoration.hintMaxLines = 1 и короткий текст плейсхолдера в ARB. "
  "Кнопки «+» и микрофон выравниваются по нижней строке (CrossAxisAlignment.end), как в мессенджерах: при многострочном вводе они остаются у последней строки.",
  ["hint_max_lines", "l10n"])
s("Тап по пустой области поля показывает «Выбрать всё / Сканировать текст», промах сворачивает клавиатуру",
  "Вероятная причина: фокус снимается глобальным GestureDetector или onTapOutside, а отступы контейнера поля не считаются частью поля.\n"
  "Решение: обернуть весь контейнер композера в TextFieldTapRegion — тапы по его отступам не снимают фокус. "
  "Состав меню выделения настроить через contextMenuBuilder.",
  ["tap_region", "on_tap_outside", "context_menu_builder"])
s("Индикатор записи и иконка «Отправить» смещены от центра",
  "Вероятная причина: несимметричные соседи в Row, а глиф самолётика оптически смещён в самом ассете.\n"
  "Решение: кнопки — слоты одинакового размера из токенов, волна — Expanded между ними. "
  "Оптическую компенсацию глифа исправить в SVG (viewBox), а не отступами в коде.",
  ["theme_ext"])
s("Во время записи неочевидно, что голос записывается",
  "Решение: состояние композера — явная модель (idle / recording / processing), отрисовываемая одним компонентом. "
  "Во время записи — пульсация кнопки (flutter_animate с повтором) и волна по реальной амплитуде (record, onAmplitudeChanged), а также таймер.",
  ["flutter_animate", "record", "sealed"])
s("Кнопки «Стоп» и «Отправить» стоят рядом справа",
  "Вариант А: отмена и удаление записи слева, отправка справа — как в ChatGPT.\n"
  "Вариант Б: одна кнопка. Удержание — запись, отпускание — отправка, свайп влево — отмена — как в Telegram.\n"
  "В обоих случаях переходы между состояниями — через AnimatedSwitcher в одном виджете композера.",
  ["animated_switcher"])
s("Меню «Файл / Изображение / Камера» без анимации",
  "Решение: тот же shared-виджет выпадающего меню, что и для списка чатов (OverlayPortal с прямой и обратной анимацией), "
  "или общая конфигурация flutter_animate.\n" + DS,
  ["overlay_portal", "flutter_animate"])
s("Полное сворачивание окна чата свайпом происходит скачком",
  "Вероятная причина: окно — DraggableScrollableSheet с точками привязки. При достижении минимума виджет удаляется из дерева без анимации.\n"
  "Вариант А: при свайпе ниже порога вызывать DraggableScrollableController.animateTo(0) с той же кривой, что у кнопки «свернуть», и только потом закрывать.\n"
  "Вариант Б: окно чата как маршрут-sheet (smooth_sheets) — анимация закрытия жестом встроена.",
  ["draggable_ctrl", "smooth_sheets"])

# ===== Финансы — sheets
SHEET = ("Вариант А: один shared-виджет AppSheet поверх showModalBottomSheet (showDragHandle: true) или showCupertinoSheet. "
         "Закрытие свайпом и тапом по фону даёт сам маршрут, поэтому крестик, Cancel и Back не нужны. "
         "Если контенту нужен скролл — он использует ScrollController sheet-а, и свайп вниз от начала контента закрывает sheet. "
         "Статичный контент не прокручивается и не пружинит.\n"
         "Вариант Б: готовые решения из продакшена — wolt_modal_sheet (Wolt) или smooth_sheets: многостраничные sheets с корректными жестами.\n" + DS)
s("Лишний крестик и overscroll вместо закрытия свайпом", SHEET,
  ["modal_bs", "cupertino_sheet", "cupertino_sheet_cookbook", "wolt", "smooth_sheets"])
s("Декоративная иконка микрофона выглядит кнопкой",
  "Решение: убрать иконку или сделать её частью иллюстрации. Декоративные элементы оборачивать в ExcludeSemantics, чтобы VoiceOver не объявлял их интерактивными.",
  ["exclude_semantics"])
s("Иконка «Проанализируй мои расходы» неконтрастна",
  "Решение: цвет иконки — из пары ColorScheme (container / onContainer), без отдельного HEX на экране. "
  "Тогда контраст гарантирует тема. В widget-тесты добавить проверку meetsGuideline(textContrastGuideline).",
  ["colorscheme", "contrast_test"])
s("Кнопка «Привязать новый банк» выглядит неактивной",
  "Решение: shared-кнопка с вариантами (primary / secondary / text). Стили по состояниям — через WidgetStateProperty. "
  "Неактивный стиль применяется только при onPressed == null, поэтому активная кнопка не может выглядеть заблокированной.\n" + DS,
  ["widget_state", "colorscheme"])
s("Экран привязки банка открывается на английском",
  "Вероятная причина: строки экрана не вынесены в ARB, или это SDK open banking-агрегатора со своей локалью.\n"
  "Решение: для нативного экрана — строки в ARB (gen-l10n) и lint-правило на строковые литералы в виджетах. "
  "Для SDK агрегатора — передавать текущую локаль приложения в его конфигурацию.",
  ["l10n", "custom_lint"])
s("Экран открывается несколько раз при повторных тапах",
  "Решение: действие перехода оформить как Command. Пока команда в состоянии running, повторный вызов игнорируется. "
  "Вариант на уровне дизайн-системы: shared-кнопка сама блокируется, пока выполняется её асинхронный onPressed, — защита появляется во всём приложении сразу.\n" + DS,
  ["command"])
s("Заголовок «Financial OS» не соответствует действию «Привязать банк»",
  "Решение: заголовок экрана описывает действие («Привязать банк») и берётся из ARB. Брендовое название раздела — в подзаголовке или на карточке главного экрана.",
  ["l10n"])
s("Список банков пуст до ввода первого символа в поиск",
  "Вероятная причина: загрузка запускается из onChanged поля поиска, а не при создании экрана.\n"
  "Решение: ViewModel запускает команду load при создании (как в Compass app). Поиск фильтрует уже загруженный список локально; для серверного поиска — debounce.",
  ["command", "compass_case"])
s("Три способа закрыть sheet", SHEET,
  ["modal_bs", "cupertino_sheet", "wolt", "smooth_sheets"])
s("«Show instruction» сдвигает кнопки, при сворачивании анимация дёргается",
  "Вероятная причина: кнопки внутри прокручиваемого контента, а одновременно анимируются высота sheet и высота блока.\n"
  "Решение: каркас sheet — прокручиваемая часть (Expanded) и закреплённый нижний слот действий. "
  "Отступ слота — SafeArea(top: false, minimum: токен). Раскрываемый блок — AnimatedSize с Curves.easeInOut; анимируется только он.",
  ["animated_size", "safearea_min", "scaffold_bottom"])
s("Четыре элемента навигации на sheet Financial OS", SHEET,
  ["modal_bs", "cupertino_sheet", "wolt", "smooth_sheets"])

# ===== Здоровье и лайфстайл
s("Sheet трекера открывается с заметной задержкой после тактильного отклика",
  "Вероятная причина: sheet открывается после await загрузки данных.\n"
  "Решение: открывать маршрут сразу и показывать skeleton (skeletonizer), данные грузить внутри. "
  "Дополнительно — предзагрузка данных трекера при открытии главного экрана.",
  ["skeletonizer"])
s("Кнопка «Начать» неактивна без подсказки, что нужно подтвердить 18+",
  "Решение: кнопка всегда активна, валидация — при нажатии. Если согласие не отмечено: Scrollable.ensureVisible к чекбоксу и shake-эффект (flutter_animate .shake()). "
  "Чекбокс — shared-виджет формы с состоянием ошибки, единый для всех согласий.",
  ["ensure_visible", "flutter_animate"])
s("При прокрутке текст под виджетом «Овуляция» перекрывается белой подложкой",
  "Вероятная причина: у закреплённого блока непрозрачный Container с белым фоном.\n"
  "Решение: закреплённая часть — SliverPersistentHeader с фоном из темы (или blur). Если закрепление не нужно, блок прокручивается вместе с контентом без подложки.",
  ["sliver_header", "colorscheme"])
s("Текст «Изменения мышления и творчества» не помещается в голубой шар",
  "Решение: текст внутри фигуры с ограничением строк и FittedBox(fit: BoxFit.scaleDown) или auto_size_text. "
  "Проверять на самой длинной локали через псевдолокализацию.",
  ["fitted", "auto_size_text"])

# ===== Сообщество
s("Skeleton залипает, данные табов перезапрашиваются при каждом переключении",
  "Вероятная причина: каждый таб создаёт свой запрос в initState, а TabBarView уничтожает неактивные табы.\n"
  "Вариант А (архитектурный): данные живут в репозитории, который кэширует ответ. ViewModel таба читает кэш и обновляет его в фоне — как источник истины в Compass app.\n"
  "Вариант Б (на уровне виджетов): AutomaticKeepAliveClientMixin или IndexedStack, чтобы табы не пересоздавались.\n"
  "Переход skeleton → контент — через AnimatedSwitcher.",
  ["compass_case", "keepalive", "indexed_stack", "skeletonizer", "animated_switcher"])
s("Белая полоса по левому и верхнему краю на iPhone SE",
  "Вероятная причина: фон находится внутри SafeArea или Padding, либо изображение масштабируется без BoxFit.cover.\n"
  "Решение: фон экрана задаёт общий каркас экрана (слот background), а не каждый экран. "
  "Внутри каркаса фон — Positioned.fill с BoxFit.cover на нижнем слое Stack, SafeArea применяется только к контенту.\n" + DS,
  ["positioned_fill", "safearea"])
s("Текст кнопки «Копировать» неконтрастен в тёмной теме",
  "Решение: цвета текста кнопки — из пары ColorScheme через общую кнопку. Контраст проверяется тестом textContrastGuideline.\n" + DS,
  ["colorscheme", "contrast_test", "widget_state"])
s("Копирование кода под QR показывает «Ссылка скопирована»",
  "Решение: отдельные ключи ARB для «Код скопирован» и «Ссылка скопирована». Тост вызывается из обработчика конкретного действия.",
  ["l10n"])
s("Тосты появляются в разных местах и стилях",
  "Вариант А: один сервис уведомлений (обёртка над ScaffoldMessenger или Overlay) с типами success / error / info. "
  "Позиция и стиль заданы в теме, экраны вызывают только сервис.\n"
  "Вариант Б: toastification с глобальной конфигурацией через ToastificationWrapper, обёрнутый тонким адаптером в ui/core.\n" + DS,
  ["scaffold_messenger", "toastification"])
s("Заголовок без фона наезжает на контент",
  "Решение: экран на CustomScrollView с SliverAppBar(pinned: true) или CupertinoSliverNavigationBar. "
  "Фон заголовка и поведение при прокрутке даёт фреймворк, ручное позиционирование не нужно.",
  ["sliver_appbar", "cupertino_sliver_nav"])
s("Кнопка «Пригласить друга» прилипла к нижнему краю",
  "Вероятная причина: у iPhone SE нет home indicator, поэтому нижний inset равен 0. SafeArea без minimum даёт нулевой отступ, и кнопка прилипает. "
  "На iPhone с Face ID тот же код выглядит нормально, поэтому ошибка не заметна на устройствах разработчиков.\n"
  "Решение (принцип единственной ответственности): проверить, есть ли в проекте общий каркас экрана. За нижние отступы должен отвечать только он, а не каждый экран.\n"
  "• Каркас (AppScaffold) имеет слот bottomAction, который рендерится в Scaffold.bottomNavigationBar внутри SafeArea(top: false, minimum: EdgeInsets.only(bottom: токен)). "
  "SafeArea берёт максимум из системного inset и minimum, поэтому iPhone SE и iPhone с Face ID получают корректный отступ без условий по модели.\n"
  "• Значение минимума — токен темы (ThemeExtension), как $styles.insets в Wonderous; экраны числа не задают.\n"
  "• Для исключений (полноэкранный фон, камера) у каркаса есть флаги safeTop / safeBottom.\n"
  "Глобальный SafeArea в MaterialApp.builder не подходит: он обрезает фоны и sheets, которые должны уходить под статус-бар и home indicator.\n" + DS,
  ["safearea_min", "scaffold_bottom", "theme_ext", "wonderous_styles", "compass_case"])

# ===== Профиль и настройки
s("При открытии «Пробный / Подписка» на мгновение показывается ошибка null",
  "Вероятная причина: экран рендерит данные до загрузки (значение null попадает в Text), отдельного состояния loading нет.\n"
  "Решение: состояние экрана — sealed class (Loading / Data / Error) или Command + Result. Компилятор заставляет обработать каждый вариант. "
  "Последние данные подписки кэшируются в репозитории: экран открывается сразу с ними и обновляется в фоне.",
  ["sealed", "command", "result"])
s("Иконки не перекрашиваются при смене системной темы",
  "Вероятная причина: цвет иконок зашит в SVG или PNG либо задан константой Color(0xFF…), поэтому ThemeMode.system перекрашивает только то, что берёт цвет из Theme.\n"
  "Решение: цвет иконок — из IconTheme или ColorScheme. SVG окрашиваются через colorFilter из темы (flutter_svg). "
  "Lint-правило запрещает хардкод цветов вне файла темы.",
  ["icon_theme", "flutter_svg", "custom_lint"])
s("Языки обозначены флагами стран",
  "Решение: список строится из AppLocalizations.supportedLocales. Подпись — название языка на нём самом (Русский, Español, English) и код. Флаги не используются.",
  ["l10n"])
s("Экран не прокручивается, пункт Daily Horoscope недоступен на iPhone SE",
  "Вероятная причина: контент в Column без прокрутки.\n"
  "Решение: экраны настроек строятся на общем каркасе, где тело по умолчанию прокручивается (ListView с CupertinoListSection). "
  "Тогда экран без скролла нельзя сделать случайно.\n" + DS,
  ["cupertino_list"])
s("Одинаковые иконки у разных типов уведомлений",
  "Решение: соответствие «тип уведомления → иконка» задаётся в одном месте (enum с иконкой). Дизайнеру — подобрать отдельную иконку для каждого типа.",
  [])
s("Тумблеры без анимации и разных стилей",
  "Вероятная причина: часть тумблеров — кастомный виджет без анимации, в блоке «Подписка» — нативный CupertinoSwitch.\n"
  "Вариант А: один shared-виджет AppSwitch в ui/core — обёртка над CupertinoSwitch или Switch.adaptive с цветами из темы и опциональными параметрами (подпись, описание, состояние загрузки). "
  "Правило команды и Claude Code: новые экраны используют только AppSwitch, прямой Switch вне ui/core запрещён lint-правилом.\n"
  "Вариант Б: использовать CupertinoSwitch напрямую по всему приложению, стиль — через тему.\n" + DS,
  ["cupertino_switch", "switch_adaptive", "custom_lint", "claude_memory"])
s("Иконка на кнопке «Написать» неконтрастна в тёмной теме",
  "Решение: иконка и текст кнопки берут цвет из одного foregroundColor через ButtonStyle.iconColor. "
  "Рассинхрон цветов иконки и текста становится невозможен.\n" + DS,
  ["button_icon_color", "widget_state"])
s("Экран не прокручивается на iPhone SE",
  "Решение: как для настроек push-уведомлений — общий каркас с прокручиваемым телом по умолчанию.\n" + DS,
  ["cupertino_list"])

# ===== Сквозное
s("WebView ведут на сторонние домены",
  "Вариант А: справочный и юридический контент — нативные экраны с текстом с сервера.\n"
  "Вариант Б: если WebView неизбежен — страницы размещаются на myklara.ai, а NavigationDelegate блокирует переход на другие домены "
  "(ссылки наружу открываются в системном браузере, где пользователь видит адрес).",
  ["md_plus", "webview"])
s("Нет единого набора shared-виджетов и правил их переиспользования",
  "Вариант А — своя дизайн-система и правила для команды:\n"
  "1. Каталог shared-виджетов в lib/ui/core/ui/, токены — в lib/ui/core/themes/ через ThemeExtension (структура из официального Compass app). "
  "Минимальный набор: AppScaffold (отступы, фон, прокрутка), AppSheet, AppButton, AppSwitch, AppToast, AppDropdown, ConsentCheckbox, ChatBubble.\n"
  "2. Каждый виджет расширяется опциональными параметрами вместо копирования. Новый вариант — новый параметр, а не новый виджет.\n"
  "3. Правила для Claude Code в репозитории, общие для всей команды: короткое правило в CLAUDE.md и подробный каталог в .claude/rules/ui-kit.md или skill .claude/skills/ui-kit/. "
  "Содержание правил: перед созданием виджета найти аналог в каталоге; расширять существующий; новый shared-виджет сразу добавлять в каталог.\n"
  "4. Lint-правила (custom_lint) запрещают прямое использование Switch, showModalBottomSheet, ScaffoldMessenger и хардкод цветов вне ui/core.\n"
  "Вариант Б — готовые пакеты (wolt_modal_sheet, toastification, skeletonizer, flutter_animate) за тонкими адаптерами в ui/core. "
  "Экраны зависят от адаптера, поэтому смена пакета не затрагивает экраны.",
  ["compass_case", "compass_repo", "theme_ext", "wonderous", "custom_lint", "claude_memory",
   "wolt", "toastification", "skeletonizer", "flutter_animate"])


def apply(defects):
    titles = {d["title"] for d in defects}
    missing = titles - SOL.keys()
    extra = SOL.keys() - titles
    assert not missing and not extra, (missing, extra)
    for d in defects:
        text, refs = SOL[d["title"]]
        for r in refs:
            assert r in R, r
        d["solution"] = text
        d["refs"] = [R[r] for r in refs]
