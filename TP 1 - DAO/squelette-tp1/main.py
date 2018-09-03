from dao.dao_book import DaoBook
from business_object.book import Book
from connection import connection

daoBook = DaoBook()

if __name__ == "__main__":
    try:
        # création du livre
        book = Book(name="A la recherche du temps perdu",
                    author="Marcel Proust")
        created = daoBook.create(book)
        print('------------------------------------------------\n')
        print("Livre créé : ")
        print(created)
        found = daoBook.get_all_books()

        print('\n------------------------------------------------\n')
        print("Livres enregistrés : ")
        print(found)

    finally:
        # fermeture de la connexion avec la base
        connection.close()
