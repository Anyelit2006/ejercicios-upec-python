# Mi tercer programa en Python

# INICIALIZACIÓN DE VARIABLES
# Lista para almacenar los pesos de cada pedido
lista_pesos = []

# Acumuladores
peso_total = 0          # Acumula el peso total de todos los pedidos
total_bultos = 0        # Acumula el total de bultos

# Contadores
contador_pesos_mayores = 0   # Cuenta pedidos con peso > 50 kg
contador_norte = 0           # Cuenta pedidos de zona Norte

# Bandera booleana (inicialmente False, se activa si hay pedido prioritario)
pedido_prioritario = False

# PROGRAMA PRINCIPAL - ESTRUCTURA REPETITIVA (6 pedidos)
print("=" * 50)
print("REGISTRO DE PEDIDOS DIARIOS")
print("=" * 50)

for i in range(1, 7):  # Estructura repetitiva: se repite 6 veces
    print(f"\n--- PEDIDO N° {i} ---")
    
    # ENTRADA DE DATOS
    cliente = input("Nombre del cliente: ")
    zona = input("Zona de entrega (Norte/Centro/Sur): ")
    try:
        peso = float(input("Peso del pedido (kg): "))
    except ValueError:
        print("Entrada inválida para peso. Se asigna 0.")
        peso = 0.0
    try:
        bultos = int(input("Número de bultos: "))
    except ValueError:
        print("Entrada inválida para bultos. Se asigna 0.")
        bultos = 0
    
    # Almacenar peso en la lista (requisito de LISTA)
    lista_pesos.append(peso)
    
    # ACUMULADORES: suman valores
    peso_total += peso
    total_bultos += bultos
    
    # ESTRUCTURA SELECTIVA (condicionales)
    # Contador de pedidos con peso > 50 kg
    if peso > 50:
        contador_pesos_mayores += 1
    
    # Contador de pedidos de zona Norte
    if zona.strip().lower() == "norte":  # .lower() para aceptar mayúsculas/minúsculas
        contador_norte += 1
    
    # Bandera booleana: verificar si el pedido es prioritario
    if peso > 50 or bultos > 10:
        pedido_prioritario = True

# CÁLCULOS ADICIONALES usando la lista
if lista_pesos:
    peso_mayor = max(lista_pesos)      # Mayor valor de la lista
    peso_menor = min(lista_pesos)      # Menor valor de la lista
    promedio_peso = peso_total / len(lista_pesos)     # Promedio de pesos
else:
    peso_mayor = peso_menor = promedio_peso = 0.0

# SALIDA DE DATOS - RESUMEN FINAL
print("\n" + "=" * 50)
print("RESUMEN FINAL DE LA JORNADA")
print("=" * 50)
print(f"Lista de pesos registrados: {lista_pesos}")
print(f"Peso total acumulado: {peso_total:.2f} kg")
print(f"Total de bultos: {total_bultos}")
print(f"Cantidad de pedidos con peso > 50 kg: {contador_pesos_mayores}")
print(f"Cantidad de pedidos en zona Norte: {contador_norte}")
print(f"Peso mayor: {peso_mayor:.2f} kg")
print(f"Peso menor: {peso_menor:.2f} kg")
print(f"Promedio de peso: {promedio_peso:.2f} kg")

# Salida condicional para la bandera
if pedido_prioritario:
    print("¿Existió al menos un pedido prioritario?: SÍ")
else:
    print("¿Existió al menos un pedido prioritario?: NO")
print("=" * 50)
