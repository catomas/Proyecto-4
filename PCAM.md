# PCAM 

## 1. Partitioning
Se expresará un desglose del orden de ejecución de las diferentes tareas que ocurren durante el ciclo de vida del programa.

1. Se reciben 2 textos como entrada, el primero siendo el texto inicial y el segundo el texto final y se guardan como arreglos.
2. Se guarda cada párrafo del texto inicial en una lista junto con el texto 2. 
3. Se realiza la funcion de comparacion de texto(compareParagraph).
4. Se asignan workers que corran la funcion compareParagraph sobre cáda párrafo del texto 1, en cada núcleo de la máquina si es posible, si no, itera por los núcleos disponibles.
5. La función de comparación almacena la información de similitud de cada párrafo del texto inicial en una lista.
6. Se retorna el listado de similitudes de cada párrafo de manera ordenada.

## 2. Communication

La tarea 4 y 5 se comunican al intercambiar los datos de la información de similitud de los párrafos. Cada párrafo del texto 1 es independiente, así que no hay data races al momento de almacenar los resultados de cada párrafo.

La función 3 se comunica con la 4 para establecer la cantidad de workers a implementarse y la correspondencia entre cada worker y su párrafo a comparar.


## 3. Agglomeration

Se pueden integrar las tareas 4 y 5, ya que si no hay data races en el funcionamiento, se puede ir almacenando la información de similitud a medida que se va obteniendo, así no habría que ocupar memoria hasta el final de la ejecución para almacenar los resultados.

## 4. Mapping

Se mapea un proceso de comparación por núcleo de la máquina, así se asegura la mayor eficiencia del algoritmo LCS. Al haber integrado las tareas 4 y 5, se elimina la comunicación que plantearía esperar hasta el final de la ejecución para retornar los datos, al almacenarlos inmediatamente en lugar de retornarlos.
