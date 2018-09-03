from connection import connection
from business_object.book import Book


class DaoBook:

    def create(self, book):
        cur = connection.cursor()
        try:
            cur.execute(
                "INSERT INTO book (name, author) VALUES (%s, %s) RETURNING id;", (book.name, book.author))

            book.id = cur.fetchone()[0]
            # la transaction est enregistrée en base
            connection.commit()
        except:
            # la transaction est annulée
            connection.rollback()
            raise
        finally:
            cur.close()

        return book

    def get_all_books(self):
        with connection.cursor() as cur:
            cur.execute(
                "select id, name, author from book")

            # on récupère des tuples et les transforme en objects Book
            result = [Book(id=item[0], author=item[2], name=item[1])
                      for item in cur.fetchall()]
            return result
