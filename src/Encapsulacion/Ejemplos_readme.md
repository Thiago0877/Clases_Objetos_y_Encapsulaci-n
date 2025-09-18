# Encapsulación en Python

Este proyecto contiene ejemplos prácticos sobre **encapsulación en Python**, incluyendo:

- Atributos privados y protegidos
- Uso de `getters` y `setters`
- Validación de datos
- Herencia y sobreescritura de métodos
- Uso de acceso directo vs. encapsulación

---

## 1. Atributos privados

En Python se usan dos convenciones:

- `_atributo`: protegido, no debería usarse fuera de la clase.
- `__atributo`: privado, Python aplica **name mangling** (`_Clase__atributo`).

Ejemplo:

```python
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial, pin):
        self._titular = titular
        self._saldo = saldo_inicial
        self.__pin = pin  # realmente privado

    def validar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado
