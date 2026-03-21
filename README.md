# python-template

Szablon projektu Python oparty o Copier.

Pozwala szybko wygenerować nowe repozytorium z gotową konfiguracją narzędzi i wybranym wariantem struktury projektu:

- `no-package`
- `package + flat`
- `package + hexagonal`

## Wymagania

- Python 3.12+
- `uv`
- `just`
- `git`

## Instalacja

Utworzenie środowiska i instalacja zależności developerskich:

`uv sync`

Instalacja hooków pre-commit:

`uv run pre-commit install`

## Najważniejsze komendy

Instalacja zależności:

`uv sync`

Formatowanie kodu repozytorium szablonu:

`just format`

Lint:

`just ruff`

Automatyczne poprawki lint:

`just ruff-fix`

Sprawdzanie typów:

`just mypy`

Uruchomienie testów:

`just test`

Pełny zestaw sprawdzeń:

`just check`

## Testowanie renderowania szablonu

Wygenerowanie wariantu `package + flat`:

`just render-flat`

Wygenerowanie wariantu `package + hexagonal`:

`just render-hexagonal`

Wygenerowanie wariantu `no-package`:

`just render-no-package`

Wygenerowanie wszystkich wariantów testowych:

`just smoke`

Usunięcie katalogów testowych z `/tmp`:

`just clean`

## Ręczne użycie Copiera

Wygenerowanie projektu z pytaniami interaktywnymi:

`uv run copier copy . ../nowy-projekt --trust`

Wygenerowanie projektu z domyślnymi odpowiedziami:

`uv run copier copy . ../nowy-projekt --trust --defaults`

## Pre-commit

Uruchomienie hooków dla wszystkich plików:

`uv run pre-commit run --all-files`

## Struktura repozytorium

- `copier.yml` — pytania i konfiguracja Copiera
- `template/common/` — pliki wspólne dla wszystkich wariantów
- `template/variants/` — pliki zależne od wybranego wariantu
- `template/scripts/post_render.py.jinja` — składanie końcowego projektu po renderze
- `tests/` — testy szablonu
- `scripts/` — pomocnicze skrypty developerskie

## Workflow

1. Zmieniasz pliki template
2. Uruchamiasz `just check`
3. Uruchamiasz `just smoke`
4. Sprawdzasz wygenerowane projekty
5. Commitujesz zmiany
