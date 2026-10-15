# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Midterm Exam 1

book_list = [
    'Ulysses',
    'Don Quixote',
    'One Hundred Years of Solitude',
    'The Great Gatsby',
    'Moby Dick',
    'War and Peace',
    'Hamlet',
    'The Odyssey',
    'Madame Bovary',
]

#I assume by "a blank line after each", the result should look double-spaced.
#So, I'll also insert a newline after each print.

for book in book_list:
    print(f"{book.lower()}")
    print();