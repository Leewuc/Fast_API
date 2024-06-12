from functools import lru_cache
from typing import Dict, Type

from backend_practice_1.app.core.settings.app import AppSettings
from backend_practice_1.app.core.settings.base import AppEnvTypes, BaseAppSettings
from backend_practice_1.app.core.settings.local import LocalAppSettings
from backend_practice_1.app.core.settings.dev import DevAppSettings
from backend_practice_1.app.core.settings.prod import ProdAppSettings
from backend_practice_1.app.core.settings.test import TestAppSettings


environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings,
    AppEnvTypes.prod: ProdAppSettings,
    AppEnvTypes.local: LocalAppSettings,
    AppEnvTypes.test: TestAppSettings
}


@lru_cache
def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    return config()
