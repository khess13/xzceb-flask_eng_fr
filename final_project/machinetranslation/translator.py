import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
auth = IAMAuthenticator(apikey)

translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=auth)
translator.set_service_url(url)


def englishToFrench(englishText):
    if len(englishText) == 0:
        return None
    text = translator.translate(
        englishText,
        model_id='en-fr'
    ).get_result()
    frenchText = text['translations'][0].get('translation')
    return frenchText


def frenchToEnglish(frenchText):
    if len(frenchText) == 0:
        return None
    text = translator.translate(
        frenchText,
        model_id='fr-en'
    ).get_result()
    englishText = text['translations'][0].get('translation')
    return englishText
