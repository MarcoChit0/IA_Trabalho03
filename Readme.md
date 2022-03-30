# Trabalho 02:

## Membros:
| Membro                            | Cartão    |
| ---                               | ---       |
| Bruna da Cruz Chiochetta          | 00242764  |
| Fernando Junior Biedermann        | 00313710  |
| Marco Antônio Chitolina da Silva  | 00308226  |
<br />

## Arquivos:
```text
trabalho_03             <-- diretorio na raiz do .zip
|-- eight_queens.py     <-- algoritmo evolutivo
|-- alegrete.py         <-- algoritmo de regessão linear
|-- ga.png              <-- imagem da melhor execução do algoritmo evolutivo
|-- relatório.pdf       <-- nosso relatório onde justificamos brevemente as escolhas dos parâmetros dos algoritmos (evolutivo e regressão)
|-- Readme.md           <-- documento de organização

```

### eight_queens.py
contém as funções utilizadas no trabalho para a implementação do algoritmo evolutivo.

### alegrete.py
contém as funções utilizadas no trabalho para a implementação do algoritmo de descida do gradiente para regressão linear.

#### parâmetros
a configuração da melhor execução do nosso algoritmo de regressão linear é: __fit(dados, 0, 0, 0.1, 200)__, ou seja, theta_0 = 0; theta_1 = 0; alpha = 0.1; número de iterações = 200. Além disso, o resultado final para theta_0 e theta_1 é 8.166405453947433e+237 e 8.232804250418806e+238 respectivamente.

### ga.png
imagem da melhor execução do algoritmo evolutivo.

#### parâmetros
a configuração dessa imagem é: __run_ga (20,200,5,0.4, True)__, ou seja, número de repetições = 20; número de indivíduos na população = 200; número de candidatos para o torneio = 5; probabilidade de mutação = 0.4; elitismo = True.

### relatório.pdf
apresenta uma breve justificativa a respeito da escolha dos parâmetros tanto para o algoritmo evolutivo, quanto para o algoritmo de regressão linear.

### read_me.md
contém os nomes dos integrantes do grupo e uma explicação sobre a estrutura do pacote de entrega.

__OBS.:__ Nenhuma biblioteca adicional precisa ser instalada.