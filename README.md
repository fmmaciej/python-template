# python-template

Szablon projektu Python oparty o Copier.

Pozwala szybko wygenerować nowe repozytorium z gotową konfiguracją narzędzi i wybranym wariantem struktury projektu:

| Tryb        | Opis                                                           |
| ----------- | -------------------------------------------------------------- |
| `script`    | Prosty projekt skryptowy, z jednym plikiem wejściowym          |
| `flat`      | Prosty projekt pakietowy CLI, z płaską strukturą               |
| `hexagonal` | Projekt pakietowy CLI z podstawową strukturą hexagonalną       |

Każdy wygenerowany projekt dostaje minimalny zestaw startowy:

- konfigurację `ruff`, `mypy`, `pytest`, `pre-commit` i `just`
- przykładowy entrypoint dla wybranego wariantu
- katalog `tests/` z prostym smoke testem, żeby `pytest` i `mypy` działały od razu po wygenerowaniu

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

`just render-flat`

Wygenerowanie wariantu `package + hexagonal`:

`just render-hex`

Wygenerowanie wariantu `script`:

`just render-script`

Wygenerowanie wszystkich wariantów testowych (wrzucane są do `examples/`):

`just smoke`

Smoke testy repozytorium renderują każdy wariant i sprawdzają nie tylko obecność kluczowych plików, ale też podstawowy workflow wygenerowanego projektu:

- `uv run pytest`
- `uv run mypy ...`

Jeśli chcesz, po renderze możesz też ręcznie przejrzeć katalogi w `examples/`, ale podstawowa walidacja renderu i startowego workflow jest wykonywana automatycznie.

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
4. Opcjonalnie ręcznie przeglądasz wygenerowane projekty w `examples/`
5. Commitujesz zmiany
