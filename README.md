Exercício 1
Exercício de Habilidade
Julia e Camila estão fazendo um estudo com cachorros. Cada uma perguntou para 5
donos a idade de seus cachorros e guardou as idades em Arrays (um array para Julia e
um para Camila). Agora, estão interessadas em saber se o cachorro é adulto ou filhote.
Um cachorro é considerado adulto se tiver pelo menos 3 anos e considerado filhote se
tiver menos que 3 anos.
Sua tarefa:
Crie uma função chamada “checarCachorros”, que aceita 2 Arrays contendo as idades
e então, faça o seguinte:
1- Julia percebeu que os donos do primeiro e dos últimos 2 cachorros na verdade são
gatos, não cachorros! Então crie uma cópia do Array de Julia e remova as idades dos
gatos.
2 - Crie um Array contendo as informações do array de Julia e de Camila.
3 - Para cada cachorro restante, printe se um cachorro é adulto ou filhote da seguinte
forma (“ O cachorro número 1 é um adulto e tem 5 anos de idade”) ou (“ O cachorro
número 3 é um filhote e tem 2 anos de idade”)
4 - Rode a função para os dois conjuntos de dados.
Dados:
Julia => [3,2,1,12,3], Camila => [4,12,15,8,3]
Julia => [9,16,6,8,3], Camila => [10,5,6,1,4]

Exercício 2
Exercício Case Real
Na ATX Automation, existe uma base de dados que corriqueiramente está com
alguns erros de Bits. Nossa missão é receber esses dados do Excel com Bits
Errados, executar uma lógica em cima deles e devolver um Excel com Bits
Errados e Bits Arrumados.
Sua tarefa:
- Importar a(s) biblioteca(s);
- Ler o arquivo Excel;
- Pegar só a Coluna Bit Errado e transformar ela em uma lista;
- Criar uma função chamada “arrumaBit” que recebe como parâmetro a lista
anterior;
- Essa função deve pegar cada elemento da lista e executar a lógica:
- Pegar o valor após a barra e dividir por 16… Parte inteira da divisão é a
‘Palavra’ e o resto da divisão é o ‘Bit’
- Exemplo: B11/35 ------> B11:’Palavra’/’Bit’
- 35 Dividido por 16 tem parte inteira = 2 e resto da divisão = 3
- Logo, o Bit B11/35 arrumado fica no formato B11:2/3
- Criar um DataFrame com duas Colunas (Bit errado e Bit Certo)
- Exportar esse DataFrame para um Excel