class Book:
    """A base class for representing a book."""
    
    def __init__(self, title, author):
        """Initialize a book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """A class representing an eBook, derived from Book."""
    
    def __init__(self, title, author, file_size):
        """Initialize an eBook with title, author, and file size."""
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of the eBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """A class representing a print book, derived from Book."""
    
    def __init__(self, title, author, page_count):
        """Initialize a print book with title, author, and page count."""
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """A class to manage a collection of books."""
    
    def __init__(self):
        """Initialize an empty library."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library."""
        for book in self.books:
            print(book)

