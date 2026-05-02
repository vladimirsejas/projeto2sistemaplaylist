class Musica:
    _contador_id = 1

    def __init__(self, titulo, artista, genero, bpm):
        self.id = Musica._contador_id
        Musica._contador_id += 1

        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm

    def __str__(self):
        return f"[{self.id}] {self.titulo} - {self.artista} | {self.genero} | {self.bpm} BPM"