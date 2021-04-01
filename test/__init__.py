import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from configs import get_settings

setting = get_settings('test')
# database = create_engine(setting.SQLALCHEMY_DATABASE_URI, encoding='utf-8', max_overflow=0)


@pytest.fixture
def app():
    app_config = setting.get_app_setting()
    _app = FastAPI(**app_config)

    yield _app


@pytest.fixture
def client(app):
    try:
        assert True
        # assert app.extra['config']['TESTING'] is True
    except AssertionError:
        # database.close()
        pytest.exit('test config value is wrong, stop test')

    return TestClient(app)
