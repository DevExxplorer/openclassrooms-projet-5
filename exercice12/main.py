class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Livre '{book.title}' ajouté à la librairie.")

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f"Livre '{book_title}' supprimé de la librairie.")
                return

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrow_books.append(book)

    def return_book(self, book_title):
        for book in self.borrow_books:
            if book.title == book_title:
                self.borrow_books.remove(book)
                self.books.append(book)

    def available_books(self):
        return [book.title for book in self.books]

    def borrowed_books(self):
        return [book.title for book in self.borrow_books]

book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

# Créer une bibliothèque
library = Library()

# Ajouter des livres à la bibliothèque
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Afficher les livres disponibles
print("\nLivres disponible:", library.available_books())

# Emprunter un livre
library.borrow_book("1984")
print("\nLivres disponible apres emprunt:", library.available_books())
print("Livres emprunté:", library.borrowed_books())

# Rendre un livre
library.return_book("1984")
print("\nLivres disponible apres retour:", library.available_books())
print("Livres emprunté:", library.borrowed_books())

# Supprimer un livre
library.remove_book("The Great Gatsby")
print("\nLivres apres suppresion:", library.available_books())
