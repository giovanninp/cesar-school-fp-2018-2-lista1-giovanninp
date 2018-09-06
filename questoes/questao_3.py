#Essa questão é para retornar o resultado do calculo de área, diâmetro e perímetro de uma circunferencia
#a partir de um valor dado(raio).

#Foi importado algumas funções do math, para o calculo de potencias e o valor de pi.
from math import *

#Tela de boas vindas, pois foi pedido uma interface um pouco mais amigável no problema.
print('Seja bem vindo ao basic circunference calculator:\n')

#Entrada de dados:
raio = float(input('Digite o valor do raio:\n'))

#Aqui foi colocada uma estrutura de repetição, para o usuário efetuar as operações e
#decidir o fim da execução.
repeater = 1
while repeater==1:

    #Escolha da operação à ser efetuada:
    select = int(input('\nEscolha a operação desejada:\n1-Área\n2-Diâmetro\n3-Perimetro\n\n0-Sair\n'))

    #Operações + saída de dados:
    if select == 1:
        area = float(raio*pow(pi,2))
        print('\nA area do circulo será de:\n',area)
    elif select == 2:
        diametro = raio*2
        print('\nO diametro do circulo será de:\n',diametro)
    elif select == 3:
        perimetro = 2*(pi*raio)
        print('\nO perimetro do circulo será de:\n',perimetro)
    elif select == 0:
        repeater = 0
    else:
        print('\nValor invalido')

