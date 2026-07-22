# Funções em Python

def greetings():
  name: str = input("Qual é o seu nome? ")
  print(f"Olá! {name}")

greetings()

# Com parametros

def soma(a: int, b: int):
  print(a + b)

soma(5, 10)

# Escopos de funções Global / Local

def local_escope():
  x: str = "valor local"
  print(x)

#print(x) X - não está definida globalmente, resultará em um erro.
country: str = ""

def global_escope():
  global country # acessando a variável global
  country: str = "brasil"
  print(country)

print(country)

#Retorno das funções

def mult(a: int, b: int):
  return a * b

multiplicao = mult(5,10)
#Passar múltiplos parâmetros def mult(*args)