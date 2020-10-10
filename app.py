from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, url_for
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from forms import BookSearchForm
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


@app.route('/', methods=['POST'])
def search_books():
    if request.form['submit_button'] == 'Search book':
        title = request.form['book']
        books_dict = {'link': str,
                      'title': str,
                      'author': str}
        with open('books.json') as f:
            books = json.load(f)
        columnNames = books_dict.keys()
        results = []
        book_found = False
        for book in books:
            if title in book['title']:
                results.append(book)
                book_found = True
        if book_found:
            return render_template('home.html', records=results, colnames=columnNames)
        else:
            flash("ERROR: Oops Book not found!!")
            return render_template('home.html', records=books, colnames=columnNames)


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = BookSearchForm()
    print(form.search.data)
    if request.method == 'POST':
        return redirect((url_for('search', query=form.search.data)))
    return render_template('home.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(port=8080, debug=True)
