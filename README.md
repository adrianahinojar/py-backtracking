# Py-Backtracking
Ejercicios de backtracking en Python para resolver problemas combinatorios y de optimización.

## 1. Problema de las Mochilas

### Descripción
Dado un conjunto de objetos con diferentes pesos y dos mochilas con capacidad limitada, el objetivo es distribuir los objetos en las mochilas de manera que el peso total sea máximo sin exceder la capacidad de cada una.

### Implementación
El algoritmo recorre todas las combinaciones posibles de asignación de objetos a las mochilas utilizando **backtracking con poda** para reducir el número de exploraciones innecesarias.

### Entrada
- Un número entero `n` que indica la cantidad de objetos.
- Una lista de `n` enteros representando los pesos de los objetos.
- Dos enteros que representan la capacidad máxima de cada mochila.

### Salida
- El peso máximo que se puede lograr distribuyendo los objetos en las dos mochilas sin exceder sus capacidades.

---

## 2. Problema del Viajante de Comercio (TSP)

### Descripción
Dado un conjunto de `n` ciudades con sus coordenadas en un plano cartesiano, el objetivo es encontrar el camino más corto que visite todas las ciudades exactamente una vez y regrese a la ciudad de origen.

### Implementación
El algoritmo utiliza **backtracking con poda** para evitar caminos que superen la mejor distancia encontrada hasta el momento.

### Entrada
- Un número entero `n` que indica la cantidad de ciudades.
- `n` pares de coordenadas `(x, y)` que representan la ubicación de cada ciudad.

### Salida
- La distancia mínima del recorrido óptimo.
- La secuencia de ciudades que conforman dicho recorrido.

---

Ambos ejercicios aplican técnicas de **poda** para reducir la cantidad de combinaciones exploradas, mejorando así la eficiencia del backtracking.

