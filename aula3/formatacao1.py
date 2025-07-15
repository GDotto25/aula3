# imc - índice massa comporea
# imc = peso / (altura ** 2) 
# imc = peso / (altura * altura)
nome = 'Dotto'
altura = 1.74
idade = 31
peso = 75
# PROCESSAMENTO

imc = peso / (altura ** 2)
print(nome, 'Tem', altura,'de altura', peso, 'pesa',peso,'seu imc é', imc)
#f-string
print(f'{nome} Tem {altura} de altura:\nPesa: {peso} \nSeu imc é = {imc:.2f}')