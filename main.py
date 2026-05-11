
from src.musica import Musica
from src.lista import Biblioteca
from src.controlador import Controlador


def menu():
    print("\n===== SISTEMA DE PLAYLIST =====")
    print("1. Adicionar música à biblioteca")
    print("2. Remover música da biblioteca")
    print("3. Buscar música")
    print("4. Listar biblioteca completa")
    print("5. Montar filas de reprodução por humor")
    print("6. Reproduzir próxima música")
    print("7. Exibir fila de humor")
    print("8. Exibir histórico de reproduções")
    print("9. Estatísticas")
    print("10. Sair")
    print("================================")


def escolher_fila(controlador):
    print("\nEscolha a fila de humor:")
    print("1. Relaxar (até 80 BPM)")
    print("2. Focar (81-120 BPM)")
    print("3. Animar (121-160 BPM)")
    print("4. Treinar (acima de 160 BPM)")

    opcao = input("Opção: ").strip()

    if opcao == "1":
        return controlador.relaxar, "Relaxar"

    elif opcao == "2":
        return controlador.focar, "Focar"

    elif opcao == "3":
        return controlador.animar, "Animar"

    elif opcao == "4":
        return controlador.treinar, "Treinar"

    else:
        print("Opção inválida.")
        return None, None


def main():
    biblioteca = Biblioteca()
    controlador = Controlador()

    while True:
        menu()

        opcao = input("Escolha uma opção: ").strip()

        # opção 1 — adicionar música
        if opcao == "1":
            titulo = input("Título: ").strip()
            artista = input("Artista: ").strip()
            genero = input("Gênero: ").strip()

            try:
                bpm = int(input("BPM: ").strip())

            except ValueError:
                print("BPM inválido. Digite um número inteiro.")
                continue

            musica = Musica(titulo, artista, genero, bpm)

            biblioteca.adicionar(musica)

            print(f"Música adicionada com ID {musica.id}.")

        # opção 2 — remover música
        elif opcao == "2":

            try:
                id_remover = int(input("Digite o ID da música: ").strip())

            except ValueError:
                print("ID inválido.")
                continue

            removida = biblioteca.remover(id_remover)

            if removida:
                print("Música removida com sucesso.")

            else:
                print("Música não encontrada.")

        # opção 3 — buscar música
        elif opcao == "3":

            print("\nBuscar por:")
            print("1. ID")
            print("2. Título")

            tipo_busca = input("Escolha: ").strip()

            if tipo_busca == "1":

                try:
                    id_busca = int(input("Digite o ID: ").strip())

                except ValueError:
                    print("ID inválido.")
                    continue

                musica = biblioteca.buscar_por_id(id_busca)

            elif tipo_busca == "2":

                titulo_busca = input("Digite o título: ").strip()

                musica = biblioteca.buscar_por_titulo(titulo_busca)

            else:
                print("Opção inválida.")
                continue

            if musica is not None:

                print("\n--- MÚSICA ENCONTRADA ---")

                musica.exibir_dados()

            else:
                print("Música não encontrada.")

        # opção 4 — listar biblioteca
        elif opcao == "4":

            print("\n--- BIBLIOTECA COMPLETA ---")

            biblioteca.listar()

        # opção 5 — montar filas
        elif opcao == "5":

            controlador.montar_filas(biblioteca)

        # opção 6 — reproduzir próxima
        elif opcao == "6":

            fila, nome = escolher_fila(controlador)

            if fila is not None:
                controlador.reproduzir(fila)

        # opção 7 — exibir fila
        elif opcao == "7":

            fila, nome = escolher_fila(controlador)

            if fila is not None:
                controlador.exibir_fila(fila, nome)

        # opção 8 — histórico
        elif opcao == "8":

            controlador.exibir_historico()

        # opção 9 — estatísticas
        elif opcao == "9":

            controlador.estatisticas(biblioteca)

        # opção 10 — sair
        elif opcao == "10":

            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Digite um número de 1 a 10.")


if __name__ == "__main__":
    main()

