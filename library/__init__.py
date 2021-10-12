"""Initialize Flask app."""
from pathlib import Path
from flask import Flask, render_template
import library.adapters.repository as repo
from library.adapters.memory_repository import MemoryRepository, populate





def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    data_path = Path('library') / 'adapters' / 'data'

    repo.repo_instance = MemoryRepository()

    populate(data_path, repo.repo_instance)



    with app.app_context():
        from .book_blueprint import book_blue
        app.register_blueprint(book_blue.book_blueprint)

        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)


    return app