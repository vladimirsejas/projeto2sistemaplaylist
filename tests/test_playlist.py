import unittest

from src.musica import Musica
from src.fila import Fila


class TestSistemaPlaylist(unittest.TestCase):

    def test_fila_fifo(self):

        fila = Fila()

        musica1 = Musica("Musica 1", "Artista A", "Pop", 100)
        musica2 = Musica("Musica 2", "Artista B", "Rock", 120)

        fila.enqueue(musica1)
        fila.enqueue(musica2)

        primeira_musica = fila.dequeue()

        self.assertEqual(primeira_musica.titulo, "Musica 1")


if __name__ == "__main__":
    unittest.main()