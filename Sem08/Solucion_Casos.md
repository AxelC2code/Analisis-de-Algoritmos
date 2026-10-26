# Semana 8 - Análisis de Algoritmos y Estrategias de Programación  
**Curso:** Análisis de Algoritmos y Estrategias de Programación - 21527 (Remoto)  
**Actividad:** Resolución de casos prácticos Semana 8

---

## 1. Definición

Problema: dada una lista de números desordenados, encuentren simultáneamente el mínimo y el máximo usando Divide y Conquista.


Para evitar divisiones infinitas y optimizar el número de operaciones elementales, se definen dos casos base:
- **Subarreglo de un solo elemento ($izq == der$):** Cuando el rango evaluado consta de un único dato, este elemento es a la vez el mínimo y el máximo de ese segmento. No se realiza ninguna comparación entre elementos.
  $$\text{resultado} = (lista[izq], lista[izq])$$
- **Subarreglo de dos elementos ($der == izq + 1$):** Se realiza exactamente **una sola comparación** directa entre ambos valores para determinar cuál corresponde al mínimo y cuál al máximo.
  $$\text{resultado} = (lista[izq], lista[der]) \quad \text{si } lista[izq] \le lista[der]$$

---

## 2. Estrategia de División y Conquista

Siguiendo el diseño metodológico de la técnica:

1. **Dividir:** Se calcula el índice medio del segmento:
   $$medio = \lfloor (izq + der) / 2 \rfloor$$
   El arreglo se particiona conceptualmente en dos subconjuntos disjuntos de tamaño aproximado $n/2$: la mitad izquierda $[izq \dots medio]$ y la mitad derecha $[medio + 1 \dots der]$.
2. **Conquistar:** Se invocan recursivamente las llamadas para cada mitad de manera independiente:
   $$(min_{izq}, max_{izq}) = \text{resolver}(lista, izq, medio)$$
   $$(min_{der}, max_{der}) = \text{resolver}(lista, medio + 1, der)$$
3. **Combinar:** Se consolidan las soluciones parciales comparando los extremos de ambas ramas. Esto requiere únicamente **dos comparaciones elementales**:
   $$min_{global} = \min(min_{izq}, min_{der})$$
   $$max_{global} = \max(max_{izq}, max_{der})$$

---

## 3. Especificación del Retorno de Cada Llamada

Cada ejecución de la función recursiva retorna una tupla estructurada de dos elementos numéricos:
$$(minimo, maximo)$$
donde el primer valor representa el menor elemento encontrado en el subrango analizado y el segundo representa el mayor elemento de dicho intervalo.

---

## 4. Implementación en Python

Para asegurar máxima eficiencia y evitar el costo en memoria y tiempo del *slicing* de listas ($O(n)$ por copia), la implementación opera directamente sobre los índices de delimitación de la lista original:
