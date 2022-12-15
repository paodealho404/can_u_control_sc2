# Can U Control

Desafio da disciplina de Sistemas de Controle 2, sob orientação do  Prof. Ícaro Bezerra Queiroz de Araújo.

### Alunos:
- José Ferreira Leite Neto (19111153)

- Lilian Giselly Pereira Santos (19111115)

- Lucas Lemos Cerqueira de Freitas (19111116)

- Pedro Henrique de Brito Nascimento (19111287)

# Arquivos:

## bonus_control.py

Código que utiliza o selenium para "roubar" no jogo, interagindo diretamente com o javascript da página (apenas para diversão). Caso deseje utilizar, executar os seguintes passos:

- Rodar `pip install selenium` (somente na primeira vez)
- Rodar `python .\bonus_control.py`

A página do Can U Control será aberta automaticamente. Sente e busque uma pipoca B)

## compute_functions.py

Arquivo que contém o código que controla o jogo, as funções que determinam os sinais de controle enviados estão aqui.

## control.py

Código principal que deve ser executado para rodar o controlador. Caso deseje utilizar, executar os seguintes passos:

- Acessar o site do [Can U Control ](https://dev-mind.blog/apps/CanUControl/level.html)
- Clicar no ícone do mouse na parte inferior até que se torne um "plugue" de tomada
- Rodar `pip install numpy` (somente na primeira vez)
- Rodar `pip install websockets` (somente na primeira vez)
- Rodar `pip install asyncio` (somente na primeira vez)
- Rodar `python .\control.py`

Ao clicar em play o personagem deve ser controlado pelo controlador aqui implementado

## lands_functions.py

Arquivo que contém a implementação das funções de cada um dos níveis.

## lands_parameters.py

Arquivo que contém os parâmetros refinados para cada nível.
