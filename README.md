# python-template

A Python project template based on Copier.

It generates a new repository with a ready-to-use toolchain and a selected project structure:

| Mode        | Description                                                    |
| ----------- | -------------------------------------------------------------- |
| `script`    | Simple script project with a single entry file                 |
| `flat`      | Simple CLI package project with a flat structure               |
| `hexagonal` | CLI package project with a lightweight hexagonal structure     |

Each generated project includes a minimal starter setup:

- `ruff`, `mypy`, `pytest`, `pre-commit`, and `just` configuration
- a sample entrypoint for the selected variant
- a `tests/` directory with a simple smoke test so `pytest` and `mypy` work immediately after generation

## Requirements

- Python 3.12+
- `uv`

## Copier Usage

Generate a project with interactive prompts:

`uv run copier copy . ../new-project --trust`

Generate a project with default answers:

`uv run copier copy . ../new-project --trust --defaults`

## After Generation

- `uv sync`
- `just check`
- `uv run pre-commit install`

## For Template Maintainers

Maintenance notes for this repository are available in:

- [docs/development.md](/Users/fm/Programming/03_Python/02_Projects/python-template/docs/development.md)
- [docs/formatting.md](/Users/fm/Programming/03_Python/02_Projects/python-template/docs/formatting.md)
- [docs/hex.md](/Users/fm/Programming/03_Python/02_Projects/python-template/docs/hex.md)

## Repository Structure

| File / directory         | Description                              |
| ------------------------ | ---------------------------------------- |
| `copier.yml`             | Copier questions and configuration       |
| `docs/`                  | additional repository documentation      |
| `template/common/`       | files shared by all variants             |
| `template/variants/`     | files specific to each variant           |
| `tests/`                 | template tests                           |
| `scripts/`               | helper scripts for repository work       |
| `scripts/post_render.py` | final project composition after render   |
