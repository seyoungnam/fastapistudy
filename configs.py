from functools import lru_cache

from pydantic import BaseSettings


class Config(BaseSettings):
    """
    소문자 : fast api 기본 설정
    대문자 : 커스텀 설정
    """
    title = "기본 템플릿"
    description = "기본 템플릿 마이그레이션 프로젝트"
    version = "0.0.5"
    openapi_tags = [
        {
            "name": "public",
            "description": "**공개** API 들, **인증**이 필요없다.",
            "externalDocs": {
                "description": "External docs",
                "url": "https://fastapi.tiangolo.com/",
            },
        },
    ]
    TESTING = False
    JWT_SECRET_KEY = 'dad324k32j5lk34j6l34k6jl34k5jl345j34lk5j3l4k5j34lk5j34kl5'

    @classmethod
    def get_app_setting(cls):
        result = {}

        for key in dir(cls):
            if key.startswith('_') or key.isupper():
                continue
            else:
                result[key] = getattr(cls, key)

        return result


class DevelopmentConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URL = f''


class TestingConfig(Config):
    debug = False
    TESTING = True
    SQLALCHEMY_DATABASE_URL = f''


class ProductionConfig(Config):
    debug = False


@lru_cache()
def get_settings(config_name='dev'):
    if config_name == 'dev':
        return DevelopmentConfig()
    elif config_name == 'test':
        return TestingConfig()
    elif config_name == 'prod':
        return ProductionConfig()


config = get_settings()
app_config = config.get_app_setting()
