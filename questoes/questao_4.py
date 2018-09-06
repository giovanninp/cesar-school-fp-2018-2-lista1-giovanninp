#Nessa questão é para fazer o calculo do preço total de um aluguel
#de carros, a partir  de um valor diario(60) e o valor do Km(0.15)

#Entrada de dados:
dias = int(input('Digite o numero de dias de aluguel:\n'))
distancia = float(input('\nDigite a distância percorrida pelo carro:\n'))

#Processamento mais saída de daods:
print('O valor do aluguel foi de: ',float((dias*60)+(distancia*0.15)))