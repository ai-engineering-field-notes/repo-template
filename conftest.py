"""Shared test helpers: load a module from a demo's before/ or after/ folder by path."""

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parent


def load_module(path: Path, name: str | None = None):
    path = Path(path)
    name = name or f"_demo_{abs(hash(str(path)))}"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def load():
    return load_module
