set shell := ["bash", "-cu"]

tmp_dir := "examples"
flat_dir := "python-template-flat"
hexagonal_dir := "python-template-hexagonal"
no_package_dir := "python-template-no-package"
copier_base := "uv run copier copy ."
copier_flags := "--trust --defaults -r HEAD --data python_version=3.12"

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

precommit-install:
    uv run pre-commit install

render-flat:
    rm -rf {{ tmp_dir }}/{{ flat_dir }}
    {{ copier_base }} {{ tmp_dir }}/{{ flat_dir }} {{ copier_flags }} --data project_slug=demo-flat --data package_mode=package --data package_layout=flat

render-hex:
    rm -rf {{ tmp_dir }}/{{ hexagonal_dir }}
    {{ copier_base }} {{ tmp_dir }}/{{ hexagonal_dir }} {{ copier_flags }} --data project_slug=demo-hexagonal --data package_mode=package --data package_layout=hexagonal

render-no-package:
    rm -rf {{ tmp_dir }}/{{ no_package_dir }}
    {{ copier_base }} {{ tmp_dir }}/{{ no_package_dir }} {{ copier_flags }} --data project_slug=demo-script --data package_mode=no-package

smoke: render-flat render-hex render-no-package

clean:
    rm -rf {{ tmp_dir }}/{{ flat_dir }} {{ tmp_dir }}/{{ hexagonal_dir }} {{ tmp_dir }}/{{ no_package_dir }}
