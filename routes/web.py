from bottle import static_file

from logit import logit

logit('importing web.py')


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=settings['STATIC_DIR'])
