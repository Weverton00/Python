# Estruturas de repetições 
# While
# continue / break

# contador: int = 20

# while contador >= 1:
#   contador -= 1

#   if contador == 10:
#     continue

#   print(f"{contador}")

# -----------
# while True:
#   nome: str = input("Qual é o seu nome: ")
#   print(nome)

#   if nome == "sair":
#     break

# Calculadora com while

while True:
  first_num: int = int(input("Digite um número: "))
  second_num: int = int(input("Digite outro número: "))
  operador: str = input("Digite a operação desejada: ( + adição) ( - subtração) ( * multiplicação) ( / divisão)")
  
  if operador == "+":
    print(f"resultado: {first_num + second_num}")
  elif operador == "-":
    print(f"Resultado: {first_num - second_num}")
  elif operador == "*":
    print(f"Resultado: {first_num * second_num}")
  elif operador == "/":
    print(f"Resultado: {first_num / second_num}")
  else:
    print("Insira um operador válido")

  sair = input("Deseja sair? [sim]").lower().startswith("s")

  if sair is True:
    break