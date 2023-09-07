# Criar uma lista de frutas
frutas = ["maçã", "banana", "laranja", "uva", "morango"]

# Criar uma lista de alergias
alergias = ["kiwi", "abacate", "pêssego"]

# Inserir uma fruta da lista de frutas na lista de alergias
fruta_alergica = "uva"
alergias.append(fruta_alergica)

# Verificar se cada fruta da lista de frutas está na lista de alergias
for fruta in frutas:
    if fruta in alergias:
        print(f"Alergia! Você é alérgico a {fruta}")
    else:
        print(f"Você pode comer {fruta} sem problemas")


# Crie uma lista de frutas
frutas = ["maçã", "banana", "laranja", "uva", "morango"]

# Crie uma lista de alergias
alergias = ["kiwi", "pêssego", "abacaxi"]

# Insira uma fruta da lista de frutas na lista de alergias
fruta_alergia = "uva"
alergias.append(fruta_alergia)

# Crie um loop for para verificar se cada fruta está na lista de alergias
for fruta in frutas:
    if fruta in alergias:
        print(f"{fruta} é uma alergia!")
    else:
        print(f"{fruta} não é uma alergia.")
