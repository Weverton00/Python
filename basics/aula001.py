# Isso é um comentário

"""
Isto é um Docstring - usado para descrever o que o código faz, e pode ser acessado por meio da função help().
"""

# Comandos com print

print("=" * 30) #operação com a string escrita.
print("Curso de python - aula 001")
print(10, 20, sep="*") # altera o separador padrão.
print("comandos básicos do print", end="---") # altera o final de cada comando print, o padrão \n para pular linha.

# Tipos primitivos

# Tipo Strings
linguagem = "Python" #tipagem dinâmica
area_de_atuacao: str = "automação" # tipagem forte

#Tipo Int (número inteiro)
# idade = 25
num: int = 45

#Tipo Float (número com ponto flutuante)
salario = 2499.99
preco: float = 59.99

#Tipo Boolean (true/False)
is_over_18 = True
is_open: bool = False

# ex 001

nome: str = "Max"
sobrenome: str = "Jr"
idade: int = 10
ano_nasc: int = 2026 - idade
maior_de_idade: bool = idade >= 18
altura_metros: float = 1.50

print(f"Nome: {nome}")
print(f"Sobrenome: {sobrenome}")
print(f"Idade: {idade}")
print(f"Ano de nascimento: {ano_nasc}")
print(f"É maior de idade: {maior_de_idade}")
print(f"Altura em metros: {altura_metros}")

# ____________--------------_________________---------------

# Operadores Aritméticos

# adição +
print(2 + 2)
#subtração -
print(10 - 5)
# divisão /
print(20 / 4)
# multiplicação *
print(5 * 4)
# Resto da divisão ou módulo %
print(21 % 4)
# Divisão Inteira //
print(30 // 2.5)
# Exponenciação
print(5 ** 3)

# imc
peso: float = 88.60
altura: float = 1.86
imc: float = peso / (altura * altura)
print(f"Peso: {peso} Altura: {altura} IMC = {imc:.2f}")

# --------------------___----------------_________________
# Input para pegar dados do usuário

mensagem: str = input("Digite uma mensagem: ")
print(mensagem)