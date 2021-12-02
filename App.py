from flask import Flask, jsonify, request
from newsapi import NewsApiClient
from utils import get_api_key

app = Flask(__name__)

# Making Connection with new api
newsapi = NewsApiClient(api_key=get_api_key())


@app.route("/")
def newApi():
    '''
        Handling the request of index route
    '''

    # fetching the number of article user want.
    article_count = request.args.get('count', default=10, type=int)

    top_headlines = newsapi.get_top_headlines(language='en', page_size=article_count)
    top_headlines['totalResults'] = article_count
    
    return jsonify(top_headlines)

if __name__ == "__main__":
    app.run()
