""" Bottle app for backtrack """

import bottle_sqlalchemy as sqlalchemy
from bottle import TEMPLATE_PATH, install, run

from db_setup import DbSetup
from settings import Settings

settings = Settings()
TEMPLATE_PATH.insert(0, settings.TEMPLATE_FOLDER)

# database
db_setup = DbSetup()
Base = db_setup.base
engine = db_setup.engine
plugin = sqlalchemy.Plugin(engine,
                           Base.metadata,
                           keyword='db',
                           commit=True,
                           create=False,
                           use_kwargs=False)
install(plugin)

# routes are here and use default_app, to be after app and db setup
import routes.web_handlers
import routes.api_handlers

if __name__ == '__main__':
    run(host=settings.HOST, port=settings.PORT, debug=True)
