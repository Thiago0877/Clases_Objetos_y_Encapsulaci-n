# Ejemplos de Encapsulación

# Atributos privados (convención con un guion bajo)
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False


# Ejemplo de uso
cuenta = CuentaBancaria("Ana García", 1000)
print("Saldo inicial (acceso directo NO recomendado):", cuenta._saldo)


# Atributos "realmente" privados (name mangling con __)
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial, pin):
        self._titular = titular
        self._saldo = saldo_inicial
        self.__pin = pin  # atributo realmente privado

    def validar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado


cuenta = CuentaBancaria("Ana García", 1000, "1234")
try:
    print(cuenta.__pin)  # genera error
except AttributeError as e:
    print("Error:", e)

print("Acceso con name mangling:", cuenta._CuentaBancaria__pin)


# Ejemplo práctico con validación de datos
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = precio


# Atributos protegidos vs privados
class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca      # protegido (convención)
        self.__modelo = modelo   # privado (name mangling)


class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self._puertas = puertas

    def info(self):
        print(f"Marca: {self._marca}")
        try:
            print(f"Modelo: {self.__modelo}")
        except AttributeError:
            print("No se puede acceder a __modelo desde la subclase")


coche = Coche("Toyota", "Corolla", 4)
coche.info()


# Getters y Setters
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Getter para nombre
    def get_nombre(self):
        return self._nombre

    # Setter para nombre
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía")

    # Getter para edad
    def get_edad(self):
        return self._edad

    # Setter para edad
    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and 0 <= nueva_edad <= 120:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un entero entre 0 y 120")


ana = Persona("Ana López", 29)
print(ana.get_nombre(), ana.get_edad())
ana.set_nombre("Ana María López")
ana.set_edad(30)
print(ana.get_nombre(), ana.get_edad())


# Ejemplo completo: Clase Producto con getters y setters
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock
        self._descuento = 0

    # Getters
    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio * (1 - self._descuento)

    def get_precio_base(self):
        return self._precio

    def get_stock(self):
        return self._stock

    def get_descuento(self):
        return self._descuento

    # Setters
    def set_nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str) or len(nuevo_nombre) == 0:
            raise ValueError("El nombre debe ser una cadena no vacía")
        self._nombre = nuevo_nombre

    def set_precio(self, nuevo_precio):
        if not isinstance(nuevo_precio, (int, float)) or nuevo_precio < 0:
            raise ValueError("El precio debe ser un número positivo")
        self._precio = nuevo_precio

    def set_stock(self, nuevo_stock):
        if not isinstance(nuevo_stock, int) or nuevo_stock < 0:
            raise ValueError("El stock debe ser un entero positivo")
        self._stock = nuevo_stock

    def set_descuento(self, nuevo_descuento):
        if not isinstance(nuevo_descuento, float) or not 0 <= nuevo_descuento <= 1:
            raise ValueError("El descuento debe ser un número entre 0 y 1")
        self._descuento = nuevo_descuento


laptop = Producto("Laptop XPS", 1200.0, 10)
print("Producto:", laptop.get_nombre())
print("Precio base:", laptop.get_precio_base())
print("Stock:", laptop.get_stock())
laptop.set_descuento(0.15)
print("Precio con descuento:", laptop.get_precio())


# Herencia con getters y setters
class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia_meses):
        super().__init__(nombre, precio, stock)
        self._garantia_meses = garantia_meses
        self._activado = False

    # Getters adicionales
    def get_garantia_meses(self):
        return self._garantia_meses

    def esta_activado(self):
        return self._activado

    # Setters adicionales
    def set_garantia_meses(self, meses):
        if not isinstance(meses, int) or meses < 0:
            raise ValueError("La garantía debe ser un entero positivo")
        self._garantia_meses = meses

    def activar(self):
        self._activado = True

    def desactivar(self):
        self._activado = False

    # Sobrescribir el setter de precio
    def set_precio(self, nuevo_precio):
        super().set_precio(nuevo_precio)
        if nuevo_precio > 1000:
            self._garantia_meses = max(self._garantia_meses, 24)


# Acceso directo sin getters/setters
class ConfiguracionSimple:
    def __init__(self):
        self.modo_debug = False
        self.max_conexiones = 100
        self.tiempo_espera = 30
