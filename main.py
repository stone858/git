"""Minimal Python project entry point."""

import argparse


def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


def main() -> None:
    parser = argparse.ArgumentParser(description="A minimal Python starter project.")
    parser.add_argument("--name", default="world", help="Name to greet.")
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
