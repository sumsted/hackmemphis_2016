"""Create singleton for sqlalchemy base and engine"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from settings import Settings

settings = Settings()


class DbSetup:
    class __DbSetup:
        def __init__(self, connection_string):
            self.base = declarative_base()
            self.engine = create_engine(connection_string)

    instance = None

    def __init__(self):
        if DbSetup.instance is None:
            print('creating DbSetup instance')
            settings.DB_PASSWORD = settings.get('DB_PASSWORD', '')
            connection_string = 'postgresql://%(DB_USER)s:%(DB_PASSWORD)s@localhost:5432/%(DB_NAME)s' % settings.get_dict()
            DbSetup.instance = DbSetup.__DbSetup(connection_string)
        else:
            print('reusing DbSetup instance')

    def __getattr__(self, item):
        try:
            print('use existing instance attribute: %s' % repr(self.instance))
            return getattr(self.instance, item)
        except Exception as e:
            print('cannot access existing attribute on inner object: %s' % str(e))
