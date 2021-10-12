from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

from better_profanity import profanity
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError
import library.book_blueprint.services as services
import library.adapters.repository as repo

import library.utilities.utilities as utilities
book_blueprint = Blueprint(
    'book_bp', __name__
)


@book_blueprint.route('/')
def home():
    return render_template(
        'Home.html',
        home_url=utilities.home_page_button(),
        list_all_books_url=utilities.book_button(),

    )


@book_blueprint.route('/list_all_book', methods=['GET'])
def list_all_book():
    books_per_page = 4
    cursor = request.args.get('cursor')
    if cursor is None:
        # No cursor query parameter, so initialise cursor to start at the beginning.
        cursor = 0
    else:
        # Convert cursor from string to int.
        cursor = int(cursor)
    books = repo.repo_instance.display_book()
    list1=[]
    for i in books:
        list1.append(i.book_id)

    books1 = services.get_articles_by_id(list1[cursor:cursor + books_per_page], repo.repo_instance)


    first_book_url = None
    last_book_url = None
    next_book_url = None
    prev_book_url = None

    if cursor > 0:
        # There are preceding articles, so generate URLs for the 'previous' and 'first' navigation buttons.
        prev_book_url = url_for('book_bp.list_all_book', cursor=cursor - books_per_page)
        first_book_url = url_for('book_bp.list_all_book', )

    if cursor + books_per_page < len(books):
        # There are further articles, so generate URLs for the 'next' and 'last' navigation buttons.
        next_book_url = url_for('book_bp.list_all_book', cursor=cursor + books_per_page)

        last_cursor = books_per_page * int(len(books) / books_per_page)
        if len(books) % books_per_page == 0:
            last_cursor -= books_per_page
        last_book_url = url_for('book_bp.list_all_book', cursor=last_cursor)

    return render_template(
        "list_all_books.html",
        books=books1,

        first_book_url=first_book_url,
        last_book_url=last_book_url,
        prev_book_url=prev_book_url,
        next_book_url=next_book_url,


    )



