# Condicionais - if else

is_on: str = input("Está ligado? (yes/no)")

if is_on == "yes":
  print("Está ligado")
elif is_on == "no":
  print("Está desligado")
else:
  print("Digite algo válido")

# operadores 

idade: int = int(input("Digite sua idade:"))

if idade < 18:
  print("Você não é maior de idade.")
elif idade >= 18:
  print("Você é maior de idade.")
else:
  print("Digite um valor válido.")