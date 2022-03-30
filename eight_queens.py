from copy import deepcopy
from math import ceil, floor
import random
from time import time
import numpy as np
import matplotlib.pyplot as plt

QUEEN_VALUE = 1
PROB_TOP1 = 0.5

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
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 10.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    new_ind = deepcopy(individual)
    new_ind[:] = [i - 1 for i in new_ind]
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
    for row, col in enumerate(new_ind):
        queen_pos = (row, col)
        add_queen_to_the_board(board, queen_pos, queens)
    v = 0
    for q in queens:
        v += q.value
    return v

def add_queen_to_the_board(board, queen_pos, queens):
    value = 0
    # não tem para que expandir se a primeira rainha não vai colidir com nenhuma outra
    if len(queens) > 0:
        value +=    horizontal_expansion(board, queen_pos)
        value +=    vertical_expansion(board, queen_pos)
        value +=    diagonal_expansion(board, queen_pos)
    new_queen = Queen(queen_pos, value)
    queens.append(new_queen)
    board[queen_pos[0]][queen_pos[1]] = QUEEN_VALUE
    return

def vertical_expansion(board, queen_pos):
    sum = 0
    for ver in range(8):
        if board[ver][queen_pos[1]] == QUEEN_VALUE:
            sum += 1
    return sum

def horizontal_expansion(board, queen_pos):
    sum = 0
    for hor in range(8):
        if board[queen_pos[0]][hor] == QUEEN_VALUE:
            sum += 1
    return sum

# diagonal nem sempre vai até 8
def diagonal_expansion(board, queen_pos):
    sum = 0 
    dict_boardCorner_deltaPos = {
        (0,0):(-1,-1),
        (0,7):(-1,1),
        (7,0):(1,-1),
        (7,7):(1,1)}
    for key in dict_boardCorner_deltaPos:
        sum += diagonal_search(board, queen_pos, key, dict_boardCorner_deltaPos[key])
    return sum

def diagonal_search(board, queen_pos, end_pos, delta_pos):
    sum = 0
    pos = deepcopy(queen_pos)
    while checkOutOfBorders(pos) and pos != end_pos:
        if board[pos[0]][pos[1]] == QUEEN_VALUE:
            sum += 1
        x = pos[0] 
        x += delta_pos[0]
        y = pos[1] 
        y += delta_pos[1]
        pos = (x,y)
    return sum

def checkOutOfBorders(current_pos):
    if 0 <= current_pos[0] <= 7 and 0 <= current_pos[1] <= 7:
        return True
    else: 
        return False

def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    if len(participants) > 0:
        best_value = evaluate(participants[0])
        best = participants[0]
        for p in participants:
            p_value = evaluate(p)
            if best_value > p_value:
                best_value = p_value
                best = p
        return best
    else: 
        return None


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
    if 1 <= index <= 7:
        uc1 = deepcopy(parent1[0:index])
        uc2 = deepcopy(parent2[0:index])
        c1 = deepcopy(parent1[index:len(parent1)])
        c2 = deepcopy(parent2[index:len(parent2)])
        offspring1 = uc1 + c2
        offspring2 = uc2 + c1
        return offspring1, offspring2
    else: 
        return parent1, parent2


def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao (0<= m <= 1)
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    if random.random() < m:
        pos = int(random.uniform(0,8))
        value = int(random.uniform(1,9))
        individual[pos] = value
    return individual


def run_ga(g, n, k, m, e, mostrar_grafico= False):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:bool - se vai haver elitismo
    :param mostrar_grafico:bool - se devemos mostrar ou não o gráfico da execução do algoritmo
    :return:list - melhor individuo encontrado
    """
    pool = generate_random_pool(n)
    if mostrar_grafico:
        piores_valores = []
        valores_medios = []
        melhores_valores = []
        x = []
        melhor_possivel = []
    for index in range(g):
        new_pool = []
        if e:
            new_pool.append(tournament(pool))
        while len(new_pool) < n:
            p1 =  tournament(pool[0:k])
            dc = deepcopy(pool)
            dc.remove(p1)
            p2 = tournament(dc[0:k])
            o1, o2 = crossover(p1, p2, int(random.uniform(0,7)))
            o1 = mutate(o1, m)
            o2 = mutate(o2, m)
            new_pool.append(o1)
            new_pool.append(o2)
        if mostrar_grafico:
            pool = new_pool
            piores_valores.append(pior(pool))
            valores_medios.append(media(pool))
            melhores_valores.append(evaluate(tournament(pool)))
            x.append(index)
            melhor_possivel.append(0)

    if mostrar_grafico:
        plt.plot(x, piores_valores, 'r', x, valores_medios, 'b', x, melhores_valores, 'g', x, melhor_possivel, 'k')
        plt.show()
    return tournament(pool)

def generate_random_pool(pool_size):
    pool = []
    basic_individual = [1,1,1,1,1,1,1,1]
    for i in range(pool_size):
        new_element = deepcopy(basic_individual)
        for j in range(8):
            new_element[j] = int(random.uniform(1,9))
        pool.append(new_element)
    return pool

def media(pool):
    m = 0
    for p in pool: 
        m += evaluate(p)
    return m/len(pool)

def pior(pool):
    valor_pior_competidor = 0
    for p in pool:
        if evaluate(p) >= valor_pior_competidor:
            valor_pior_competidor = evaluate(p)
    return valor_pior_competidor

'''
print("original")
run_ga(20,200,10,0.4, True, True)

print("variação - param 1")
run_ga(10,200,10,0.4, True, True)
run_ga(30,200,10,0.4, True, True)

print("variação - param 2")
run_ga(20,100,10,0.4, True, True)
run_ga(20,300,10,0.4, True, True)

print("variação - param 3")
run_ga(20,200,5,0.4, True, True)
run_ga(20,200,15,0.4, True, True)

print("variação - param 4")
run_ga(20,200,10,0.2, True, True)
run_ga(20,200,10,0.3, True, True)

print("original - sem elitismo")
run_ga(20,200,10,0.4,   False, True)

print("variação - param 1")
run_ga(10,200,10,0.4,   False, True)
run_ga(30,200,10,0.4,   False, True)

print("variação - param 2")
run_ga(20,100,10,0.4,   False, True)
run_ga(20,300,10,0.4,   False, True)

print("variação - param 3")
run_ga(20,200,5,0.4,    False, True)
run_ga(20,200,15,0.4,   False, True)

print("variação - param 4")
run_ga(20,200,10,0.2,   False, True)
run_ga(20,200,10,0.3,   False, True)
'''
