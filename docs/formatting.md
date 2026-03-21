# EditorConfig vs VSCode settings

Krótka reguła:

- `.editorconfig` służy do trzymania **ogólnych zasad edycji plików**
- `.vscode/settings.json` służy do trzymania **ustawień specyficznych dla VSCode, języka i narzędzi**

## Cel

- `.editorconfig` ma być źródłem prawdy dla podstawowych zasad edycji
- `.vscode/settings.json` ma tylko uzupełniać workflow w VSCode

## Co trzymać w `.editorconfig`

Tutaj rzeczy związane z samą treścią plików, najlepiej takie, które mają działać podobnie niezależnie od edytora:

- kodowanie plików
- końce linii
- końcowy pusty wiersz
- usuwanie końcowych spacji
- typ wcięć
- szerokość wcięć
- wyjątki dla typów plików, np. inne wcięcia dla YAML/TOML/JSON

Przykłady:

- `charset = utf-8`
- `end_of_line = lf`
- `insert_final_newline = true`
- `trim_trailing_whitespace = true`
- `indent_style = space`
- `indent_size = 4`

## Co trzymać w `.vscode/settings.json`

Tutaj rzeczy zależne od VSCode albo od konkretnych rozszerzeń i narzędzi:

- interpreter Pythona
- integrację z `ruff`
- integrację z `pytest`
- ustawienia Pylance
- `formatOnSave`
- `codeActionsOnSave`
- skojarzenia typów plików, np. `*.jinja`
- ukrywanie katalogów typu `.venv`, `__pycache__`, `.ruff_cache`
- ustawienia terminala
- rzeczy specyficzne dla debugowania lub pracy w VSCode

Przykłady:

- `python.defaultInterpreterPath`
- `python.testing.pytestEnabled`
- `python.analysis.typeCheckingMode`
- `editor.codeActionsOnSave`
- `files.associations`
- `files.exclude`
- `search.exclude`

## Praktyczna zasada

Jeśli ustawienie dotyczy:

- **tekstu pliku i jego formatowania niezależnie od edytora** → daj do `.editorconfig`
- **zachowania VSCode albo rozszerzeń** → daj do `.vscode/settings.json`

## Czego nie dublować

Jeśli coś jest już sensownie ustawione w `.editorconfig`, nie ma potrzeby powtarzać tego w `settings.json`.

Najczęściej nie trzeba dublować:

- końcowych spacji
- final newline
- tabów / spacji
- rozmiaru wcięć
