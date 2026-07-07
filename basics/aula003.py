# Try/Exception - tratar erros no código.

numero = input("Digite o número")

try:
  print(f"{numero} ainda é uma string.")
  num_int: int = int(numero)
  print(f"O dobro do número {numero} é {num_int * 2}")
except:
  print("Não é um número.")

# Ex --- 01 

number: int = int(input("Digite um número: "))

if number % 2 == 0:
  print(f"O número {number} é par.")
elif number % 2 == 1:
  print(f"O número {number} é ímpar.")
else:
  print("Insira um valor válido.")

# Ex --- 02

name: str = input("Qual é o seu nome? ")

if len(name) <= 4:
  print("O seu nome é curto.")
elif len(name) > 4 and len(name) < 6:
  print("O seu nome é normal.")
else:
  print("O seu nome é muito longo.")