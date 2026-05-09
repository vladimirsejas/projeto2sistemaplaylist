from src.fila import Fila


class Controlador:
    def __init__(self):
        self.relaxar = Fila()
        self.focar = Fila()
        self.animar = Fila()
        self.treinar = Fila()
        self.historico = Fila()

    # limpa uma fila drenando todos os elementos
    def limpar_fila(self, fila):
        while not fila.esta_vazia():
            fila.dequeue()

    # opção 5: monta (ou remonta) as filas de humor a partir da biblioteca
    def montar_filas(self, biblioteca):
        if biblioteca.inicio is None:
            print("Biblioteca vazia. Adicione músicas antes de montar as filas.")
            return

        # limpa filas anteriores
        self.limpar_fila(self.relaxar)
        self.limpar_fila(self.focar)
        self.limpar_fila(self.animar)
        self.limpar_fila(self.treinar)

        atual = biblioteca.inicio
        while atual is not None:
            bpm = atual.musica.bpm
            if bpm <= 80:
                self.relaxar.enqueue(atual.musica)
            elif bpm <= 120:
                self.focar.enqueue(atual.musica)
            elif bpm <= 160:
                self.animar.enqueue(atual.musica)
            else:
                self.treinar.enqueue(atual.musica)
            atual = atual.proximo

        print("Filas de humor montadas com sucesso!")

    # opção 6: retira a próxima música da fila escolhida e manda pro histórico
    def reproduzir(self, fila):
        musica = fila.dequeue()
        if musica is None:
            print("Fila vazia. Nenhuma música para reproduzir.")
            return

        print("\n--- REPRODUZINDO ---")
        musica.exibir_dados()
        self.historico.enqueue(musica)

    # opção 8: exibe o histórico completo
    def exibir_historico(self):
        print("\n--- HISTÓRICO DE REPRODUÇÕES ---")
        if self.historico.esta_vazia():
            print("Nenhuma música reproduzida ainda.")
            return
        self.historico.listar()

    # opção 9: estatísticas gerais
    def estatisticas(self, biblioteca):
        print("\n--- ESTATÍSTICAS ---")
        print("Músicas na biblioteca:", self.contar_lista(biblioteca))
        print("Fila Relaxar (até 80 BPM):", self.contar_fila(self.relaxar))
        print("Fila Focar (81-120 BPM):", self.contar_fila(self.focar))
        print("Fila Animar (121-160 BPM):", self.contar_fila(self.animar))
        print("Fila Treinar (acima de 160 BPM):", self.contar_fila(self.treinar))
        print("Total reproduzidas:", self.contar_fila(self.historico))

    # conta nós da lista encadeada (biblioteca)
    def contar_lista(self, biblioteca):
        contagem = 0
        atual = biblioteca.inicio
        while atual is not None:
            contagem = contagem + 1
            atual = atual.proximo
        return contagem

    # conta nós da fila percorrendo os nós
    def contar_fila(self, fila):
        contagem = 0
        atual = fila.inicio
        while atual is not None:
            contagem = contagem + 1
            atual = atual.proximo
        return contagem