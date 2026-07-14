#Tuplas - semelhante a lista porém imutável

nomes: list = ["Max", "Gabi", "Juh"]
print(nomes)
nomes[1] = "Leah"
print(nomes)

cores: tuple = ("Azul", "Preto", "Amarelo")
print(cores)
# cores[0] = "Rosa" - Resulta em erro

#Enumerate - enumera iteráveis (índices)

nomes_enumerados = enumerate(nomes)
# print(nomes_enumerados)
# for item in nomes_enumerados:
#   print(item)

#Ex - Lista de compras

compras: list = []

while True:
  options: int = int(input("Qual ação deseja executar: 1 - Adicionar item 2 - Apagar 3 - Listar itens 4 - Sair"))

  if options == 1:
    item: str = input("Nome do item: ")
    compras.append(item)
  elif options == 2:
    indice: int = int(input("Qual índice o produto está?"))
    compras.remove(indice + 1)
  elif options == 3:
    for i, nome in enumerate(compras):
      print(i + 1, f"Produto: {nome}")
  elif options == 4:
    print("Saindo...")
    break
  else:
    print("Opção inválida.")
    continue