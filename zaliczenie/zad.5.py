'''

Zadanie 5. Napisz klasę Playlist, która będzie reprezentować listę odtwarzania utworów muzycznych.
 Klasa powinna zawierać metody magiczne __add__, __radd__, __getitem__ oraz __setitem__,
 aby umożliwić łączenie dwóch list odtwarzania, dodawanie utworu do listy odtwarzania,
 uzyskiwanie utworów z listy odtwarzania oraz ustawianie wartości utworów na liście odtwarzania.
'''

class Playlist:
    def __init__(self, list_songs):
        self.list_songs = list_songs

    #Łączenie list
    def __add__(self, other):
        listsongs =[]
        listsongs.extend(self.list_songs)
        listsongs.extend(other.list_songs)
        return listsongs

    def __setitem__(self, number_song, title):
        self.list_songs[number_song] = title

    def __getitem__(self, number_song):
        return self.list_songs[number_song]


    def __str__(self):
        return f'{self.list_songs}'

p1 = Playlist(['u1','u2'])
p2 = Playlist(['u111','u211'])
print(p1)
print(p1 + p2)
p1[0]='Jamajka'
print(p1)
print(p1[0])
