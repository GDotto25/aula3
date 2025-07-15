entrada = input('Voce quer [Entrar ou Sair]')
entrada = entrada.lower()
print(entrada)
"""
= Atribuição
número = 10

== Comparação 
10 == 10
"""
if entrada == 'entrar':
    print("Seja bem vindo, entrou no Sistema")
elif entrada == 'sair':
    print('Você saiu do sistema...')
else:
    print('Você não digitou nem entrar e nem sair')