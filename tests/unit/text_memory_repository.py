from typing import List
import pytest

from library.domain.model import Publisher, Author, Book, Review, User, BooksInventory
from library.adapters.repository import RepositoryException


def test_repository_can_add_book(in_memory_repo):
    Book1 = Book(123456, "Dog")
    in_memory_repo.add_book(Book1)

    assert in_memory_repo.get_book(123456) is Book1






