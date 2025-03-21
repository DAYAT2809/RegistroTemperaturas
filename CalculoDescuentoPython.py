def calcular_descuento(monto_total, porcentaje_descuento=10):
    """Calcula el monto del descuento basado en un porcentaje dado"""
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Precio del vestido rosado
precio_vestido = 90.85  # Precio en dólares

# Aplicar descuento por defecto (10%)
descuento_vestido = calcular_descuento(precio_vestido)
precio_final_vestido = precio_vestido - descuento_vestido

# Aplicar un descuento personalizado (20%)
descuento_vestido_20 = calcular_descuento(precio_vestido, 20)
precio_final_vestido_20 = precio_vestido - descuento_vestido_20

# Mostrar resultados
print(f"Vestido rosado de ${precio_vestido:.2f} con 10% de descuento: "
      f"Descuento de ${descuento_vestido:.2f}, total a pagar: ${precio_final_vestido:.2f}")

print(f"Vestido rosado de ${precio_vestido:.2f} con 20% de descuento: "
      f"Descuento de ${descuento_vestido_20:.2f}, total a pagar: ${precio_final_vestido_20:.2f}")
