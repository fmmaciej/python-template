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


def render(
    target: Path, *, project_slug: str, package_mode: str, package_layout: str | None = None
) -> None:
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
        f"project_slug={project_slug}",
        "--data",
        "python_version=3.12",
        "--data",
        f"package_mode={package_mode}",
    ]

    if package_layout is not None:
        cmd.extend(["--data", f"package_layout={package_layout}"])

    subprocess.run(cmd, check=True)


def run_generated_check(target: Path, *args: str) -> None:
    subprocess.run(["uv", "run", *args], cwd=target, check=True)


def test_render_no_package(tmp_path: Path) -> None:
    target = tmp_path / "demo-script"
    render(target, project_slug="demo-script", package_mode="no-package")

    assert (target / "main.py").exists()
    assert (target / "tests" / "test_smoke.py").exists()
    assert not (target / "variants").exists()
    assert not (target / "common").exists()

    run_generated_check(target, "pytest")
    run_generated_check(target, "mypy", "main.py", "tests", "--config-file=pyproject.toml")


def test_render_package_flat(tmp_path: Path) -> None:
    target = tmp_path / "demo-flat"
    render(target, project_slug="demo-flat", package_mode="package", package_layout="flat")

    assert (target / "src" / "demo_flat" / "main.py").exists()
    assert (target / "tests" / "test_smoke.py").exists()
    assert not (target / "variants").exists()
    assert not (target / "common").exists()

    run_generated_check(target, "pytest")
    run_generated_check(target, "mypy", "src", "tests", "--config-file=pyproject.toml")


def test_render_package_hexagonal(tmp_path: Path) -> None:
    target = tmp_path / "demo-hex"
    render(target, project_slug="demo-hex", package_mode="package", package_layout="hexagonal")

    assert (target / "src" / "demo_hex" / "main.py").exists()
    assert (target / "src" / "demo_hex" / "app.py").exists()
    assert (target / "tests" / "test_smoke.py").exists()
    assert not (target / "variants").exists()
    assert not (target / "common").exists()

    run_generated_check(target, "pytest")
    run_generated_check(target, "mypy", "src", "tests", "--config-file=pyproject.toml")
