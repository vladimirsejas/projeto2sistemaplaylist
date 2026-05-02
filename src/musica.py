class Musica:
    contador_id = 1

    def __init__(self, titulo, artista, genero, bpm):
        self.id = Musica.contador_id
        Musica.contador_id = Musica.contador_id + 1

        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm

    def exibir_dados(self):
        print("ID:", self.id)
        print("Título:", self.titulo)
        print("Artista:", self.artista)
        print("Gênero:", self.genero)
        print("BPM:", self.bpm)
        print("----------------------")