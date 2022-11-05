from typing import List
from importlib import import_module


def load_apps(apps: List[str]):
    for app in apps:
        import_module(app + '.routes')
