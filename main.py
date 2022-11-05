from app import app
from utils.app_loading import load_apps
from main.settings import apps


if __name__ == '__main__':
    msgs = load_apps(apps)
    app.run()
