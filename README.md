# Circle the Cat
## Sobre o jogo
- Possui um tabuleiro.
- Possui dois jogadores (gato e pegador);
- Um jogador joga de cada vez (o pegador começa jogando) até alguem vencer;
- O gato vence se chegar em alguma saída;
- O pegador vence se prender o gato.

### Tabuleiro
- O tabuleiro possui 11x11 casas. Veja abaixo a disposição do tabuleiro.
<p align="center">
<img src="https://raw.githubusercontent.com/PedroBernini/game_circle-the-cat-best-first-search/master/Jogos/tabuleiro.jpg" text_align="center" width="700" height="593">
</p>

### Movimentação do gato
O gato pode escolher se movimentar para 6 direções (VERDE). são elas:
- Nordeste (NE);
- Leste (E);
- Sudeste (SE);
- Sudoeste (SO);
- Oeste (O);
- Noroeste (NO);

<p align="center">
<img src="https://raw.githubusercontent.com/PedroBernini/game_circle-the-cat-best-first-search/master/Jogos/movimentacao.jpg" text_align="center" width="700" height="593">
</p>

### Bloqueios
Conjunto de casas bloqueadas (VERMELHO) que o gato não pode ir. Veja abaixo o conjunto de bloqueios: 
<p align="center">
<img src="https://raw.githubusercontent.com/PedroBernini/game_circle-the-cat-best-first-search/master/Jogos/bloqueios.jpg" text_align="center" width="700" height="593">
</p>

### Exemplo de jogo
Após definir os bloqueios e as saídas (AZUL), o jogo está pronto. Veja um exemplo completo do jogo:
<p align="center">
<img src="https://raw.githubusercontent.com/PedroBernini/game_circle-the-cat-best-first-search/master/Jogos/saidas.jpg" text_align="center" width="700" height="593">
</p>

### Regras
Regras para o gato:
- Deve começar na casa (5,5);
- Não deve se movimentar em direção à uma casa bloqueada;
- Não deve sair do tabuleiro.

Regras para o pegador:
- Deve ser o primeiro a jogar;
- Não deve colocar um bloqueio na casa que o gato está;
- Não deve colocar bloqueio numa casa já bloqueada;
- Não deve colocar bloqueio fora do tabuleiro.

## Gato vencedor
Se o gato chegar em alguma das saídas o jogo termina e o gato o vence. Veja um exemplo de jogo onde o gato é o vencedor:
<p align="center">
<img src="https://raw.githubusercontent.com/PedroBernini/game_circle-the-cat-best-first-search/master/Jogos/CatWin.gif" text_align="center" width="700" height="593">
</p>

## Pegador vencedor
Se o pegador impedir que o gato se movimente para qualquer direção o jogo termina e o pegador vence. Veja um exemplo de jogo onde o pegador é o vencedor:
<p align="center">
<img src="https://raw.githubusercontent.com/PedroBernini/game_circle-the-cat-best-first-search/master/Jogos/CatcherWin.gif" text_align="center" width="700" height="593">
</p>

## Estratégias
Ambos os programas (gato e pegador) trabalham em cima do algoritmo de busca (best-first). Para saber como eles funcionam, veja o arquivo "Estratégias.pptx" dentro da pasta "Estratégias".

## Como executar um jogo
O  programa *game.py*  deve receber como  entrada  três  parâmetros  por linha  de  comando.   Esses  parêmetros  devem ser lido da seguinte forma (em uma unica linha):
*python meu_codigo.py "[5, 5]"
"[ (1,1), (1,5), (2,5), (4,5), (5,1), (5, 4), (6, 5), (8, 2) ]"
"[ (0,0), (6, 10), (9, 10), (10, 1) ]"*

- O primeiro parâmetro representa a posição do gato;
- O segundo parâmetro representa o posicionamento dos bloqueios;
- O terceiro parâmetro representa as saídas disponíveis para o gato.

O resultado do jogo final do jogo estará disponível em formato gif no arquivo *game.gif*

## Desenvolvedores
- [Felipe Marchi](https://github.com/felipemarchi)
- [Pedro Bernini](https://github.com/PedroBernini)
