import numpy as np


def read_data_csv(file_name):
    """
    Le dados de um arquivo csv e retorna um ndarray bidimensional (matriz)
    onde a primeira coluna contem a area dos terrenos e a segunda coluna 
    contem os precos em milhares de reais
    :param file_name: string - endereco do arquivo a ser lido
    :return: ndarray bidimensional - matriz de dados
    """
    data = np.genfromtxt(file_name, delimiter=',')
    return data


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
    # copia todos os valores da primeira coluna (Xi) e aplica a funcao para calculo
    # dos valores previstos e subtrai os valores reais de Yi
    predicted_values = np.copy(data[:, 0]) * theta_1 + theta_0
    predicted_values = predicted_values - data[:, 1]
    num_elementos = predicted_values.size
    # calcula derivadas para theta_0 e theta_1
    sum_to_theta_0 = np.sum(predicted_values) * (2 / num_elementos)
    sum_to_theta_1 = np.sum(
        predicted_values * data[:, 0]) * (2 / num_elementos)
    # calcula novos valores para theta_0 e theta_1
    new_theta_0 = theta_0 - alpha * sum_to_theta_0
    new_theta_1 = theta_1 - alpha * sum_to_theta_1
    return new_theta_0, new_theta_1


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
    cont_iterations = 0
    all_theta_0 = list()
    all_theta_1 = list()
    all_theta_0.append(theta_0)
    all_theta_1.append(theta_1)
    prox_theta_0, prox_theta_1 = theta_0, theta_1
    while cont_iterations != num_iterations:
        prox_theta_0, prox_theta_1 = step_gradient(
            prox_theta_0, prox_theta_1, data, alpha
        )
        all_theta_0.append(prox_theta_0)
        all_theta_1.append(prox_theta_1)
        cont_iterations += 1
    return all_theta_0, all_theta_1


dados = read_data_csv('alegrete.csv')
print(fit(dados, 0, 0.5, 0.1, 30))
