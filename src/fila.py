class NodoFila:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enqueue(self, musica):
        novo = NodoFila(musica)

        if self.inicio == None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

    def dequeue(self):
        if self.inicio == None:
            print("Fila vazia")
            return None

        removido = self.inicio
        self.inicio = self.inicio.proximo

        if self.inicio == None:
            self.fim = None

        return removido.musica

    def esta_vazia(self):
        if self.inicio == None:
            return True
        return False

    def listar(self):
        if self.inicio == None:
            print("Fila vazia")
            return

        atual = self.inicio
        while atual != None:
            atual.musica.exibir_dados()
            atual = atual.proximo