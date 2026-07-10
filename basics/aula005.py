# Tipo Listas / Array mutáveis

string: str = "abcdef"
lista: list = ["Max", 20, 14.6, ["Azul", "Red", "Schwarz"]]

print(lista[0])
print(lista[3][0])

lista[3][0] = "Blue"
print(lista[3][0])

del lista[3][2]
print(lista)

lista[3].append("Schwarz")
lista.append(25) #add um elemento ao final da lista
lista.append(30)
print(lista)
ultimo_item = lista.pop() #Remove o último elemento da lista
print(ultimo_item)
print(lista)
lista[3].insert(1,"Rot") #Insere um elemento no índice específico
print(lista)

lista_2: list = [1,2,3,4,5]
lista_3: list = []
lista_3.extend(lista)
lista_3.extend(lista_2)
print(lista_3)
print(lista_2)
lista_2.clear() #Limpar lista
print(lista_2)