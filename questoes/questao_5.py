#Essa questão é relacionada à um calculo de uma possível perda de tempo
#causada pelo consumo de cigarros.

#A função ceil foi importada para fazer o arredondamento dos valores
from math import ceil

#Info de boas vindas:
print('\nBem-Vindo ao FumanteSoft\n')

#Entrada de dados:
tempFumo = int(input('Digite o numero de anos como fumante:\n'))
qtdC = int(input('Digite o numero de cigarros consumidos por dia:\n'))

#Processamento de dados:
#Calculo do numero total de cigarros consumidos:
nCig = qtdC*(365*tempFumo)
#Cálculo do número de horas perdidas totais:
horasPerdTotal: float = (nCig * 10)/60
#Cálculo do número de dias perdidos:
diasPerd = horasPerdTotal / 24
#Cálculo do número de horas perdidas:
horasPerd = horasPerdTotal % 24

#Saída de dados:
print('O tempo de vida perdido por conta do fumo foi de:\nDias: ',ceil(diasPerd),' Horas: ' , ceil(horasPerd))


