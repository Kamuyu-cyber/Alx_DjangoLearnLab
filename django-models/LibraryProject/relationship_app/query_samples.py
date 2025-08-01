from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return [book.title for book in books]

def query_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return [book.title for book in books]

def query_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian.name
