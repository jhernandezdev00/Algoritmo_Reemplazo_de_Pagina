# Algoritmo_Reemplazo_de_Pagina
<h4>En sistemas operativos que utilizan paginación para el manejo de memoria el reemplazo de páginas es un proceso que se utiliza en sistemas operativos para administrar la memoria física y virtual en un dispositivo de almacenamiento. El objetivo principal de este algoritmo es determinar qué página de memoria virtual debe ser eliminada cuando la memoria física está llena y se necesita espacio para cargar una nueva página.
<br>
Existen varios algoritmos de reemplazo de páginas, como el algoritmo de reemplazo de página menos recientemente utilizado (LRU), el algoritmo de reemplazo de página más antiguo (FIFO) y el algoritmo de reemplazo de página óptimo (OPT). Cada algoritmo tiene sus propias ventajas y desventajas y se selecciona en función de los requisitos específicos del sistema.
<br>
Este algoritmo utiliza el método de reemplazo por medio de algoritmo FIFO, LRU y Segunda oportunidad, que a continuación se detallaran brevemente su funcionamiento.
</h4><br>

<h3><i>Primero en entrar, primero en salir (FIFO, First In, First Out)</i></h3>
<h4>Este método implica que el sistema operativo ordene las páginas cargadas en orden cronológico y, al necesitar espacio, pueda fácilmente seleccionar la página más antigua para ser eliminada. Se utiliza una cola para mantener un registro de las páginas cargadas, y cada nueva página se agrega al final de la cola. Aunque las colas FIFO son simples y fáciles de entender, no funcionan bien en la práctica debido a la Anomalía FIFO o Anomalía de Belady. Esta anomalía se refiere a la situación en la que, en ocasiones, un sistema con menos marcos de página puede tener menos fallos de página que un sistema con más marcos de página. Esto se debe a que una página muy utilizada puede ser eliminada de la memoria solo porque es la más antigua.</h4>

<br>

<h3><i>Menos Usada Recientemente (Least Recently Used, LRU)</i></h3>
<h4>El algoritmo "Menos usada recientemente" difiere del algoritmo "No usada recientemente" porque, en lugar de solo tener en cuenta el tiempo desde que se pusieron en cero los bits de referencia de las páginas, busca proporcionar un comportamiento casi óptimo al observar las páginas menos utilizadas recientemente, que estadísticamente tienen menos probabilidades de ser utilizadas de nuevo.

Aunque este algoritmo es efectivo en teoría, es costoso de implementar debido a que requiere muchos recursos. Hay varios métodos que buscan mantener bajos los costos de implementación y lograr un buen rendimiento. Uno de ellos consiste en tener una lista enlazada y ordenada de todas las páginas en memoria, donde la página menos utilizada recientemente se encuentra al final de la lista y la más utilizada recientemente al principio. El costo alto de este método se debe a que cada vez que se hace referencia a una página, se debe mover en la lista, lo que consume mucho tiempo.

Otro método requiere soporte de hardware y consiste en tener un contador que se incrementa en cada instrucción del CPU. Cada vez que se accede a una página, gana el número del contador en ese momento. Cuando una página debe ser retirada de la memoria, simplemente se busca la página con el menor número, que es la que se utilizó hace más tiempo. Sin embargo, en la actualidad, no existen contadores lo suficientemente grandes para implementar este método. Debido al alto costo del algoritmo "Menos usada recientemente", se proponen algoritmos similares que permiten implementaciones menos costosas.</h4>

<br>

<h3><i>Segunda oportunidad (Reloj)</i></h3>
<h4>Se trata de una pequeña modificación al algoritmo FIFO que funciona mejor que el FIFO original. Cuando se necesita sacar una página, en lugar de eliminar la primera de la cola, se verifica el valor de un bit de referencia. Si el bit está fijado en 1, se cambia a 0 y se mueve al final de la cola, actualizando su tiempo de carga como si fuera una página nueva. Esto le da una segunda oportunidad. Si el bit está sin fijar (en 0), la página se saca de la memoria. Cada vez que se accede a una página, la MMU fija su bit de referencia a 1. Este método requiere soporte de hardware para el bit de referencia.</h4>

<br>

___

<h4>Este algoritmo permite al usuario ingresar un listado de procesos numéricos insertando el orden de como serán atendido o permite ejecutar un ejemplo pre cargado para demostrar como realiza la paginación de procesos cada método además de permitir ingresar cuantos marcos o espacio de memoria tiene para atender cada solicitud, como resultado muestra como se van realizando los cambios, el total de fallos que se generaron, la eficiencia del cada algoritmo y gráfica como se van realizando los cambios.</h4>
<br>
<h4>Ahora veremos una visualización de como funciona el algoritmo:</h4>
<h4>Para este ejemplo, usaremos los valores cargados en el algoritmo para ejecutar, el algoritmo solicita los datos anteriormente descritos y comienza el proceso mostrando los datos que aparecen al principio de la imagen e inicia el proceso, realiza la carga de procesos de acuerdo al algoritmo seleccionado.</h4>

<img src="Source\Imagen_1.png">
<img src="Source\Imagen_2.png">
<img src="Source\Imagen_3.png">
<img src="Source\Imagen_4.png">
<br>
<h4>Una vez terminado, muestra el número de fallos de página y muestra un resumen de los reemplazos realizados en cada carga</h4>
<br>
<img src="Source\Imagen_5.png">
<br>
<h4>Además, grafica una emulación de como se realizaron los cambios</h4>
<br>
<img src="Source\Imagen_6.png">