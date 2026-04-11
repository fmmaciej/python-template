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
- `just` for local usage from a cloned repository

## Copier Usage

Generate a project with interactive prompts:

`just copier copy . ../new-project --trust`

Generate a project with default answers:

`just copier copy . ../new-project --trust --defaults`

Without `--defaults`, Copier asks the template questions interactively.

With `--defaults`, Copier uses the default values defined in `copier.yml`. Values passed with `--data` still override those defaults.

`just copier ...` is a short wrapper around `uv run copier ...`.

Direct `uv` usage is also available:

`uv run copier copy . ../new-project --trust`

## Remote Usage

Generate a project directly from a remote Git repository into the current directory:

`uv run copier copy https://github.com/fmmaciej/python-template.git . --trust`

Generate a flat package project with explicit template data:

`uv run copier copy https://github.com/fmmaciej/python-template.git . --trust --defaults --data project=my-app --data python=3.12 --data mode=package --data layout=flat`

Generate a hexagonal package project:

`uv run copier copy https://github.com/fmmaciej/python-template.git . --trust --defaults --data project=my-app --data python=3.12 --data mode=package --data layout=hexagonal`

Generate a script project:

`uv run copier copy https://github.com/fmmaciej/python-template.git . --trust --defaults --data project=my-app --data python=3.12 --data mode=no-package`

Available template parameters:

| Parameter        | Description                            | Values                    |
| ---------------- | -------------------------------------- | ------------------------- |
| `project`        | Project name and package/script name   | e.g. `my-app`             |
| `python`         | Target Python version                  | `3.11`, `3.12`, `3.13`    |
| `mode`           | Project type                           | `no-package`, `package`   |
| `layout`         | Package layout, only for package mode  | `flat`, `hexagonal`       |

Generate from a specific tagged version:

`uv run copier copy https://github.com/fmmaciej/python-template.git . --trust --vcs-ref v1.0.0`

Generate from the current `HEAD` of the remote repository:

`uv run copier copy https://github.com/fmmaciej/python-template.git . --trust --vcs-ref HEAD`

When using a remote Git repository, Copier renders the selected Git reference rather than a local working tree.

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
