def min_max_divide_y_conquista(lista, izq, der):
    # CASO BASE 1: Un solo elemento
    if izq == der:
        return (lista[izq], lista[izq])

    # CASO BASE 2: Dos elementos
    if der == izq + 1:
        if lista[izq] < lista[der]:
            return (lista[izq], lista[der])
        else:
            return (lista[der], lista[izq])

    # 1. DIVIDIR
    medio = (izq + der) // 2

    # 2. CONQUISTAR
    min_izq, max_izq = min_max_divide_y_conquista(lista, izq, medio)
    min_der, max_der = min_max_divide_y_conquista(lista, medio + 1, der)

    # 3. COMBINAR
    min_final = min_izq if min_izq < min_der else min_der
    max_final = max_izq if max_izq > max_der else max_der

    return (min_final, max_final)


# Función envoltorio para invocarlo limpiamente
def encontrar_min_max(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía.")
    return min_max_divide_y_conquista(lista, 0, len(lista) - 1)


# Prueba de ejecución
if __name__ == "__main__":
    datos = [38, 27, 43, 3, 9, 82, 10, 1]
    minimo, maximo = encontrar_min_max(datos)
    print(f"Lista: {datos}")
    print(f"Mínimo: {minimo}")  # 1
    print(f"Máximo: {maximo}")  # 82