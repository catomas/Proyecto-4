# PCAM 

## 1. Partitioning
Se expresará un desglose del orden de ejecución de las diferentes tareas que ocurren durante el ciclo de vida del programa.

1. Se reciben 2 textos como entrada, el primero siendo el texto inicial y el segundo el texto final y se guardan como arreglos.
2. Se guarda cada párrafo del texto inicial en una lista junto con el texto 2. 
3. Se realiza la funcion de comparacion de texto en cada uno de los ítems de la lista.
4. La funcion de comparación almacena la información de similitud de cada párrafo del texto inicial en una lista.
5. Se retorna el listado de similitudes de cada párrafo de manera ordenada.

## 2. Communication

La tarea 3 y 4 se comunican al intercambiar los datos de la información de similitud de los párrafos. Cada párrafo del texto 1 es independiente, así que no hay data races al momento de almacenar los resultados de cada párrafo.

## 3. Agglomeration
WIP
## 4. Mapping
WIP
