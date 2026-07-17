# Funções em Python

def greetings():
  name: str = input("Qual é o seu nome? ")
  print(f"Olá! {name}")

greetings()

# Com parametros

def soma(a: int, b: int):
  print(a + b)

soma(5, 10)