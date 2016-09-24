from bottle import static_file, route, get

from settings import Settings

from logit import logit

logit('importing web.py')

settings = Settings()

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=settings.STATIC_DIR)


@get('/')
def get_index():
    return 'Hello'
