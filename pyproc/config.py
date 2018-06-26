"""Web app (Flask) configuration settings."""


from pyproc import settings, utils


class BaseConfig(object):

    """Common configuration."""

    # Server related flags.
    DEBUG = False
    TESTING = False
    SECRET_KEY = utils.get_secret_key()
    SSL_DISABLE = False
    PROPAGATE_EXCEPTIONS = False

    # Celery related configuration.
    _ADDR_DETAILS = utils.get_broker()
    _ADDRESS = "pyamqp://{username}:{password}@{host}".format(**_ADDR_DETAILS)
    CELERY_BROKER_URL = _ADDRESS
    CELERY_RESULT_BACKEND = _ADDRESS


class ProductionConfig(BaseConfig):

    """What is used in production and normal runs."""


class DevelopmentConfig(BaseConfig):

    """Used while doing development & debugging."""

    DEBUG = True


class TestingConfig(BaseConfig):

    """Used when running tests."""

    TESTING = True
    WTF_CSRF_ENABLED = False


DefaultConfig = DevelopmentConfig if settings.DEBUG else ProductionConfig


config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "default": DefaultConfig,
}
