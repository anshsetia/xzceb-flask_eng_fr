"""this module translates text from english to french and french to english"""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('0Dou0QH5s6_gPG69o2WRxpVPgFz9XopLbNmC3rGSPgvr')
language_translator = LanguageTranslatorV3(
     version='2022-12-17',
    authenticator=authenticator
)

language_translator.set_service_url(
'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/0ee9f48e-2561-4390-8913-4fe90b268b65')

englishText = 'This is python programming'
frenchText = 'Il s agit d une programmation Python'

def englishtofrench(englishtext):
    frenchtext = language_translator.translate(text=englishtext,model_id='en-fr').get_result()
    return frenchtext.get("translations")[0].get("translation")

def frenchtoenglish(frenchtext):
    """this function translates french to english"""
    englishtext = language_translator.translate(text=frenchtext,model_id='fr-en').get_result()
    return englishtext.get("translations")[0].get("translation")

translatedText = englishtofrench(englishText)
translatedText2 = frenchtoenglish(frenchText)
