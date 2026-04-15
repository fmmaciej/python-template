set shell := ["bash", "-cu"]

tmp_dir := "examples"
tmp_source_dir := "/tmp/python-template-working-copy"

script_name := "demo-script"
flat_name := "demo-flat"
hexagonal_name := "demo-hexagonal"

copier_flags := "--trust --defaults --data python=3.12"

default:
    @just --list

help:
    @printf '%s\n' \
        'python-template' \
        '' \
        'This repository is a Copier template. Use it to generate a new Python project; it is not the generated app itself.' \
        '' \
        'Start here:' \
        '  just copier copy . ../my-app --trust' \
        '    Runs Copier interactively. It asks for the project name, Python version, and project shape.' \
        '' \
        'Choose a project shape during generation:' \
        '  no-package' \
        '    Choose mode=no-package.' \
        '    Result: one main.py file, argparse CLI, no installable package.' \
        '' \
        '  package + flat' \
        '    Choose mode=package and layout=flat.' \
        '    Result: installable CLI package with src/ layout, Typer command, minimal structure.' \
        '' \
        '  package + hexagonal' \
        '    Choose mode=package and layout=hexagonal.' \
        '    Result: installable CLI package with separate CLI, application, domain, and adapter layers.' \
        '' \
        'Generate a specific shape without prompts:' \
        '  just copier copy . ../my-script --trust --defaults --data project=my-script --data mode=no-package' \
        '  just copier copy . ../my-flat --trust --defaults --data project=my-flat --data mode=package --data layout=flat' \
        '  just copier copy . ../my-hex --trust --defaults --data project=my-hex --data mode=package --data layout=hexagonal'

dev-help:
    @printf '%s\n' \
        'python-template developer help' \
        '' \
        'Work on this template repository:' \
        '  just sync             # install/update dependencies' \
        '  just check            # format, lint, type-check, and test' \
        '  just clean            # remove generated examples and temporary template copy' \
        '' \
        'Generate example projects from this working tree:' \
        '  just render-script    # writes examples/demo-script' \
        '  just render-flat      # writes examples/demo-flat' \
        '  just render-hex       # writes examples/demo-hexagonal' \
        '  just smoke            # renders all three examples' \
        '' \
        'List every just recipe:' \
        '  just --list'

copier +args:
    uv run copier {{args}}

sync:
    uv sync

format:
    uv run ruff format scripts tests

ruff:
    uv run ruff check scripts tests

ruff-fix:
    uv run ruff check scripts tests --fix

mypy:
    uv run mypy

test:
    uv run pytest

check: format ruff mypy test

sync-template-source:
    rm -rf {{ tmp_source_dir }}
    rsync -a ./ {{ tmp_source_dir }}/ --exclude .git --exclude .venv --exclude .mypy_cache --exclude .pytest_cache --exclude .ruff_cache --exclude __pycache__ --exclude examples

render-flat: sync-template-source
    rm -rf {{ tmp_dir }}/{{ flat_name }}
    uv run copier copy {{ tmp_source_dir }} {{ tmp_dir }}/{{ flat_name }} {{ copier_flags }} --data project={{ flat_name }} --data mode=package --data layout=flat

render-hex: sync-template-source
    rm -rf {{ tmp_dir }}/{{ hexagonal_name }}
    uv run copier copy {{ tmp_source_dir }} {{ tmp_dir }}/{{ hexagonal_name }} {{ copier_flags }} --data project={{ hexagonal_name }} --data mode=package --data layout=hexagonal

render-script: sync-template-source
    rm -rf {{ tmp_dir }}/{{ script_name }}
    uv run copier copy {{ tmp_source_dir }} {{ tmp_dir }}/{{ script_name }} {{ copier_flags }} --data project={{ script_name }} --data mode=no-package

smoke: render-flat render-hex render-script

clean:
    rm -rf {{ tmp_dir }}/{{ flat_name }} {{ tmp_dir }}/{{ hexagonal_name }} {{ tmp_dir }}/{{ script_name }}
    rm -rf {{ tmp_source_dir }}
