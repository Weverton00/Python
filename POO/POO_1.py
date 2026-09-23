#Criando e inicializando as classes

class Carro:
    def __init__(self, name):
        self.name = name
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, name):
        self.name = name

class Fabricante:
    def __init__(self, name):
        self.name = name

fusca = Carro('Fusca')
volkswagen = Fabricante('Volskwagen')
fusca.fabricante = volkswagen
motor_v8 = Motor('V8 3.0')
fusca.motor = motor_v8

print(f"{fusca.name} - {fusca.motor.name} - {fusca.fabricante.name}")