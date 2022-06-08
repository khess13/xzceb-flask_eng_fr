"""French <> English Translator"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
auth = IAMAuthenticator(apikey)

translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=auth)
translator.set_service_url(url)


def english_to_french(english_text):
    """Translate Enlgish to French"""
    if len(english_text) == 0:
        return None
    text = translator.translate(
        english_text,
        model_id='en-fr'
    ).get_result()
    french_text = text['translations'][0].get('translation')
    return french_text


def french_to_english(french_text):
    """Translate French to English"""
    if len(french_text) == 0:
        return None
    text = translator.translate(
        french_text,
        model_id='fr-en'
    ).get_result()
    english_text = text['translations'][0].get('translation')
    return english_text
