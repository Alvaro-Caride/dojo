# MPI\_QULACS TRAINNING - Notas para mi

## Introducción 

- Introducción Formador:
    - Álvaro Caride
    - Porque estoy yo con esto
    - Experiencia con mpi-qulacs
    - Contacto con desarrolladores -> Anotemos las dudas que surgan y podremos consultarlas
- Introcucción al curso:
    Objetivo: responder a 3 preguntas con respecto a esta aplicación. Qué es? Porque usarlo? Como se usa?
    Tres partes:
        1. Que 9-10:15
            1.1 Emulador Cuántico
            1.2 FX700
            1.3 MPI-Qulacs
                1.3.4 [qulacs git](https://github.com/qulacs/qulacs)
                1.3.5 [qulacs Docs](http://docs.qulacs.org/en/latest/)
                1.3.6 [qulacs Gui](https://qulacs-gui.github.io/qulacs-simulator/)
            - Break pequeño
        2. Porqué 10:30-11:30
            2.1 Rápido
            2.2 Flexible
            2.3 Cómodo
            2.4 Disponible
            - Breack Grande
        3. Como 12-14
            3.1 Implementación en el Cluster
            3.2 Revisión Qulacs
            3.3 Implementación Paralela
            3.4 [Dojo](https://dojo.qulacs.org/ja/latest/index.html#)
                3.4.1 Dojo 0
                3.4.2 Dojo 1
                3.4.3 Cinturón blanco-amarillo
            3.5 Migración al QS
            -Fin

### Qué es emulador cuántico.

Algoritmos cuanticos sobre hardware clásico. Emulas sobre tecnología de semiconductores matemática perteneciente a la cuántica. Problema principal: escalabilidad. Necesidad de pasar por este paso en el desarrollo de la computación cuántica por que utiliza hardware maduro y sobre este establece software en desarrollo. A nivel de algoritmos serían los mismos que se ejecutarían en una máquina cuántica real. Cuanto más real (migrable) queremos que sea nuestro algoritmo más limitaciones tenemos que poner en nuestro algoritmo. 

Necesidad de paralelismo.

### Qué es un FX700.

Los equipos Fx700 de Fujitsu implementan procesadores arm con instrucciones vectoriales de 64 bits. Son servidores que montan en dos us, 8 nodos distribuidos en 4 blades. Con procesadores A64FX de 48 cores y 32 GB de memoria y con instruciones vectoriales extendidas. Básicamente SIMD (Single Instruction Multiple Data). SVE permite diferentes tamaños del vector.

login into fx700 y cat /proc/cpuinfo y cat /proc/meminfo.

Overall Bandwith inside chip of 1TB/s for memory acces.

### Overview del cluster. ¿Dónde?

A grandes rasgos: tres entornos. HPC clásico 23 nodos con 1 TB de memoria cada uno procesadores dual socket de 32 cores cada uno. 2xFX700 que dan 16 nodos, con esto se puede llegar a emular circuitos de hasta 34 qubits. Computador cuántico de qpu superconductora de 32 qubits. Lustre y cabina de almacenamiento nfs dan soporte de almacenamiento al sistema. Está conectado a la red del cesga lo que da acceso a los home de los usuarios y que se utilicen los mismos usuarios y conexión directa con el FTIII. Forma de conexión definitiva no definida aún. 

Los Fx700 están conectados por IB y tienen además network on chip que hace que las comunicaciones sean muy rápidas.

### Que es MPI-Qulacs?

Sobre este Hardware concreto se monta Qulacs compilado especificamente para este hardware y con la campa de MPI. Memoria distribuida. 

Reqirements:   
 - GCC 11.2
 - CMake 3.24.0
 - Open MPI 4.1

```
C\_COMPILER=mpicc CXX\_COMPILER=mpic++ USE\_MPI=Yes pip install .
```

## ¿Por qué usarlo?

Disponible en el cluster. En desarrollo. Contacto con los desarrolladores [Captura del chat frikis del qulacs]. Modulo y como se utiliza en el cluster.

Rápido. Artículo de comparación. Plots más interesantes del articulo y revisar las de la presentación de Masafumi.

Contexto. Mismo orden de magnitud que el Computador Cuantico de Qubits Superconductores que tenemos abajo. En una escala de tiempos que podría ser equivalente a nivel servidor. Cálculo teórico.

Cómodo de utilizar. En su versión paralela gana potencia si perder velocidad. Muestra del multi\_cpu Device.

## ¿Cómo se utiliza?

- Conexión e implementación en el cluster

- Funciones básicas de Qulacs también disponibles en mpi-qulacs

- Implementación paralela

- Entrada en el Dojo

    - Dojo 0

    - Dojo 1

    - Cinturón Blanco-Amarillo

- Migración al Quantum Computer - Trabajo Heterogéneo.

## Fin 

- Agradecimientos

- Diapo de referencias condensada

- Contacto

---






