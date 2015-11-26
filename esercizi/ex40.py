#Esercizio 40

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


happy_bday = Song(["Happy bday to you",
                    "I don't want to get sued",
                    "So I'll stop right there."])

bulls_on_parade = Song(["They rally round tha family",
                        "With pockets full of shells"])

friday_im_in_love = Song(["Monday you can fall apart",
                            "Tuesday Wednesday break my heart",
                            "Thursday doesn't even start",
                            "If Friday I'm in love!"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

friday_im_in_love.sing_me_a_song()

print "*" * 22

##fineee##
