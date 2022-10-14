"""Final project using ibm_watson"""
import os
import urllib3
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


urllib3.disable_warnings()
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(
    version = '2021-09-22',
    authenticator = authenticator)
lt.set_service_url(url)
lt.set_disable_ssl_verification(True)


def english_to_french(english_text):
    """
    Translates a text from english to french
    """
    translation = lt.translate(text = english_text, model_id = 'en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Translates a text from french to english
    """
    translation = lt.translate(text = french_text, model_id = 'fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text

def main():
    """
    sample functions
    """
    print(english_to_french('hello'))
    print(french_to_english('bonne nuit'))


if __name__ == '__main__':
    main()
