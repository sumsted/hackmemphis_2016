from bottle import HTTPError, request

from schema import Debug
from settings import Settings

settings = Settings()

UNKNOWN_INTENT_RESPONSE = {}

UNKNOWN_USER_RESPONSE = {}

SERVICE_TIMEOUT_RESPONSE = {}

BAD_REQUEST_RESPONSE = {}


def authorized(handler):
    def decorator(db):
        r = handler
        try:
            in_token = request.forms.get('token')
        except Exception as e:
            debug = Debug('authorized', 'exception: ' + str(e))
            db.add(debug)
            in_token = None
        if in_token is not None and in_token == settings.TOKEN:
            # todo: check team id
            return r(db)
        else:
            debug = Debug('authorized', 'denied: ' + in_token if in_token is not None else 'None')
            db.add(debug)
            return HTTPError(403, 'denied')

    return decorator


# def ga_post_event(action=None, label=None, value=None):
#     try:
#         event = {
#             'v': settings.GA_VERSION,
#             'tid': settings.GA_TRACKING_CODE,
#             'cid': int(settings.GA_CID),
#             't': settings.GA_HIT_TYPE,
#             'ec': settings.GA_CATEGORY,
#             'ea': action if action is not None else settings.GA_ACTION,
#             'el': label if label is not None else settings.GA_LABEL,
#             'ev': value if value is not None else settings.GA_VALUE
#         }
#         result = requests.post(settings.GA_URL, data=event)
#     except:
#         result = None
#     return result