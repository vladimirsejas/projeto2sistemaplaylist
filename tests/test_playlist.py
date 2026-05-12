import unittest

from src.musica import Musica
from src.fila import Fila
from src.controlador import Controlador
from src.lista import Biblioteca


class TestSistemaPlaylist(unittest.TestCase):

    def setUp(self):

        Musica.contador_id = 1

        self.biblioteca = Biblioteca()
        self.controlador = Controlador()

    def test_fila_fifo(self):

        fila = Fila()

        musica1 = Musica("Musica 1", "Artista A", "Pop", 100)
        musica2 = Musica("Musica 2", "Artista B", "Rock", 120)

        fila.enqueue(musica1)
        fila.enqueue(musica2)

        primeira_musica = fila.dequeue()

        self.assertEqual(primeira_musica.titulo, "Musica 1")

    def test_classificacao_bpm(self):

        musica_relax = Musica("Relax", "Artista", "Lo-fi", 70)

        self.biblioteca.adicionar(musica_relax)

        self.controlador.montar_filas(self.biblioteca)

        self.assertFalse(
            self.controlador.relaxar.esta_vazia()
        )

    def test_historico_reproducao(self):

        musica = Musica("Teste", "Artista", "Pop", 100)

        self.controlador.focar.enqueue(musica)

        musica_reproduzida = self.controlador.focar.dequeue()

        self.controlador.historico.enqueue(musica_reproduzida)

        historico = self.controlador.historico.dequeue()

        self.assertEqual(historico.titulo, "Teste")

    def test_fila_vazia(self):

        resultado = self.controlador.relaxar.dequeue()

        self.assertIsNone(resultado)


if __name__ == "__main__":
    unittest.main()