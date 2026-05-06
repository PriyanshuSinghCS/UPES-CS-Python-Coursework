class BookNotAvailableError(Exception):
    pass

class MaximumBooksIssuedError(Exception):
    pass

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__is_available = True

    def is_available(self):
        return self.__is_available

    def set_availability(self, status):
        self.__is_available = status

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.__borrowed_books = []

    def get_borrowed_books(self):
        return self.__borrowed_books

    def issue_book(self, book, limit):
        if len(self.__borrowed_books) >= limit:
            raise MaximumBooksIssuedError()
        if not book.is_available():
            raise BookNotAvailableError()
        
        self.__borrowed_books.append(book)
        book.set_availability(False)

    def return_book(self, book, days_late):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            book.set_availability(True)
            fine = days_late * 5
            return fine
        return 0

class StudentMember(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.limit = 3

    def issue_book(self, book):
        super().issue_book(book, self.limit)

class FacultyMember(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.limit = 5

    def issue_book(self, book):
        super().issue_book(book, self.limit)

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def search_book(self, query):
        results = []
        for book in self.books:
            if query == book.title or query == book.author or query == book.isbn:
                results.append(book)
        return results

class Librarian:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def issue_book_to_member(self, member, book):
        member.issue_book(book)

    def receive_returned_book(self, member, book, days_late):
        fine = member.return_book(book, days_late)
        return fine
    
my_library = Library()
librarian = Librarian("Mr. Sharma", "EMP001")

book1 = Book("Python Basics", "John Doe", "12345")
book2 = Book("Data Structures", "Jane Smith", "67890")
book3 = Book("Algorithms", "Alan Turing", "11223")

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

student1 = StudentMember("Ravi", "S101")
faculty1 = FacultyMember("Dr. Gupta", "F201")

my_library.add_member(student1)
my_library.add_member(faculty1)

print("--- Testing Library System ---")

try:
    librarian.issue_book_to_member(student1, book1)
    print("Success:", book1.title, "issued to", student1.name)
except Exception as e:
    print("Error:", type(e).__name__)

try:
    librarian.issue_book_to_member(faculty1, book1)
except Exception as e:
    print("Error when faculty tried to borrow the same book:", type(e).__name__)

fine_amount = librarian.receive_returned_book(student1, book1, 2)
print("Fine for returning", book1.title, "late:", fine_amount)

search_results = my_library.search_book("Algorithms")
for b in search_results:
    print("Search found book:", b.title)