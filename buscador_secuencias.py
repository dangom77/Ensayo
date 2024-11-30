""""""
#Este código busca secuencias específicas de ntds o aa en archivos multifasta.

#Autor: Daniel Gómez
#Fecha: 30-11-2024
""""""

def buscar_secuencia(archivo, secuencia):
    """
    Busca una secuencia de interés en un archivo multifasta

    Parámetros:
    - archivo: Ruta del archivo multifasta
    - secuencia: Secuencia de nucleótidos a buscar

    Retorna: Lista de encabezados de secuencias que contienen la secuencia
    """
    secuencias_encontradas = []

    # Abrir el archivo multifasta
    with open(archivo, 'r') as f:
        encabezado = ""
        secuencia_actual = ""

        # Leer el archivo línea por línea
        for linea in f:
            # Quitar espacios al inicio y final
            linea = linea.strip()

            # Si la línea es un encabezado
            if linea.startswith('>'):
                if encabezado and secuencia_actual:
                    if secuencia.upper() in secuencia_actual.upper():
                        secuencias_encontradas.append(encabezado)

                # Guardar nuevo encabezado
                encabezado = linea
                # Reiniciar secuencia actual
                secuencia_actual = ""

            # Si es una línea de secuencia
            else:
                # Agregar la línea a la secuencia actual
                secuencia_actual += linea

        # Verificar la última secuencia
        if encabezado and secuencia_actual:
            if secuencia.upper() in secuencia_actual.upper():
                secuencias_encontradas.append(encabezado)

    return secuencias_encontradas


# Ejecución directa
archivo = input("Escribe la ruta del archivo multifasta: ").strip()
secuencia = input("Escribe la secuencia de nucleótidos a buscar: ").strip()

# Buscar la secuencia
resultados = buscar_secuencia(archivo, secuencia)

# Mostrar resultados
print("\nSecuencias que contienen la secuencia:")
for encabezado in resultados:
    print(encabezado)
print(f"\nTotal de secuencias encontradas: {len(resultados)}")