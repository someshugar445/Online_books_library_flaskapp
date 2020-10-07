from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["DEBUG"] = True
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'asdf'

toolbar = DebugToolbarExtension(app)
books = [
    {'book_id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge'},
    {'book_id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin'},
    {'book_id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany'}
]


@app.route('/', methods=['GET'])
def home():
    books_dict = {'book_id': int,
                  'title': str,
                  'author': str}
    columnNames = books_dict.keys()
    return render_template('home.html', records=books, colnames=columnNames)


@app.route('/books', methods=['GET'])
def api_id(book_id):
    if 'id' in request.args:
        book_id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an book_id."
    # Create an empty list for our results
    results = []
    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['book_id'] == book_id:
            results.append(book)
    return jsonify(results)


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


if __name__ == "__main__":
    app.run(debug=True, port=8080)
