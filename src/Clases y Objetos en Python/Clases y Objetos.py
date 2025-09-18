# Ejemplos de Programación Orientada a Objetos en Python

# Ejemplo básico de clase
class Coche:
    pass

mi_coche = Coche()
coche_de_amigo = Coche()


# Constructor y atributos básicos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


ana = Persona("Ana García", 28)
juan = Persona("Juan López", 35)


# Constructor con valores por defecto
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


laptop = Producto("Laptop XPS", 1200)
teclado = Producto("Teclado mecánico", 80, 15)


# Ejemplo de validación en constructor
class Cuenta:
    def __init__(self, titular, saldo_inicial):
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self.titular = titular
        self.saldo = saldo_inicial


# Atributos de instancia y de clase
class Estudiante:
    universidad = "Universidad Autónoma"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# Métodos de instancia
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.encendido = False
        self.velocidad_maxima = 200

    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"{self.marca} {self.modelo} encendido"
        return f"{self.marca} {self.modelo} ya estaba encendido"

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            return f"{self.marca} {self.modelo} apagado"
        return f"{self.marca} {self.modelo} ya estaba apagado"

    def acelerar(self, incremento):
        if not self.encendido:
            return f"No se puede acelerar: {self.marca} {self.modelo} está apagado"
        nueva_velocidad = self.velocidad + incremento
        if nueva_velocidad > self.velocidad_maxima:
            self.velocidad = self.velocidad_maxima
            return f"Velocidad máxima alcanzada: {self.velocidad} km/h"
        self.velocidad = nueva_velocidad
        return f"Velocidad actual: {self.velocidad} km/h"

    def frenar(self, decremento):
        if self.velocidad == 0:
            return "El coche ya está detenido"
        nueva_velocidad = self.velocidad - decremento
        if nueva_velocidad < 0:
            self.velocidad = 0
            return "Coche detenido"
        self.velocidad = nueva_velocidad
        return f"Velocidad actual: {self.velocidad} km/h"


# Métodos que interactúan con atributos
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial

    def consultar_saldo(self):
        return f"Saldo actual de {self.titular}: ${self._saldo}"

    def depositar(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a depositar debe ser positiva"
        self._saldo += cantidad
        return f"Depósito de ${cantidad} realizado. Nuevo saldo: ${self._saldo}"

    def retirar(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a retirar debe ser positiva"
        if cantidad > self._saldo:
            return "Fondos insuficientes"
        self._saldo -= cantidad
        return f"Retiro de ${cantidad} realizado. Nuevo saldo: ${self._saldo}"


# Métodos estáticos y de clase
class MathUtils:
    @staticmethod
    def es_primo(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        if n in (0, 1):
            return 1
        return n * MathUtils.factorial(n - 1)