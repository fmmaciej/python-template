# python-template

Szablon projektu Python oparty o Copier.

Pozwala szybko wygenerować nowe repozytorium z gotową konfiguracją narzędzi i wybranym wariantem struktury projektu:

| Tryb        | Opis                                                           |
| ----------- | -------------------------------------------------------------- |
| `script`    | Prosty projekt skryptowy, z jednym plikiem wejściowym          |
| `flat`      | Prosty projekt pakietowy CLI, z płaską strukturą               |
| `hexagonal` | Projekt pakietowy CLI z podstawową strukturą hexagonalną       |

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

Ruff lint:

`just ruff`

Automatyczne poprawki ruff lint:

`just ruff-fix`

Sprawdzanie typów:

`just mypy`

Uruchomienie testów:

`just test`

Pełny zestaw sprawdzeń:

`just check`

## Testowanie renderowania szablonu

Wygenerowanie wariantu `package + flat`:

`just flat`

Wygenerowanie wariantu `package + hexagonal`:

`just hexagonal`

Wygenerowanie wariantu `script`:

`just script`

Wygenerowanie wszystkich wariantów testowych (wrzucane są do `examples/`):

`just smoke`

Usunięcie katalogów testowych z `examples/`:

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

| Plik / katalog           | Opis                                     |
| ------------------------ | ---------------------------------------- |
| `copier.yml`             | pytania i konfiguracja Copiera           |
| `docs/`                  | przydatne informacje                     |
| `template/common/`       | pliki wspólne dla wszystkich wariantów   |
| `template/variants/`     | pliki zależne od wybranego wariantu      |
| `tests/`                 | testy szablonu                           |
| `scripts/`               | pomocnicze skrypty developerskie         |
| `scripts/post_render.py` | składanie końcowego projektu po renderze |

## Workflow

1. Zmieniasz pliki template
2. Uruchamiasz `just check`
3. Uruchamiasz `just smoke`
4. Sprawdzasz wygenerowane projekty
5. Commitujesz zmiany
