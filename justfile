set shell := ["bash", "-cu"]

tmp_dir := "examples"
tmp_source_dir := "/tmp/python-template-working-copy"

script_name := "demo-script"
flat_name := "demo-flat"
hexagonal_name := "demo-hexagonal"

copier_flags := "--trust --defaults --data python=3.12"

default:
    @just --list

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
