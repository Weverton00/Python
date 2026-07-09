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

# laço for / for in

word: str = "Python"

for letra in word:
  print(letra)

# for + função range(start, stop, step)

numbers_1 = range(10) #range(start=0:stop=10:step=1)
numbers_2 = range(5,10) #range(start=5:stop=10:step=1)
numbers_3 = range(5,30,2) #range(start=5:stop=10:step=2)

print(numbers_1)
print(numbers_2)
print(numbers_3)

# Palavra secreta


palavra_secreta: str = "controle"
letra_correta: str = ""
num_tentativas = 0

while True:

  letra_digitada: str = input("Digite uma letra: ")
  num_tentativas += 1

  if len(letra_digitada) > 1:
    print("Digite apenas uma letra.")
    continue

  if letra_digitada in palavra_secreta:
    letra_correta += letra_digitada

  palavra_formada: str = ""
  for letra_secreta in palavra_secreta:
    if letra_secreta in letra_correta:
      palavra_secreta += letra_secreta
    else:
      palavra_formada += "*"

  print(f"Palavra formada: {palavra_formada}")

  if palavra_formada == palavra_secreta:
    print("Você acertou!")
    print(f"A palavra secreta era: {palavra_secreta}")
    print(f"Tentativas: {num_tentativas}")
    letra_correta = ""
    num_tentativas = 0