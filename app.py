from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap

import json

bootstrap = Bootstrap()


def create_app():
    my_app = Flask(__name__)
    bootstrap.init_app(my_app)
    return my_app


app = create_app()
# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'asdf'

toolbar = DebugToolbarExtension(app)


@app.route('/')
def index():
    books_dict = {'link': str,
                  'title': str,
                  'author': str}
    with open('books.json') as f:
        books = json.load(f)
    columnNames = books_dict.keys()
    return render_template('home.html', records=books, colnames=columnNames)


@app.route('/', methods=['GET'])
def search_books(title):
    if request.form['submit_button'] == 'search_book':
        with open('books.json') as f:
            books = json.load(f)
        # Create an empty list for our results
        results = []
        for book in books:
            if book['title'] == title:
                results.append(book)
            else:
                "ERROR: Book with given book_id is not found"
        return jsonify(results)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(port=8080, debug=True)
