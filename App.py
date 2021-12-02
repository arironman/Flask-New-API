from flask import Flask, jsonify, request
from newsapi import NewsApiClient
from utils import get_api_key, sort_article_data



app = Flask(__name__)


@app.route("/")
def newApi():
    '''
        Handling the request of index route
    '''

    # fetching the number of article user want.
    article_count = request.args.get('count', default=10, type=int)

    # fetching the news article
    top_headlines = newsapi.get_top_headlines(
        language='en', page_size=article_count)
    
    # creating new dict to store the sorted news
    news = dict()
    news['NEWS Articles'] = list()
    news['NEWS Count'] = article_count

    # iterating through old article and adding article to new dict
    for article in top_headlines['articles']:
        new_article = sort_article_data(article)
        news['NEWS Articles'].append(new_article)

    return jsonify(news)


if __name__ == "__main__":
    # Making Connection with news api by creating its object
    newsapi = NewsApiClient(api_key=get_api_key())
    
    app.run()
