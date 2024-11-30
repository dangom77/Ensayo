# buscador_secuencias.py

# Daniel Gomez
# 30/11/2024

## Descripción

Este script de Python busca una secuencia específica de nucleótidos o aminoácidos dentro de un archivo multifasta. 

**Funcionalidades:**

* **Lectura de archivos multifasta:** Lee archivos en formato FASTA, con secuencias en nucleotidos o aminoácidos. Es importante aclarar que solo funciona con archivos cuya extensión sea .fasta, si tiene archivos con extensión .fna o .faa, sugiero renombrarlos, por ejemplo. Archivo_faa.fasta o Archivo_fna.fasta para no generar errores.
* **Búsqueda de secuencias:** Busca la secuencia específica proporcionada dentro de las secuencias del archivo.
* **Salida:** Devuelve una lista de los encabezados (">") de las secuencias que contienen la secuencia buscada.

## Cómo utilizar

1. **Clonar el repositorio:** Si el código se encuentra en un repositorio Git, clona el repositorio en tu máquina local. Puedes descargar los 2 archivos .fasta de prueba.
2. **Ejecutar el script:** Abre una terminal y ejecuta el script utilizando Python. A continuación, el código solicitará la ruta al archivo multifasta y la secuencia que desea buscar.
