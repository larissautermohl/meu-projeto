# Solicitar a idade do usuário
idade = input("Digite sua idade: ")

# Converter a entrada do usuário para um número inteiro
idade = int(idade)

# Verificar a idade do usuário
if idade >= 18:
    print("Indivíduo possui idade mínima para dirigir")
elif idade >= 16:
    print("Indivíduo pode obter uma licença para dirigir, mas não é suficiente para dirigir sozinho")
else:
    print("Indivíduo não possui idade mínima para dirigir")
