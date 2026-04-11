# Hex Variant

Dokument dotyczy wariantu `package + hexagonal` w repozytorium template.

## Cel

Ten wariant pokazuje lekki układ hexagonalny dla aplikacji CLI:

- `main.py` jako cienki entrypoint
- `app.py` jako composition root
- `cli/` jako warstwa wejścia
- `application/` jako use case'y, DTO i porty
- `domain/` jako model domenowy
- `adapters/` jako implementacje techniczne

## Zakres

Wariant nie próbuje pokryć wszystkich możliwych elementów architektury heksagonalnej. Ma pokazać minimalny, czytelny szkielet projektu startowego.

W szczególności:

- `domain/services/` nie jest generowane domyślnie
- `adapters/clients/` jest miejscem na klientów do zewnętrznych usług, ale może pozostać puste
- przykład domenowy jest celowo mały i służy głównie pokazaniu przepływu przez warstwy

## Przepływ

1. CLI zbiera input w `cli/commands.py`
2. Use case działa w `application/use_cases/`
3. Port jest definiowany w `application/ports/`
4. Adapter implementuje port w `adapters/repositories/`
5. `app.py` składa zależności i zwraca gotową aplikację
