# Mi segundo programa en Python
# Inicialización de variables
peso_total = 0.0          # Acumulador de pesos
contador_mayores_50 = 0   # Contador de envíos > 50 kg
es_prioritario = False    # Bandera para envío prioritario (>100 kg)

# Estructura repetitiva (for)
for i in range(1, 6):
    # Entrada de datos
    peso = float(input("Ingrese el peso del paquete {i} (kg): "))
    
    # Acumulador
    peso_total += peso
    
    # Estructura selectiva para contar >50 kg
    if peso > 50:
        contador_mayores_50 += 1
    
    # Estructura selectiva para bandera de prioritario (>100 kg)
    if peso > 100:
        es_prioritario = True

# Salida de resultados
print("--- RESUMEN FINAL ---")
print("Peso total acumulado: {peso_total:.2f} kg")
print("Cantidad de envíos mayores a 50 kg: {contador_mayores_50}")

# Mostrar si hubo envío prioritario
if es_prioritario:
    print("¿Existió al menos un envío prioritario? Sí")
else:
    print("¿Existió al menos un envío prioritario? No")
