# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Midterm Exam 3

def make_book(book_title, book_author, book_length=100):
    return {'title': book_title,
            'author': book_author,
            'length': book_length,}

print(make_book("Ulysses", "James Joyce", 762))
print(make_book(book_title="The Odyssey", book_author="Homer"))
