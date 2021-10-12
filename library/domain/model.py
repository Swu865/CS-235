from datetime import datetime
from typing import List

from datetime import datetime


class Author:
    def __init__(self, author_id: int, author_full_name: str):
        if isinstance(author_id, (int)) and isinstance(author_full_name, (str)):
            if author_id < 0 or author_full_name.isspace() or not author_full_name:
                raise ValueError
            else:
                self.__unique_id = author_id
                self.__author_full_name = author_full_name

        else:
            raise ValueError
        self.__coauthor = set()

    @property
    def unique_id(self) -> int:
        return self.__unique_id

    @property
    def full_name(self) -> str:
        return self.__author_full_name

    @unique_id.setter
    def unique_id(self, author_id):
        raise AttributeError

    @full_name.setter
    def full_name(self, author_full_name):
        self.__author_full_name = author_full_name

    def __repr__(self):
        return f'<Author {self.__author_full_name}, author id = {self.__unique_id}>'

    def __eq__(self, other):
        if not isinstance(other, Author):
            return False
        return self.__unique_id == other.__unique_id

    def __lt__(self, other):
        if not isinstance(other, Author):
            return False
        return self.__unique_id < other.__unique_id

    def __hash__(self):
        return hash(self.__unique_id)

    def add_coauthor(self, coauthor):

        self.__coauthor.add(coauthor)

    def check_if_this_author_coauthored_with(self, author):
        if author in self.__coauthor:
            return True
        else:
            return False


class Publisher:
    def __init__(self, publisher_name: str):
        if isinstance(publisher_name, str):
            if publisher_name.isspace() or not publisher_name:
                self.__name = 'N/A'
            else:
                self.__name = publisher_name.strip()
        else:
            self.__name = 'N/A'

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, publisher_name):
        self.__name = publisher_name

    def __repr__(self):
        return f'<Publisher {self.__name}>'

    def __eq__(self, other):
        if not isinstance(other, Publisher):
            return False
        return other.__name == self.__name

    def __lt__(self, other):
        if not isinstance(other, Publisher):
            return False
        return self.__name < other.__name

    def __hash__(self):
        return hash(self.__name)


class Book:
    def __init__(self, book_id: int, book_title: str):


        if isinstance(book_id, int) and isinstance(book_title, str):
            if book_id < 0 or book_title.isspace() or not book_title:
                raise ValueError
            else:
                self.__book_id = book_id
                self.__book_title = book_title.strip()

        else:
            raise ValueError
        self.__book_author = []
        self.__description = ""
        self.__release_year = None
        self.__ebook = None
        self.__publisher = None
        self.__ebook = None
        self.__num_pages = 0
        self.__image_url = ""

    @property
    def book_id(self) -> int:
        return self.__book_id

    @book_id.setter
    def book_id(self, book_id):
        raise AttributeError

    @property
    def image_url(self) -> str:
        return self.__image_url

    @image_url.setter
    def image_url(self,imageurl):
        self.__image_url=imageurl

    @property
    def title(self) -> str:
        return self.__book_title

    @title.setter
    def title(self, book_title):
        if isinstance(book_title, str):
            self.__book_title = book_title.strip()
        else:
            raise ValueError

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, descriptions):
        if isinstance(descriptions, str):
            self.__description = descriptions.strip()
        else:
            raise ValueError

    @property
    def publisher(self) -> Publisher:
        return self.__publisher

    @publisher.setter
    def publisher(self, add_publisher: Publisher):

        if isinstance(add_publisher, Publisher) and self.__publisher is None:
            self.__publisher = add_publisher
        else:
            raise ValueError


    @property
    def authors(self):
        return self.__book_author

    @property
    def release_year(self) -> int:
        return self.__release_year

    @release_year.setter
    def release_year(self, years):
        if years >= 0 and isinstance(years, int):
            self.__release_year = years
        else:
            raise ValueError


    @property
    def ebook(self) -> bool:
        return self.__ebook

    @ebook.setter
    def ebook(self, ebook_bool):
        if isinstance(ebook_bool, bool):
            self.__ebook = ebook_bool
        else:
            raise ValueError

    @property
    def num_pages(self) -> int:

        return self.__num_pages

    @num_pages.setter
    def num_pages(self, pages: int):

        self.__num_pages = pages

    def __repr__(self):
        return f'<Book {self.__book_title}, book id = {self.__book_id}>'

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.__book_id == other.__book_id

    def __lt__(self, other):
        if not isinstance(other, Book):
            return False
        return self.__book_id < other.__book_id

    def __hash__(self):
        return hash(self.__book_id)

    def add_author(self, author: Author):
        self.__book_author.append(author)

    def remove_author(self, author):
        if len(self.__book_author) == 0 or author not in self.__book_author:
            return False
        else:
            self.__book_author.remove(author)


