# Development

Dokument dotyczy utrzymania repozytorium template, nie użycia wygenerowanego projektu.

## Setup

- `uv sync`
- `uv run pre-commit install`

## Najważniejsze komendy

- `just format`
- `just ruff`
- `just ruff-fix`
- `just mypy`
- `just test`
- `just check`
- `just copier ...`

`just copier ...` jest krótkim wrapperem na `uv run copier ...`.

## Render examples

- `just render-script`
- `just render-flat`
- `just render-hex`
- `just smoke`
- `just clean`

`just smoke` renderuje przykłady z aktualnego working tree, a nie z wersji odczytanej przez Copier jako źródło VCS.

## Tags and releases

W tym repo są dwa różne scenariusze pracy z template:

1. Lokalna praca nad template:

    - `just render-*`
    - `just smoke`
    - testy smoke z `tests/test_template_smoke.py`

    Te ścieżki renderują z aktualnego working tree, więc obejmują także lokalne, niezatwierdzone zmiany.

2. Użycie template jako repozytorium Git przez użytkownika:

    - Copier renderuje wskazany stan repozytorium Git
    - najbardziej czytelnym punktem odniesienia dla użytkownika są tagi wersji

    Po większych zmianach przeznaczonych dla użytkowników warto utworzyć nowy tag, żeby ta wersja template była jednoznacznie wskazywalna.

## Testy repo

Smoke testy repo renderują warianty do katalogów tymczasowych i sprawdzają:

- poprawność struktury po renderze
- `uv run pytest` w wygenerowanym projekcie
- `uv run mypy` w wygenerowanym projekcie

Główna implementacja tych testów jest w [tests/test_template_smoke.py](/Users/fm/Programming/03_Python/02_Projects/tool-template-py/tests/test_template_smoke.py).

## Dokumenty pomocnicze

- [docs/formatting.md](/Users/fm/Programming/03_Python/02_Projects/tool-template-py/docs/formatting.md)
- [docs/hex.md](/Users/fm/Programming/03_Python/02_Projects/tool-template-py/docs/hex.md)
