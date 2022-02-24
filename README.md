# Récords de la Fórmula 1
Este es un calculo de recorrido en distancia media donde se registra los datos de velocidad en las pistas de F1

Con el propósito de mejorar la medición de los récords relacionados con la máxima velocidad alcanzada por un vehículo en un tramo de la pista, los directivos de la Fórmula 1 han decidido implementar radares de tramo para mantener la lista de récords actualizados.

-	Los radares de tramo funcionan colocando dos cámaras en dos puntos alejados de una pista con el fin de comprobar cuánto tiempo tarda un piloto recorrer dicho tramo. Estos radares no miden la velocidad de paso, sino el tiempo de paso representado como la velocidad media de un piloto en un trayecto con una longitud determinada.
-	Formalmente, los radares de tramo se basan en el teorema de Lagrange (también conocido como el teorema de valor medio o de Bonnet-Lagrange), el cual nos dice que dice tenemos una función continua en un intervalo cerrado, y derivable en un intervalo abierto, entonces algún punto de ese intervalo abierto la función tendrá una derivada instantánea igual a la pendiente media de la curva en el intervalo cerrado.

Aunque estos conceptos pueden asustar en un principio, su interpretación es muy simple: 

-	Si un piloto recorre un trayecto de la pista con una velocidad media es de 100 Km/h, necesariamente en algún punto del trayecto su velocidad habrá sido de 100 Km/h. 

Esto quiere decir que, si la velocidad media de un piloto supera la velocidad registrada en el récord actual, gracias al teorema anterior, sabremos que en algún punto del trayecto el piloto superó la velocidad de dicho récord. Por ejemplo, si colocamos las cámaras separadas 10 Km en un tramo cuyo récord de velocidad es de 110 Km/h, y un piloto tarda 5 minutos en ser visto por la segunda cámara, sabremos que su velocidad media ha sido de 120 Km/h, y, por lo tanto, el piloto superó el récord actual.

PROBLEMA:

Usted hace parte del equipo de desarrollo encargado de construir el software que procesará los datos registrados por las cámaras.
Su misión es crear un programa en Python que permita saber si un piloto supero un récord o no.

Entrada
El programa recibirá 3 parámetros:

•	La distancia en metros que separa dos cámaras.   
•	El actual récord de velocidad para ese trayecto en (Km/h).   
•	El tiempo en segundos que tarda el piloto en recorrer el trayecto.    

Salida
El programa imprimirá una línea con dos valores: 

•	El primer valor corresponde a la velocidad media del piloto en el trayecto evaluado en (km/h) y con un número decimal.   
•	El segundo valor indicará sí el piloto superó el récord o no.   

Se debe considerar lo siguiente:

1.	Imprimirá VELOCIDAD NORMAL si el piloto no superó el récord.
2.	Imprimirá NUEVO RECORD si se superó la velocidad registrada en el récord actual en menos de un 20%.
3.	Imprimirá ENTREVISTA si el récord fue superado en un 20% o más de la velocidad registrada en el récord actual. 

En este caso se realizará una entrevista en medios deportivos.
Debido a que los sistemas pueden fallar y registrar valores errados, (por ejemplo, indicando que el tiempo que ha tardado el piloto es negativo) en esos casos, se deberá imprimir únicamente ERROR.

Casos de prueba:

Entradas de ejemplo 

9165	110	300   
9165	110	299   
-1000	-50	-100   
12000	100	359   
12000	-100	359   
12000	100	433   
12000	100	431   
12000	100	360   
12000	100	361   

Salidas de ejemplo

110.0 VELOCIDAD NORMAL   
110.3 NUEVO RECORD    
ERROR   
120.3 ENTREVISTA   
ERROR   
99.8 VELOCIDAD NORMAL   
100.2 NUEVO RECORD   
120.0 ENTREVISTA   
119.7 NUEVO RECORD   
