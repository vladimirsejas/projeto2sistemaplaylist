from src.fila import Fila


class Controlador:
    def __init__(self):
        # filas de reprodução por humor
        self.relaxar = Fila()
        self.focar = Fila()
        self.animar = Fila()
        self.treinar = Fila()
        # fila de histórico
        self.historico = Fila()

    # limpa completamente uma fila
    def limpar_fila(self, fila):
        while not fila.esta_vazia():
            fila.dequeue()

    # opção 5: monta as filas de humor com base no BPM
    def montar_filas(self, biblioteca):
        if biblioteca.inicio is None:
            print("Biblioteca vazia. Adicione músicas antes de montar as filas.")
            return

        # limpa filas anteriores antes de remontar
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

    # opção 6: reproduz a próxima música da fila escolhida
    def reproduzir(self, fila):
        musica = fila.dequeue()
        if musica is None:
            print("Fila vazia. Nenhuma música para reproduzir.")
            return

        print("\n--- REPRODUZINDO AGORA ---")
        musica.exibir_dados()
        # envia música reproduzida para o histórico
        self.historico.enqueue(musica)

    # opção 7: exibe uma fila sem remover elementos
    def exibir_fila(self, fila, nome_fila):
        print(f"\n--- FILA {nome_fila.upper()} ---")
        if fila.esta_vazia():
            print("Fila vazia.")
            return
        fila.listar()

    # opção 8: exibe o histórico de reproduções
    def exibir_historico(self):
        print("\n--- HISTÓRICO DE REPRODUÇÕES ---")
        if self.historico.esta_vazia():
            print("Nenhuma música foi reproduzida ainda.")
            return
        self.historico.listar()

    # opção 9: estatísticas gerais do sistema
    def estatisticas(self, biblioteca):
        print("\n--- ESTATÍSTICAS DO SISTEMA ---")
        print("Total de músicas na biblioteca:", self.contar_lista(biblioteca))
        print("Fila Relaxar (até 80 BPM):", self.contar_fila(self.relaxar))
        print("Fila Focar (81-120 BPM):", self.contar_fila(self.focar))
        print("Fila Animar (121-160 BPM):", self.contar_fila(self.animar))
        print("Fila Treinar (acima de 160 BPM):", self.contar_fila(self.treinar))
        print("Total de músicas reproduzidas:", self.contar_fila(self.historico))

    # conta elementos da lista encadeada (biblioteca)
    def contar_lista(self, biblioteca):
        contagem = 0
        atual = biblioteca.inicio
        while atual is not None:
            contagem = contagem + 1
            atual = atual.proximo
        return contagem

    # conta elementos de uma fila percorrendo os nós
    def contar_fila(self, fila):
        contagem = 0
        atual = fila.inicio
        while atual is not None:
            contagem = contagem + 1
            atual = atual.proximo
        return contagem