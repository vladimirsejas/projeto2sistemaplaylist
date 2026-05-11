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

        # 1 — adicionar música
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
            print(f"Música '{titulo}' adicionada com ID {musica.id}.")

        # 2 — remover música
        elif opcao == "2":
            try:
                id_remover = int(input("ID da música a remover: ").strip())
            except ValueError:
                print("ID inválido. Digite um número inteiro.")
                continue

            removida = biblioteca.remover(id_remover)
            if removida:
                print(f"Música com ID {id_remover} removida com sucesso.")
            else:
                print(f"Nenhuma música encontrada com ID {id_remover}.")

        # 3 — buscar música
        elif opcao == "3":
            print("Buscar por:")
            print("1. ID")
            print("2. Título")
            tipo = input("Opção: ").strip()

            if tipo == "1":
                try:
                    id_busca = int(input("ID: ").strip())
                except ValueError:
                    print("ID inválido.")
                    continue
                musica = biblioteca.buscar_por_id(id_busca)

            elif tipo == "2":
                titulo_busca = input("Título: ").strip()
                musica = biblioteca.buscar_por_titulo(titulo_busca)

            else:
                print("Opção inválida.")
                continue

            if musica:
                print("\n--- MÚSICA ENCONTRADA ---")
                musica.exibir_dados()
            else:
                print("Música não encontrada.")

        # 4 — listar biblioteca
        elif opcao == "4":
            print("\n--- BIBLIOTECA COMPLETA ---")
            biblioteca.listar()

        # 5 — montar filas por humor
        elif opcao == "5":
            controlador.montar_filas(biblioteca)

        # 6 — reproduzir próxima
        elif opcao == "6":
            fila, nome = escolher_fila(controlador)
            if fila is not None:
                controlador.reproduzir(fila)

        # 7 — exibir fila de humor
        elif opcao == "7":
            fila, nome = escolher_fila(controlador)
            if fila is not None:
                controlador.exibir_fila(fila, nome)

        # 8 — histórico
        elif opcao == "8":
            controlador.exibir_historico()

        # 9 — estatísticas
        elif opcao == "9":
            controlador.estatisticas(biblioteca)

        # 10 — sair
        elif opcao == "10":
            print("Encerrando o sistema. Até mais!")
            break

        else:
            print("Opção inválida. Digite um número de 1 a 10.")


if __name__ == "__main__":
    main()