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
  country = "brasil"
  print(country)

print(country)

#Retorno das funções

def mult(a: int, b: int):
  return a * b

multiplicao = mult(5,10)
#Passar múltiplos parâmetros def mult(*args)

#Exercícios

def mult_nums(*args: int):
  total = 1
  for num in args:
    total *= num
  return total

mu = mult_nums(1,2,3,4,5)
print(mu)

def par_ou_impar(num: int):
  if num % 2 == 0:
    return f"Número {num} é par."
  return f"Número {num} é ímpar."

print(par_ou_impar(5))
print(par_ou_impar(2))
print(par_ou_impar(10))
print(par_ou_impar(93))
