from wtforms import Form, StringField, SelectField


class BookSearchForm(Form):
    choices = [('title', 'title'),
               ('link', 'link'),
               ('author', 'author')]
    select = SelectField('Search for book:', choices=choices)
    search = StringField('')
