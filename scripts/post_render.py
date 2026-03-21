from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def copy_contents(src: Path, dst: Path) -> None:
    if not src.exists():
        raise FileNotFoundError(f"Source directory does not exist: {src}")

    for item in src.iterdir():
        target = dst / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)


def remove_if_exists(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def resolve_variant(root: Path, package_mode: str, package_layout: str | None) -> Path:
    variants_root = root / "variants"

    if package_mode == "no-package":
        return variants_root / "no-package"

    if package_mode == "package" and package_layout == "flat":
        return variants_root / "package" / "flat"

    if package_mode == "package" and package_layout == "hexagonal":
        return variants_root / "package" / "hexagonal"

    raise RuntimeError(
        f"Unsupported variant selection: package_mode={package_mode!r}, "
        f"package_layout={package_layout!r}"
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compose final project structure from Copier-rendered common/ and variants/."
    )
    parser.add_argument(
        "--project-root",
        default=".",
        help="Path to rendered project root (default: current working directory).",
    )
    parser.add_argument(
        "--package-mode",
        required=True,
        choices=["no-package", "package"],
        help="Selected package mode.",
    )
    parser.add_argument(
        "--package-layout",
        choices=["flat", "hexagonal"],
        default=None,
        help="Selected package layout for package mode.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    common_dir = root / "common"
    variant_dir = resolve_variant(
        root=root,
        package_mode=args.package_mode,
        package_layout=args.package_layout,
    )

    copy_contents(common_dir, root)
    copy_contents(variant_dir, root)

    remove_if_exists(common_dir)
    remove_if_exists(root / "variants")

    print(f"Selected variant: {variant_dir.relative_to(root)}")


if __name__ == "__main__":
    main()
