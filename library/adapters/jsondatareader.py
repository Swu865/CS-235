import json


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

    @property
    def book_id(self) -> int:
        return self.__book_id

    @book_id.setter
    def book_id(self, book_id):
        raise AttributeError

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
        if not isinstance(years, int):
            return None
        self.__release_year = years

    @property
    def ebook(self) -> bool:
        return self.__ebook

    @ebook.setter
    def ebook(self, ebook_bool):
        if isinstance(ebook_bool, bool):
            self.__ebook = ebook_bool
        else:
            raise ValueError

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


class BooksJSONReader:

    def __init__(self, books_file_name: str, authors_file_name: str):
        self.__books_file_name = books_file_name
        self.__authors_file_name = authors_file_name
        self.__dataset_of_books = []

    @property
    def dataset_of_books(self):
        return self.__dataset_of_books

    def read_json_files(self):
        authors = [json.loads(line) for line in open(self.__authors_file_name, 'r')]
        books = [json.loads(line) for line in open(self.__books_file_name, 'r')]

        for i in range(len(books)):
            self.__dataset_of_books.append(Book(int(books[i]["book_id"]), str(books[i]["title"])))

        for i in range(len(self.__dataset_of_books)):
            self.__dataset_of_books[i].publisher = Publisher(books[i]["publisher"])
            self.__dataset_of_books[i].description = str(books[i]["description"])

            self.__dataset_of_books[i].ebook = bool(books[i]["description"])
            if not books[i]["publication_year"]:
                self.__dataset_of_books[i].release_year = None
            else:
                self.__dataset_of_books[i].release_year = int(books[i]["publication_year"])

            self.__dataset_of_books[i].image_url = str(books[i]["image_url"])


        for book in range(len(self.__dataset_of_books)):
            for author in range(len(authors)):
                for authors_id in range(len(books[book]["authors"])):
                    if authors[author]["author_id"] in books[book]["authors"][authors_id]["author_id"]:
                        self.__dataset_of_books[book].add_author(
                            Author(int(authors[author]["author_id"]), str(authors[author]["name"])))





