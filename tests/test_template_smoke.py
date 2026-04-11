from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COPYTREE_IGNORE = shutil.ignore_patterns(
    ".git",
    ".venv",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "__pycache__",
    "examples",
)


def render(target: Path, *, project: str, mode: str, layout: str | None = None) -> None:
    if target.exists():
        shutil.rmtree(target)

    source = target.parent / "template-source"
    if source.exists():
        shutil.rmtree(source)
    shutil.copytree(ROOT, source, ignore=COPYTREE_IGNORE)

    cmd = [
        "uv",
        "run",
        "copier",
        "copy",
        str(source),
        str(target),
        "--trust",
        "--defaults",
        "--data",
        f"project={project}",
        "--data",
        "python=3.12",
        "--data",
        f"mode={mode}",
    ]

    if layout is not None:
        cmd.extend(["--data", f"layout={layout}"])

    subprocess.run(cmd, check=True)


def run_generated_check(target: Path, *args: str) -> None:
    subprocess.run(["uv", "run", *args], cwd=target, check=True)


def test_render_no_package(tmp_path: Path) -> None:
    target = tmp_path / "demo-script"
    render(target, project="demo-script", mode="no-package")

    assert (target / "main.py").exists()
    assert (target / "tests" / "test_smoke.py").exists()
    assert not (target / "variants").exists()
    assert not (target / "common").exists()

    run_generated_check(target, "pytest")
    run_generated_check(target, "mypy", "main.py", "tests", "--config-file=pyproject.toml")


def test_render_package_flat(tmp_path: Path) -> None:
    target = tmp_path / "demo-flat"
    render(target, project="demo-flat", mode="package", layout="flat")

    assert (target / "src" / "demo_flat" / "main.py").exists()
    assert (target / "tests" / "test_smoke.py").exists()
    assert not (target / "variants").exists()
    assert not (target / "common").exists()

    run_generated_check(target, "pytest")
    run_generated_check(target, "mypy", "src", "tests", "--config-file=pyproject.toml")


def test_render_package_hexagonal(tmp_path: Path) -> None:
    target = tmp_path / "demo-hex"
    render(target, project="demo-hex", mode="package", layout="hexagonal")

    assert (target / "src" / "demo_hex" / "__main__.py").exists()
    assert (target / "src" / "demo_hex" / "main.py").exists()
    assert (target / "src" / "demo_hex" / "app.py").exists()
    assert (target / "src" / "demo_hex" / "config" / "settings.py").exists()
    assert (target / "src" / "demo_hex" / "application" / "use_cases" / "say_hello.py").exists()
    assert (target / "src" / "demo_hex" / "application" / "dto" / "say_hello_command.py").exists()
    assert (target / "src" / "demo_hex" / "domain" / "value_objects" / "user_name.py").exists()
    assert (
        target
        / "src"
        / "demo_hex"
        / "adapters"
        / "repositories"
        / "default_greeting_template_repository.py"
    ).exists()
    assert (target / "src" / "demo_hex" / "cli" / "commands.py").exists()
    assert (target / "docs" / "architecture.md").exists()
    assert (target / "tests" / "test_smoke.py").exists()
    assert not (target / "variants").exists()
    assert not (target / "common").exists()

    run_generated_check(target, "pytest")
    run_generated_check(target, "mypy", "src", "tests", "--config-file=pyproject.toml")
