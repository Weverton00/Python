# Try/Exception - tratar erros no código.

numero = input("Digite o número")

try:
  print(f"{numero} ainda é uma string.")
  num_int: int = int(numero)
  print(f"O dobro do número {numero} é {num_int * 2}")
except:
  print("Não é um número.")