# Importamos las constantes que hemos creado[cite: 1]
from config import IVA, DISCOUNT, CURRENCY

# Asignamos el valor inicial a una variable para que tampoco sea un número mágico
precio_base = 100

# Refactorizamos las operaciones sustituyendo los números por las constantes[cite: 1]
total = precio_base * IVA
final = total - (total * DISCOUNT)

# Mostramos una pequeña factura clara por pantalla[cite: 1]
print("--- FACTURA ---")
print("Precio inicial:", precio_base, CURRENCY)
print("Total con IVA:", total, CURRENCY)
print("Total a pagar (con descuento):", final, CURRENCY)