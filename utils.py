from googletrans import Translator


# making connection with google translate api by creating its object
translator = Translator()


def get_api_key(path='private/API KEY.txt'):
    ''''
        Return the api key of NEW API
    '''
    with open(path, 'r') as f:
        key = f.read()
    return key


def text_translate(text, from_lang='en', to_lang='french'):
    '''
        This Function return the translated text
    '''
    if not text:
        text = 'None'
    translated_text = translator.translate(text, src=from_lang, dest=to_lang)
    return translated_text.text

    
def sort_article_data(article):
    '''
        This function return the required data, by creating the new article dict
    '''
    new_article = dict()
    new_article['title_en'] = article['title']
    new_article['desc_en'] = article['description']
    new_article['title_fr'] = text_translate(article['title'])
    new_article['desc_fr'] = text_translate(article['description'])
    new_article['timestamp'] = article['publishedAt']
    new_article['image_url'] = article['urlToImage']
    return new_article    
    