class Review:
    def __init__(self, book: Book, review_text: str, rating: int):
        if not isinstance(book, Book):
            self.__book = None
        else:
            self.__book = book

        if not isinstance(review_text, str):
            self.__review_text = "N/A"
        else:
            self.__review_text = review_text.strip()

        if not isinstance(rating, int) or rating < 1 or rating > 5:
            raise ValueError
        else:
            self.__rating = rating

        self.__timestamp = datetime.now()

    @property
    def book(self) -> Book:
        return self.__book

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp



    def __eq__(self, other):
        if not isinstance(other, Review):
            return False
        elif self.__book == other.__book and self.__review_text == other.__review_text and self.__rating == other.__rating:
            return True
        else:
            return False


class User:
    def __init__(self, user_name: str, password: str):
        if not isinstance(user_name, str):
            self.__user_name = None
        else:
            self.__user_name = user_name.lower().strip()

        if not isinstance(password, str) or len(password) < 7:
            self.__password = None
        else:
            self.__password = password

        self.__read_books = []
        self.__reviews = []
        self.__pages_read = 0

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def read_books(self) -> list:
        return self.__read_books

    @property
    def reviews(self) -> list:
        return self.__reviews

    @property
    def pages_read(self) -> int:
        return self.__pages_read

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return other.__user_name == self.__user_name

    def __lt__(self, other):
        if not isinstance(other, User):
            return False
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)

    def read_a_book(self, book: Book):
        self.__read_books.append(book)
        self.__pages_read += book.num_pages

    def add_review(self, review: Review):
        self.__reviews.append(review)


class BooksInventory:

    def __init__(self):
        self.__books = {}
        self.__prices = {}
        self.__stock_count = {}

    def add_book(self, book: Book, price: int, nr_books_in_stock: int):
        self.__books[book.book_id] = book
        self.__prices[book.book_id] = price
        self.__stock_count[book.book_id] = nr_books_in_stock

    def remove_book(self, book_id: int):
        self.__books.pop(book_id)
        self.__prices.pop(book_id)
        self.__stock_count.pop(book_id)

    def find_book(self, book_id: int):
        if book_id in self.__books.keys():
            return self.__books[book_id]
        return None

    def find_price(self, book_id: int):
        if book_id in self.__books.keys():
            return self.__prices[book_id]
        return None

    def find_stock_count(self, book_id: int):
        if book_id in self.__books.keys():
            return self.__stock_count[book_id]
        return None

    def search_book_by_title(self, book_title: str):
        for book_id in self.__books.keys():
            if self.__books[book_id].title == book_title:
                return self.__books[book_id]
        return None

class BooksInventory:
    def __init__(self):
        self.__book = {}
        self.__price = {}
        self.__stock = {}
        self.__book_title= {}

    def add_book(self,book:Book, price: int,nr_books_in_stock:int):

        self.__book[book.book_id] = book
        self.__price[book.book_id]= price
        self.__stock[book.book_id] = nr_books_in_stock
        self.__book_title[book.title]= book

    def remove_book(self,book_id:int):
        del self.__book[book_id]
        del self.__price[book_id]
        del self.__stock[book_id]

    def find_book(self,book_id):
        if book_id not in self.__book:
            return None
        else:
            return self.__book[book_id]

    def find_price(self, book_id):
        if book_id not in self.__book:
            return None
        else:
            return self.__price[book_id]

    def find_stock_count(self, book_id):
        if book_id not in self.__book:
            return None
        else:
            return self.__stock[book_id]

    def search_book_by_title(self, title):
        if title not in self.__book_title:
            return None
        else:
            return self.__book_title[title]
