from flask import Flask
from flask import request, jsonify

app=Flask(__name__)

app.config["DEBUG"]=True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'DARSHAN SAWANT',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'ARNAV SAWANT',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/', methods=["GET"])
def home():
    return "<center><h1>Distance reading archive</h1><p><u>This site is a prototype API for distant reading of science fiction novels.</uh></p></center>"

@app.route('/api/v1/resources/books/all', methods=["GET"])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results=[]

    for book in books:
        if book['id']== id:
            results.append(book)

    return jsonify(results)
app.run()