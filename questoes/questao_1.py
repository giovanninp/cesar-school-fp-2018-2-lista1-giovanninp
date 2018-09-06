#Essa questão é para o calculo de aumento, a partir de um salario inicial e um aumento em %.

#Entrada de dados:
salario = float(input('Digite o salario:\n'))
aumentoP = float(input('Digite o aumento em porcentagem:\n'))

#Processamento de dados:
salarioFinal = (((salario/100)*aumentoP)+salario)

#Saída de dados
print('O salario final será de:\n',salarioFinal)