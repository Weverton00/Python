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

# Operadores Lógicos
# and (e) or (ou) not (não)

username: str = input("Digite o nome de usuário:")
password: str = input("digite a senha:")

correct_password: str = "abc123xyz456"
correct_username: str = "john"

if username == correct_username and password == correct_password:
  print("Login realizado.")
elif username == correct_username and password != correct_password:
  print("Senha Incorreta.")
else:
  print("Tente novamente.")

# in e not in - em iterações
word: str = "Probabilidade"
print("i" in word)

# Interpolação de strings
# s - string | i ou d - inteiro | f - float | x - hexadecimal


print("%s custa %f.2f" % ("Playstation", 4600.4567))
print("%d em hexadecimal é %04x" % (200, 200))

# Fatiamento de Strings [início:fim:salto]
new_word: str = "Paralelepipedo"
print(new_word[0::2])
print(new_word[7:])
print(new_word[3:8])
print(len(new_word))

# ------------------
name: str = input("Digite o seu nome: ")
age: int = int(input("Digite sua idade: "))

if name and age:
  print(f"O seu nome é: {name}.")
  print(f"O seu nome invertido é: {name[::-1]}")
  print(f"O seu nome contém espaços? {" " in name}")
  print(f"O seu nome tem {len(name)} letras.")
  print(f"A primeira letra do seu nome é: {name[0]}")
  print(f"A última letra do seu nome é: {name[-1]}")
else:
  print("Não deixe o campo 'name' vazio.")