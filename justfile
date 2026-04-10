set shell := ["bash", "-cu"]

tmp_dir := "examples"

script_name := "demo-script"
flat_name := "demo-flat"
hexagonal_name := "demo-hexagonal"

copier_base := "uv run copier copy ."
copier_flags := "--trust --defaults --data python_version=3.12"

default:
    @just --list

install:
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

render-flat:
    rm -rf {{ tmp_dir }}/{{ flat_name }}
    {{ copier_base }} {{ tmp_dir }}/{{ flat_name }} {{ copier_flags }} --data project_slug={{ flat_name }} --data package_mode=package --data package_layout=flat

render-hex:
    rm -rf {{ tmp_dir }}/{{ hexagonal_name }}
    {{ copier_base }} {{ tmp_dir }}/{{ hexagonal_name }} {{ copier_flags }} --data project_slug={{ hexagonal_name }} --data package_mode=package --data package_layout=hexagonal

render-script:
    rm -rf {{ tmp_dir }}/{{ script_name }}
    {{ copier_base }} {{ tmp_dir }}/{{ script_name }} {{ copier_flags }} --data project_slug={{ script_name }} --data package_mode=no-package

smoke: render-flat render-hex render-script

clean:
    rm -rf {{ tmp_dir }}/{{ flat_name }} {{ tmp_dir }}/{{ hexagonal_name }} {{ tmp_dir }}/{{ script_name }}
