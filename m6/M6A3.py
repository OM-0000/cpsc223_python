# Name: Ossama Mostafa
# Student ID: 871567681
# Section: 18254
# Assignment: Module 6 Assignment 3

def make_album(artist, album_title, numsongs='None'):
    return {'artist': artist, 
            'title': album_title,
            'number of songs': numsongs,
           }

album_title = input("What is the title of the album (or q for quit)? ")
artist_name = ''
while (album_title != 'q'):
    artist_name = input("What is the name of the artist? ")
    print(make_album(artist_name, album_title))
    album_title = input("What is the title of the album (or q for quit)? ")