from translate import Translator


# creating translate object
translator = Translator(to_lang="fr")


def get_api_key(path='private/API KEY.txt'):
    ''''
        Return the api key of NEW API
    '''
    with open(path, 'r') as f:
        key = f.read()
    return key


def text_translate(text):
    '''
        return the translated text in french
    '''
    if not text:
        text = 'None'
    translation = translator.translate(text)
    return translation

    
def sort_article_data(article):
    '''
        Return the New NEWS Article with required fields
    '''
    new_article = dict()
    new_article['title_en'] = article['title']
    new_article['desc_en'] = article['description']
    new_article['title_fr'] = text_translate(article['title'])
    new_article['desc_fr'] = text_translate(article['description'])
    new_article['timestamp'] = article['publishedAt']
    new_article['image_url'] = article['urlToImage']
    return new_article    
    
