def get_access_token(alexa_session):
    try:
        return alexa_session['user']['accessToken']
    except:
        return ''


def get_slot(intent, key, default=None):
    try:
        return intent['slots'][key]['value']
    except:
        return default


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


def handle_help_intent():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome to Memphis"
    speech_output = " Welcome to Memphis. Land of the chicken strip. Home of the Tigers."

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Hey are you there? Memphis waits for no one."

    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for visiting Memphis. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def handle_attack_intent(intent, session):
    title = "Memphis - ATTACK!"
    should_end_session = False
    session_attributes = {}
    speech_output = "I'm attacking."
    reprompt_text = None
    try:
        pass
    except:
        pass
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def handle_navigate_intent(intent, session):
    title = "Memphis - RUN!"
    should_end_session = False
    session_attributes = {}
    speech_output = "I'm running."
    reprompt_text = None
    try:
        pass
    except:
        pass
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def handle_look_intent(intent, session):
    title = "Memphis - LOOKING!"
    should_end_session = False
    session_attributes = {}
    speech_output = "I'm looking around."
    reprompt_text = None
    try:
        pass
    except:
        pass
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def handle_take_intent(intent, session):
    title = "Memphis - TAKING!"
    should_end_session = False
    session_attributes = {}
    speech_output = "I'm taking stuff."
    reprompt_text = None
    try:
        pass
    except:
        pass
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def handle_health_intent(intent, session):
    title = "Memphis - HEALTH!"
    should_end_session = False
    session_attributes = {}
    speech_output = "I'm healthy."
    reprompt_text = None
    try:
        pass
    except:
        pass
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))


def handle_restart_intent(intent, session):
    title = "Memphis - RESTART!"
    should_end_session = False
    session_attributes = {}
    speech_output = "I'm restarting."
    reprompt_text = None
    try:
        pass
    except:
        pass
    return build_response(session_attributes, build_speechlet_response(
        title, speech_output, reprompt_text, should_end_session))
