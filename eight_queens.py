from copy import deepcopy


QUEEN_VALUE = 1

class Queen: 
    def __init__ (self, position, value):
        self.position = position
        self.value = value
    
    def print(self):
        print("pos: ", self.position, " -- value: ", self.value)


"""
    M <- matriz 8 x 8 de zeros
    individual <- array contendo as posições das 8 rainhas
    loop:
        colocar a rainha no tabuleiro
        expandir linha horizontal, linha vertical e diagonais
        se durante expansão encontrou outra rainha: 
            contar quantas rainhas foram encontradas
"""
def evaluate(individual):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 9.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    
    # board [0...7][0...7]
    board = [
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
    queens = []
    for row, col in enumerate(individual):
        queen_pos = (row, col)
        add_queen_to_the_board(board, queen_pos, queens)
    print(board)
    v = 0
    for q in queens:
        q.print()
        v += q.value
    print(v/2)

def add_queen_to_the_board(board, queen_pos, queens):
    original_value = deepcopy(board[queen_pos[0]][queen_pos[1]])
    new_queen = Queen(queen_pos , original_value)
    board[queen_pos[0]][queen_pos[1]] = QUEEN_VALUE
    queens.append(new_queen)
    vertical_expansion(board, queen_pos, queens)
    horizontal_expansion(board, queen_pos, queens)
    # diagonal_expansion(board, queen_pos, queens)
    return

def update_queen_list(queen_pos, queens):
    for q in queens:
        if q.position[0] == queen_pos[0] and q.position[1] == queen_pos[1]:
            q.value = q.value + 1

def vertical_expansion(board, queen_pos, queens):
    for ver in range(8):
        if board[ver][queen_pos[1]] != QUEEN_VALUE:
            board[ver][queen_pos[1]] = board[ver][queen_pos[1]] + 1
        else:
            if board[ver][queen_pos[1]] != queen_pos:
                update_queen_list(queen_pos, queens)

def horizontal_expansion(board, queen_pos, queens):
    for hor in range(8):
        if board[queen_pos[0]][hor] != QUEEN_VALUE:
            board[queen_pos[0]][hor] = board[queen_pos[0]][hor] + 1
        else:
            print("chamei")
            update_queen_list(queen_pos, queens)

def diagonal_expansion(board, queen_pos, queens):
    raise NotImplementedError

def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    raise NotImplementedError  # substituir pelo seu codigo


def crossover(parent1, parent2, index):
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """
    raise NotImplementedError  # substituir pelo seu codigo


def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    raise NotImplementedError  # substituir pelo seu codigo


def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:bool - se vai haver elitismo
    :return:list - melhor individuo encontrado
    """
    raise NotImplementedError  # substituir pelo seu codigo

evaluate([6,6,6,6,6,6,6,6])