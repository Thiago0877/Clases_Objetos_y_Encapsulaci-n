class CuentaBancaria:
    def __init__(self, titular, saldo=0.0):
        self._titular = titular
        if saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = saldo

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = nuevo_saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False


def main():
    cuenta = CuentaBancaria("Ana García", 1000)

    print("=== Información inicial ===")
    print(f"Titular: {cuenta.titular}")
    print(f"Saldo: {cuenta.saldo}\n")

    print("=== Depósito de 500 ===")
    if cuenta.depositar(500):
        print(f"Depósito exitoso. Saldo actual: {cuenta.saldo}")
    else:
        print("Depósito fallido.")
    print()

    print("=== Retiro de 300 ===")
    if cuenta.retirar(300):
        print(f"Retiro exitoso. Saldo actual: {cuenta.saldo}")
    else:
        print("Retiro fallido.")
    print()

    print("=== Intento de retiro mayor al saldo ===")
    if cuenta.retirar(2000):
        print("Retiro exitoso.")
    else:
        print(f"Retiro fallido. Saldo actual: {cuenta.saldo}")
    print()

    print("=== Intento de establecer saldo negativo ===")
    try:
        cuenta.saldo = -100
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("=== Información final ===")
    print(f"Titular: {cuenta.titular}")
    print(f"Saldo: {cuenta.saldo}")


if __name__ == "__main__":
    main()