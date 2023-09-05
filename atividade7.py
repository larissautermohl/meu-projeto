"""
1. Crie uma tupla com 5 dados
2. Altere a tupla para uma lista
3. Insira 2 dados extras a essa lista
4. Remova o primeiro dado da lista
5. Remova o último dado da lista
6. Faça um print com o primeiro dado da lista
7. Faça um print com a quantidade de dados da lista
8. Crie um dicionário com os seguintes dados:
    Nome, Idade, Profissão
9. Imprima somente o valor contido na chave Nome do dicionário
"""
#Item 1
tupla = (1, 2, 3, 4, 5)
#Item 2
lista = list(tupla)
#Item 3
lista.append('Rafaela')
lista.append(10)
#Item 4
lista.remove(1)
#Item 5
lista.remove(10)
# Impressão de checagem
print(lista)
#Item 6
print(lista[0])    
#Item 7
qtditens = len(lista)
print(qtditens)
#Item 8
dicionario = {'Nome': 'Rafaela', 'Idade':32, 'Profissão': 'Analista'}
#Item 9
print(dicionario['Nome'])