from janeiro_config.exceptions import ConfigurationError


_APP_NAME: str = None
_APP_VERSION: str = None

def set_app_name(app_name: str):
    global _APP_NAME
    _APP_NAME = app_name

def get_app_name():
    if _APP_NAME is None:
        raise ConfigurationError("Application name has not been initialized")
    return _APP_NAME

def set_app_version(app_version: str):
    global _APP_VERSION
    app_version = app_version

def get_app_version():
    if _APP_VERSION is None:
        raise ConfigurationError("Application version has not been initialized")
    return _APP_VERSION
