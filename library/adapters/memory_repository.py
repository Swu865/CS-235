from library.adapters.jsondatareader import BooksJSONReader
from pathlib import Path
from library.domain.model import Book,User
from library.adapters.repository import AbstractRepository


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self.__book = []
        self.__books_index = dict()
        self.__users=[]

    def add_book(self, book: Book):
        self.__books_index[book.book_id]=book
        self.__book.append(book)

    def get_book(self, book_id1):
        return next((book for book in self.__book if book.book_id == book_id1), None)

    def display_book(self):
        return self.__book

    def get_book_by_id(self, id_list):
        existing_ids = [id for id in id_list if id in self.__books_index]
        books = [self.__books_index[id] for id in existing_ids]
        return books

    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, user_name) -> User:
        return next((user for user in self.__users if user.user_name == user_name), None)



def load_books(data_path: Path, repo: MemoryRepository):
    authors_filename = str(Path(data_path) / 'book_authors_excerpt.json')
    books_filename = str(Path(data_path) / 'comic_books_excerpt.json')
    reader = BooksJSONReader(books_filename, authors_filename)
    reader.read_json_files()

    for book in reader.dataset_of_books:
        repo.add_book(book)


def populate(data_path: Path, repo: MemoryRepository):

    load_books(data_path, repo)



