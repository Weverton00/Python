# Estruturas de repetições 
# While
# continue / break

contador: int = 20

while contador >= 1:
  contador -= 1

  if contador == 10:
    continue

  print(f"{contador}")

# -----------
while True:
  nome: str = input("Qual é o seu nome: ")
  print(nome)

  if nome == "sair":
    break