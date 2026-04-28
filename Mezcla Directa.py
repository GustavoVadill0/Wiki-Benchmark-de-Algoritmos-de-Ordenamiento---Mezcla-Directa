import time

def mezcla_directa(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        mezcla_directa(izquierda)
        mezcla_directa(derecha)

        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

def ejecutar_proceso(archivo_entrada, archivo_salida):
    try:
        # 1. Leer los datos
        with open(archivo_entrada, 'r') as f:
            contenido = f.read()
            lista_numeros = [int(n) for n in contenido.split()]
        
        # 2. Medir el tiempo de inicio
        inicio = time.time()
        
        # 3. Ordenar
        mezcla_directa(lista_numeros)
        
        # 4. Medir el tiempo final
        fin = time.time()
        
        # Calculamos la diferencia y convertimos a milisegundos
        tiempo_ms = (fin - inicio) * 1000
        
        # 5. Guardar los resultados en el nuevo archivo
        with open(archivo_salida, 'w') as f_out:
            f_out.write(" ".join(map(str, lista_numeros)))
        
        # 6. Mostrar solo el tiempo en milisegundos
        print(f"Proceso finalizado con éxito.")
        print(f"Tiempo de ejecución: {tiempo_ms:.4f} ms")
        print(f"Los datos ordenados se han guardado en: {archivo_salida}")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_entrada}'.")
    except ValueError:
        print("Error: El archivo contiene datos que no son números enteros.")

ejecutar_proceso('datos.txt', 'datos_ordenados.txt')