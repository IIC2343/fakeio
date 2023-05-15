# FAKEIO

Este es un pequeño módulo escrito para Python 3.10 que abstrae y emula un controlador de _Input Output Port-Mapped_, a través de el método `IN(port, data)` y `OUT(port)`

## Componentes

Todos los componentes reciben como _input_ un número entero y, de tener _output_, lo entregan como `str`.

### Printer

Representa a una impresora.

Tiene solo disponible la opción de imprimir, que toma la instrucción `OUT(0, data)` y escribe `data` como un carácter ASCII al archivo `paper.txt`.

### Entropy

Representa a un generador de números aleatorios.

Tiene solo disponible la opción de recibir un número entero aleatorio a través de la instrucción `IN(1)`.

### Coprocessor

Representa a un coprocesador de números de punto flotante. Tiene dos registros, `A` y `B`, que se pueden actualizar con los comandos `OUT(6, data)` y `OUT(7, data)` respectivamente. La operación se selecciona con `OUT(8, data)`, donde `data` puede ser un entero del 0 al 3 para suma, resta, multiplicación y división respectivamente. El resultado de la operación se almacena en el registro `A` y se ejecuta con `IN(9)`.

### Magnetic tape

Representa a una cita magnética (extremadamente abstraída). Esta permite leer y escribir cantidades arbitrarias de bytes y lee de un archivo indicado por `TAPEDIR`.  Para leer, se debe elegir la cantidad de bytes a leer con `OUT(4, data)`, mover el cabezal al punto a partir del cual se quiere leer con `OUT(5, data)` y, finalmente, leer con `IN(2)`. Para escribir, basta con mover el cabezal al punto al que se quiera escribir con `OUT(5, data)` y luego escribir con `OUT(3, data)`, donde `data` es un entero cualquiera en que cada par de dígitos se interpreta como un carácter ASCII.

## Logfile

Casi todas las acciones que realiza la librería y los errores que puedan ocurrir se van escribiendo al archivo `./logs/pmio.logs`.

## Ejemplo de ejecución

En el archivo `main.py` puede encontrar un ejemplo de cómo hacer uso de este módulo para interactuar con los distintos dispositivos existentes.
