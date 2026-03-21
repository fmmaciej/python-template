from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render(
    target: Path, *, project_slug: str, package_mode: str, package_layout: str | None = None
) -> None:
    if target.exists():
        shutil.rmtree(target)

    cmd = [
        "uv",
        "run",
        "copier",
        "copy",
        str(ROOT),
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


def test_render_no_package(tmp_path: Path) -> None:
    target = tmp_path / "demo-script"
    render(target, project_slug="demo-script", package_mode="no-package")

    assert (target / "main.py").exists()
    assert not (target / "variants").exists()
    assert not (target / "common").exists()


def test_render_package_flat(tmp_path: Path) -> None:
    target = tmp_path / "demo-flat"
    render(target, project_slug="demo-flat", package_mode="package", package_layout="flat")

    assert (target / "src" / "demo_flat" / "__main__.py").exists()
    assert not (target / "variants").exists()
    assert not (target / "common").exists()


def test_render_package_hexagonal(tmp_path: Path) -> None:
    target = tmp_path / "demo-hex"
    render(target, project_slug="demo-hex", package_mode="package", package_layout="hexagonal")

    assert (target / "src" / "demo_hex" / "bootstrap.py").exists()
    assert not (target / "variants").exists()
    assert not (target / "common").exists()
