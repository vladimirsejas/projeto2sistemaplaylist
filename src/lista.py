# nó da lista — guarda uma música e aponta para o próximo
class NodoLista:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


# biblioteca — lista encadeada de músicas
class Biblioteca:
    def __init__(self):
        self.inicio = None

    # adiciona uma música no final da lista
    def adicionar(self, musica):
        novo = NodoLista(musica)

        if self.inicio is None:
            self.inicio = novo
            return

        atual = self.inicio
        while atual.proximo is not None:
            atual = atual.proximo

        atual.proximo = novo

    # lista todas as músicas cadastradas
    def listar(self):
        if self.inicio is None:
            print("A biblioteca está vazia.")
            return

        atual = self.inicio
        while atual is not None:
            atual.musica.exibir_dados()
            atual = atual.proximo

    # busca uma música pelo id
    def buscar_por_id(self, id_busca):
        atual = self.inicio
        while atual is not None:
            if atual.musica.id == id_busca:
                return atual.musica
            atual = atual.proximo
        return None

    # busca uma música pelo título (sem diferenciar maiúsculas ou espaços)
    def buscar_por_titulo(self, titulo_busca):
        atual = self.inicio
        while atual is not None:
            if atual.musica.titulo.strip().lower() == titulo_busca.strip().lower():
                return atual.musica
            atual = atual.proximo
        return None

    # remove uma música pelo id
    def remover(self, id_remover):
        atual = self.inicio
        anterior = None

        while atual is not None:
            if atual.musica.id == id_remover:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo

        return False

    # conta quantas músicas estão na biblioteca
    def tamanho(self):
        contador = 0
        atual = self.inicio
        while atual is not None:
            contador = contador + 1
            atual = atual.proximo
        return contador