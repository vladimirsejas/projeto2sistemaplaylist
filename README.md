# projeto2sistemaplaylist
Sobre o Projeto: Playlist com Estrutura de DadosA ideia desse projeto é criar um simulador de playlist, mas o foco não é a música em si, e sim estudar Estrutura de Dados (especialmente Lista Encadeada e um pouco de Fila). É bom deixar claro: o sistema não toca áudio de verdade. As músicas aqui são só "objetos" que a gente usa para aprender como organizar, inserir e buscar informações dentro de uma estrutura.  Para entender melhor: pensa numa lista de contatos do celular. Ela não faz a ligação sozinha, ela só organiza os nomes e números. Ou uma biblioteca, que guarda os livros mas não lê eles para você. Essa playlist é a mesma coisa: ela só organiza os dados das músicas (título, artista, BPM) para a gente treinar como manipular esses dados no código. 
Como o código foi dividido:
Para não virar uma bagunça, separei o projeto em partes menores:  Musica: É onde definimos o que cada música tem (ID, título, artista, etc.).  Lista e Fila: São as "engrenagens". É aqui que a mágica da estrutura acontece, usando nós que se conectam um no outro.  Controlador: É o cérebro que cuida das regras, tipo como adicionar uma música ou montar a fila pelo humor.  Main: É a casca do programa, onde fica o menu para o usuário escolher o que quer fazer.  Por que estamos fazendo assim?
Na faculdade, isso serve para a gente ver na prática como funcionam os Nós, os ponteiros que ligam um elemento ao outro e como percorrer uma lista do começo ao fim. Além disso, separar o código em arquivos diferentes ajuda a entender como organizar um sistema real, onde cada parte tem sua responsabilidade. 
Aviso importante:
Não espere ouvir nada! O projeto não usa áudio, nem Spotify, nem YouTube. O objetivo da nossa disciplina é entender o que acontece "por baixo do capô" na organização dos dados, e não fazer um player de música completo.  

## Classe Musica  (musica.py)
Representa uma música no sistema com título, artista, gênero e BPM.
O ID é gerado automaticamente usando uma variável de classe (`_contador_id`), garantindo que não seja reutilizado mesmo após remoção, conforme o requisito do projeto.
O método `__str__` define como a música é exibida ao usar `print()`.

## Lista Encadeada (Biblioteca) (lista.py)
Representa a estrutura que armazena e organiza as músicas no sistema usando nós ligados entre si. Cada nó guarda uma música e aponta para o próximo, permitindo percorrer a lista do início ao fim.
A classe Biblioteca permite adicionar músicas, listar, buscar por ID ou título, remover e contar elementos. Não utiliza índice, pois o acesso é feito caminhando nó por nó.
O objetivo é entender na prática como funciona uma lista encadeada.
