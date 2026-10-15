# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Midterm Exam 2

book_dict = {
    'Ulysses': 'James Joyce',
    'Don Quixote': 'Miguel de Cervantes',
    'One Hundred Years of Solitude': 'Gabriel Garcia Marquez',
    'The Great Gatsby': 'F. Scott Fitzgerald',
    'Moby Dick': 'Herman Melville',
    'War and Peace': 'Leo Tolstoy',
    'Hamlet': 'William Shakespeare',
    'The Odyssey': 'Homer',
    'Madame Bovary': 'Gustave Flaubert',
}

for title, author in book_dict.items():
    print(f"The book {title} was written by {author}")

fav_book = input("What is your favorite book? ")
print(f"{fav_book} was written by {book_dict[fav_book]}")
