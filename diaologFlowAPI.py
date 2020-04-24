def send_dialogflow_request(message):
    import os
    import dialogflow_v2 as dialogflow
    from google.api_core.exceptions import InvalidArgument

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'telegrm-bot-exdpjp.json'

    DIALOGFLOW_PROJECT_ID = 'telegrm-bot-exdpjp'
    DIALOGFLOW_LANGUAGE_CODE = 'uk-UA'
    SESSION_ID = 'me'

    text_to_be_analyzed = message

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    return response.query_result.fulfillment_text