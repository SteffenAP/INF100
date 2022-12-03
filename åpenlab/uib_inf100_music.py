import pygame

# For å starte lydmikseren til pygame. Mikseren kan spille av
# flere lyder samtidig.
pygame.mixer.init()

# En klasse. Objekter av denne klassen representerer en enkelt lyd.
class Sound(object):
    def __init__(self, path):
        self.path = path
        self.loops = 1
        pygame.mixer.music.load(path)

    def is_playing(self):
        """ Returnerer True dersom lyden spilles av for øyeblikket. """
        return bool(pygame.mixer.music.get_busy())

    def start(self, loops=1):
        """ Begynner å spille av lyden. Et kall til .start() vil
        spille av lyden én gang, mens et kall til .start(loops=3) vil
        spille av lyden tre ganger. Et kall til .start(loops=-1) vil
        spille av lyden i en evig løkke.
        """
        self.loops = loops
        pygame.mixer.music.play(loops=loops)

    def stop(self):
        """ Avbryter avspilling av lyden. """
        pygame.mixer.music.stop()

# I INF100 lærer vi ikke om objekter, så vi
# later som om load_sound er en funksjon.
load_sound = Sound