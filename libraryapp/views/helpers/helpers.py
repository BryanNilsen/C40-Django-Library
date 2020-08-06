import sqlite3
from ..connection import Connection
from libraryapp.models import Book
from libraryapp.models import model_factory


class Helpers:
    # Get Book by Id
    def get_book(book_id):
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Book)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                b.id,
                b.title,
                b.isbn,
                b.author,
                b.year_published,
                b.librarian_id,
                b.location_id
            FROM libraryapp_book b
            WHERE b.id = ?
            """, (book_id,))

            return db_cursor.fetchone()
