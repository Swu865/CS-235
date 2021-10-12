from typing import List, Iterable

from library.adapters.repository import AbstractRepository
from library.domain.model import Book


class NonExistentArticleException(Exception):
    pass


class UnknownUserException(Exception):
    pass


def get_articles_by_id(id_list, repo: AbstractRepository):
    articles = repo.get_book_by_id(id_list)

    # Convert Articles to dictionary form.
    articles_as_dict = articles_to_dict(articles)

    return articles_as_dict


def article_to_dict(book: Book):
    article_dict = {
        'id': book.book_id,
        'title': book.title,
        'description': book.description,
        'publisher': book.publisher,
        'authors': book.authors,
        'release_year': book.release_year,
        'ebook': book.ebook,
        'image_url': book.image_url,
    }
    return article_dict


def articles_to_dict(book: Iterable[Book]):
    return [article_to_dict(b) for b in book]
