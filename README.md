# FAKEIO

Esta es un pequeño módulo escrito para Python 3.10 que abstrae y emula un controlador de Input Output Port-Mapped, a través de el método `IN(port, data)` y `OUT(port)`

## Componentes

Todos los componentes reciben como input un entero y de tener output, lo entregan como str.

### Printer

Representa a una impresora.

Tiene solo disponible la opción de imprimir, que toma la instrucción `OUT(0, data)` y escribe `data` como un carácter ASCII al archivo `paper.txt`.

### Entropy

Representa a un generador de números aleatorios.

Tiene solo disponible la opción de recibir un entero aleatorio, a través de la instrucción `IN(1)`.

### Coprocessor

Representa a un coprocesador de números de punto flotante. Tiene dos registros, `A` y `B`, que se pueden actualizar con los comandos `OUT(6, data)` y `OUT(7, data)` respectivamente. La operación se selecciona con `OUT(8, data)`, donde `data` puede ser un entero del 0 al 3 para suma, resta, multiplicación y división. El resultado de la operación se almacena al registro `A` y se ejecuta con `IN(9)`.

### Magetic tape

Representa a una cita magnética (extremadamente abstraída). Esta permite leer y escribir cantidades arbitrarias de bytes y lee de un archivo indicado por `TAPEDIR`.  Para leer, se debe elegir la cantidad de bytes a leer con `OUT(4, data)`, mover el cabezal al punto a partir del cual se quiere leer con `OUT(5, data)` y finalmente leer con `IN(2)`. Para escribir, basta con mover el cabezal al punto al que se quiera escribir con `OUT(5, data)` y luego escribir con `OUT(3, data)`, donde `data` es un entero cualquiera en que cada par de dígitos se interpreta como un carácter ASCII.