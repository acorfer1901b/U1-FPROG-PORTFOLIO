#1
RATE_EUR_USD = 1.08
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Producto: {num1 * num2}")
print(f"División real: {round(num1 / num2, 2)}")
print(f"División real: {num1 / num2:.2f}")
print(f"División entera: {num1 // num2}")
print(f"Resto o módulo: {num1 % num2}")
print(f"Potencia: {num1 ** num2}")

#2
celsius = float(input("Introduce la temperatura en °C: "))
fahrenheit = (celsius * 1.8) + 32
print(f"{celsius} °C = {fahrenheit} °F")

euros = float(input("Introduce la cantidad en EUR: "))
usd = euros * RATE_EUR_USD
print(f"{euros} EUR = {usd} USD")