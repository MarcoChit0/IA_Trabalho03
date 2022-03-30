from copy import deepcopy
from wsgiref.simple_server import demo_app
import numpy as np

def compute_mse(theta_0, theta_1, data):
    """
    Calcula o erro quadratico medio
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    # copia todos os valores da primeira coluna (Xi) e aplica a funcao para calculo
    # dos valores previstos
    predicted_values = np.copy(data[:, 0]) * theta_1 + theta_0
    # calcula os erros quadraticos para cada valor
    erros_quadrados = (predicted_values - data[:, 1]) ** 2
    # calcula o erro quadratico medio
    erro_quadratico_medio = np.sum(erros_quadrados) / erros_quadrados.size
    return erro_quadratico_medio

def step_gradient(theta_0, theta_1, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de theta_0 e theta_1.
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de theta_0 e theta_1, respectivamente
    """
    h = np.copy(data[:,0]) * theta_1 + theta_0
    derivada_theta_0 = h - np.copy(data[:,1])
    derivada_theta_1 = np.copy(derivada_theta_0)
    derivada_theta_1 = np.copy(derivada_theta_1) * np.copy(data[:,0])
    num_elementos = len(data)
    num_elementos = 2 / num_elementos
    derivada_theta_0 = np.sum(derivada_theta_0) * num_elementos
    derivada_theta_1 = np.sum(derivada_theta_1) * num_elementos
    theta_0 -= alpha * derivada_theta_0
    theta_1 -= alpha * derivada_theta_1
    return theta_0, theta_1


def fit(data, theta_0, theta_1, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de theta_0 e theta_1.
    Ao final, retorna duas listas, uma com os theta_0 e outra com os theta_1
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os theta_0 e outra com os theta_1 obtidos ao longo da execução
    """
    lista_theta_0 = [theta_0]
    lista_tetha_1 = [theta_1]
    i = 0
    while i != num_iterations:
        theta_0, theta_1 = step_gradient(theta_0, theta_1, data, alpha)
        lista_theta_0.append(deepcopy(theta_0))
        lista_tetha_1.append(deepcopy(theta_1))
        i += 1
    return lista_theta_0, lista_tetha_1

"""
# inicialização
path = 'D:/UFRGS/IA/Trabalhos/Trabalho 03/IA_Trabalho03/alegrete.csv'
theta_0 = 0
theta_1 = 0
alpha = 0.1
iteracoes = 50
fator = 1
print("obtendo dados:")
dados = np.genfromtxt(path, delimiter=',')

print("configuração original:")
lista_theta_0, lista_theta_1 = fit(dados, theta_0, theta_1, alpha, iteracoes)
print("theta_0: ", lista_theta_0[iteracoes - 1], " theta_1: ",lista_theta_1[iteracoes -1])


print("alterações no aplha:")
fator = 2
lista_theta_0, lista_theta_1 = fit(dados, theta_0, theta_1, alpha*fator, iteracoes)
print("theta_0: ", lista_theta_0[iteracoes - 1], " theta_1: ",lista_theta_1[iteracoes -1])
fator = 3
lista_theta_0, lista_theta_1 = fit(dados, theta_0, theta_1, alpha*fator, iteracoes)
print("theta_0: ", lista_theta_0[iteracoes - 1], " theta_1: ",lista_theta_1[iteracoes -1])


print("alterações na iteração:")
fator = 2
lista_theta_0, lista_theta_1 = fit(dados, theta_0, theta_1, alpha, iteracoes*fator)
print("theta_0: ", lista_theta_0[iteracoes*fator - 1], " theta_1: ",lista_theta_1[iteracoes*fator -1])
fator = 4
lista_theta_0, lista_theta_1 = fit(dados, theta_0, theta_1, alpha, iteracoes*fator)
print("theta_0: ", lista_theta_0[iteracoes*fator - 1], " theta_1: ",lista_theta_1[iteracoes*fator -1])
"""
