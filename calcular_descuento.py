# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    return monto_total * (porcentaje_descuento / 100)

# Porcentaje fijo para todas las compras
porcentaje = 10

# Lista de montos de compra
compras = [150.00, 500.00, 80.00, 1200.00]

# Encabezado de resultados
print("Resumen de compras con descuento del 10%:\n")
print(f"{'Compra':<10}{'Monto Total':<15}{'Descuento':<15}{'Monto Final':<15}")

# Procesar cada compra
for i, monto in enumerate(compras, start=1):
    descuento = calcular_descuento(monto, porcentaje)
    monto_final = monto - descuento
    print(f"{i:<10}${monto:<14.2f}${descuento:<14.2f}${monto_final:<14.2f}")
