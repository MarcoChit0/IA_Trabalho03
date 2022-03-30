from random import random, randint, sample, choice
from time import time


def evaluate(individual):
    '''
    Recebe individuo e retorna numero de ataques
    '''
    num_atack = 0
    proibitions = set()
    position_queens = dict()
    for x, lin in enumerate(individual):
        position_queens[x] = (x, 8 - lin)
    for values in position_queens.values():
        x = values[0]
        y = values[1]
        if x == 7:
            break
        # Adiciona casas a direita na mesma linha
        i, j = x + 1, y
        while i < 8:
            proibitions.add((i, j))
            i += 1
        # Adiciona casas a esquerda na mesma linha
        i, j = x - 1, y
        while i >= 0:
            proibitions.add((i, j))
            i -= 1
        # Adiciona casas acima na mesma coluna
        i, j = x, y + 1
        while j < 8:
            proibitions.add((i, j))
            j += 1
        # Adiciona casas abaixo na mesma coluna
        i, j = x, y - 1
        while j >= 0:
            proibitions.add((i, j))
            j -= 1
        # Adiciona casas na diagonal superior esquerda
        i, j = x - 1, y - 1
        while i >= 0 and j >= 0:
            proibitions.add((i, j))
            i, j = i - 1, j - 1
        # Adiciona casas na diagonal superior direita
        i, j = x + 1, y - 1
        while i < 8 and j >= 0:
            proibitions.add((i, j))
            i, j = i + 1, j - 1
        # Adiciona casas na diagonal inferior esquerda
        i, j = x - 1, y + 1
        while i >= 0 and j < 8:
            proibitions.add((i, j))
            i, j = i - 1, j + 1
        # Adiciona casas na diagonal inferior direita
        i, j = x + 1, y + 1
        while i < 8 and j < 8:
            proibitions.add((i, j))
            i, j = i + 1, j + 1
        # Para cada um das outras rainhas se ela estiver dentro das casas
        # de outra, incrementa num_atack
        for other_pos in range(x + 1, 8):
            if position_queens[other_pos] in proibitions:
                num_atack += 1
        proibitions.clear()
    return num_atack


def tournament(participants):
    '''
    Recebe uma lista com varios individuos e retorna o melhor deles
    '''
    scoreboard = [0] * len(participants)
    for cont_pos, ind in enumerate(participants):
        scoreboard[cont_pos] = evaluate(ind)
    index_winner = scoreboard.index(
        min(scoreboard)
    )
    return participants[index_winner]


def crossover(parent1, parent2, index):
    '''
    Recebe dois individuos e o ponto de corte entre eles e retorna
    dois individuos filhos gerados por crossover entre os pais
    '''
    offspring_1 = parent1[:index] + parent2[index:]
    offspring_2 = parent2[:index] + parent1[index:]
    return offspring_1, offspring_2


def mutate(individual, m):
    '''
    Recebe um individuo e a probabilidade se sofrer mutacao. Se o numero
    aleatorio gerado for menor que essa probebilidade, sorteia uma posicao
    aleatoria e altera o valor desta
    '''
    if random() < m:
        pos = randint(0, 7)
        while True:
            new_value = randint(1, 8)
            if new_value != individual[pos]:
                individual[pos] = new_value
                break


def random_population(num_individuals):
    '''
    Recebe um numero inteiro positivo e retorna essa mesma quantidade
    de individuos gerados de maneira aleatoria
    '''
    population = list(
        [0] * 8 for cont in range(num_individuals)
    )
    j = 0
    while j < num_individuals:
        i = 0
        while i < 8:
            population[j][i] = randint(1, 8)
            i += 1
        j += 1
    return population


def run_ga(g, n, k, m, e):
    '''
    Recebe os parametros e executa o algoritmo genetico
    g: numero de geracoes
    n: numero de individuos da populacao
    k: numero de participantes do torneio
    m: probabilidade de mutacao
    e: booleano para se havera elitismo ou nao
    '''
    parental_population = random_population(n)
    new_population = list()
    cont_geracoes = 0
    while cont_geracoes < g:
        cont_populacao = 0
        if e:
            best_parental = tournament(parental_population)
            new_population.append(best_parental)
            cont_populacao += 1
        while cont_populacao <= n:
            participants = sample(parental_population, k)
            parental_1 = tournament(participants)
            participants = sample(parental_population, k)
            parental_2 = tournament(participants)
            offspring1, offspring2 = crossover(
                parental_1, parental_2, randint(0, 7)
            )
            mutate(offspring1, m)
            mutate(offspring2, m)
            if cont_populacao + 1 == n:
                new_population.append(
                    choice([offspring1, offspring2])
                )
                cont_populacao += 1
            else:
                new_population.append(offspring1)
                new_population.append(offspring2)
                cont_populacao += 2
        parental_population = new_population.copy()
        cont_geracoes += 1
    return tournament(parental_population)


ini = time()
# n grande e k pequeno parece ser melhor para achar valor 0
a = run_ga(10, 200, 10, 0.3, True)
fim = time()                       # mutacao demais (m grande) parece ser ruim
print(a)
print(evaluate(a))
print(f'Tempo execução = {fim - ini}')

# g = 15, n = 200, k = 10, m = 0.2, e = True parecem resultar em sucesso (0 ataques) em aproximadamente 50% das tentativas
