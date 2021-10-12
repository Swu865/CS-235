from flask import Blueprint, request, render_template, redirect, url_for, session

import library.adapters.repository as repo



# Configure Blueprint.
utilities_blueprint = Blueprint(
    'utilities_bp', __name__)


def home_page_button():

    tag_urls = url_for('book_bp.home')


    return tag_urls


def book_button():
    tag_urls = url_for('book_bp.list_all_book')
    return tag_urls

def register_button():
    tag_urls = url_for('authentication_bp.register')

    return tag_urls

def login_button():
    tag_urls = url_for('authentication_bp.login')

    return tag_urls