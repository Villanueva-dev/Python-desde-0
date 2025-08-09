# Sesión de Refuerzo   Versatilidad Extrema: Con Python puedes hacer de todo: desarrollo web (Django, Flask), análisis de datos (Pandas, NumPy), inteligencia artificial (TensorFlow, PyTorch), scripting para automatizar tareas, videojuegos y mucho más. Aprender Python abre un mundo de posibilidades.

---

## El Poder de Python en el Mundo Real: ¿Qué se ha construido con él?

Python no es solo un lenguaje para aprender; es la columna vertebral de algunas de las aplicaciones y servicios más grandes del mundo. Aquí tienes ejemplos reales y documentados:

*   **Instagram:** La popular red social procesa y sirve millones de usuarios utilizando Python en su backend. Su framework principal es Django, que está escrito en Python.
    *   **Fuente:** Blog de Ingeniería de Instagram. En su artículo "Web Service Efficiency at Instagram with Python", explican cómo usan Python y cómo lo han optimizado para su escala masiva.
    *   **Enlace:** `https://instagram-engineering.com/web-service-efficiency-at-instagram-with-python-4976d075e3c`

*   **Spotify:** El gigante del streaming de música utiliza Python extensamente para el análisis de datos y para sus servicios de backend. La rapidez de desarrollo que ofrece Python les permite crear y probar nuevas funcionalidades constantemente.
    *   **Fuente:** Blog de Ingeniería de Spotify. En el artículo "How we use Python at Spotify", detallan su uso para servicios de backend y análisis, mencionando que tienen más de 6000 servicios en Python.
    *   **Enlace:** `https://engineering.atspotify.com/2013/03/how-we-use-python-at-spotify/`

*   **Dropbox:** El servicio de almacenamiento en la nube comenzó con Python. El cliente de escritorio original y gran parte de su infraestructura del lado del servidor fueron escritos en Python, demostrando su capacidad para crear aplicaciones de escritorio y sistemas distribuidos robustos.
    *   **Fuente:** Blog de Tecnología de Dropbox. En este artículo, "Our journey to type checking 4 million lines of Python", no solo confirman su uso masivo de Python, sino que explican los desafíos técnicos que han superado.
    *   **Enlace:** `https://dropbox.tech/application/our-journey-to-type-checking-4-million-lines-of-python`

*   **Netflix:** Utilizan Python en casi todas las áreas de su negocio. Desde el análisis de datos para las recomendaciones de contenido, hasta la automatización de la seguridad, la monitorización y la infraestructura de su red de entrega de contenido (CDN).
    *   **Fuente:** Blog de Tecnología de Netflix. En "Python at Netflix", describen cómo el lenguaje les permite a sus ingenieros moverse rápido y resolver problemas complejos en diferentes dominios.
    *   **Enlace:** `https://netflixtechblog.com/python-at-netflix-bba45dae649e`

*   **Google:** Desde sus inicios, Google ha utilizado Python. Su política interna es "Python donde podamos, C++ donde debamos". Se usa en innumerables sistemas internos, en la infraestructura de YouTube y en muchas de sus APIs.
    *   **Fuente:** Peter Norvig (Director de Investigación en Google). En varias charlas y escritos, ha documentado el uso extensivo de Python en Google. La propia página de carreras de Google menciona Python como un lenguaje clave.
    *   **Enlace:** `https://www.youtube.com/watch?v=sPi6wH8b4s8` (Charla de Peter Norvig sobre la IA y el rol de Python en Google).

Estos ejemplos demuestran que aprender Python no solo te da una base sólida en programación, sino que te abre las puertas a trabajar en proyectos de alto impacto a nivel mundial.

## Introducciónde Python desde 0

## Datos Curiosos y Por Qué Python es Genial para Empezar

Antes de sumergirnos en el código, aquí tienes algunos datos interesantes sobre Python que quizás no conocías y que explican su popularidad, especialmente entre los principiantes:

**Datos Curiosos:**

*   **¿Nombre de serpiente? No, de comedia:** A diferencia de lo que muchos creen, el nombre "Python" no proviene de la serpiente, sino del grupo de comedia británico **Monty Python**. Guido van Rossum, su creador, era un gran fan.
*   **El Zen de Python:** Python tiene una filosofía de diseño resumida en "El Zen de Python" (escribe `import this` en un intérprete de Python para leerlo). Son 19 aforismos que guían la escritura de código simple y legible, como "Bello es mejor que feo" y "Simple es mejor que complejo".
*   **Más antiguo que Java:** Python fue concebido a finales de los 80 y su implementación comenzó en diciembre de 1989. Su primera versión pública fue en 1991, lo que lo hace más antiguo que otros lenguajes populares como Java (lanzado en 1995).
*   **Baterías Incluidas:** Python es conocido por su filosofía de "baterías incluidas", refiriéndose a su enorme librería estándar que viene con módulos para realizar todo tipo de tareas (manejar correos, crear servidores web, etc.) sin necesidad de instalar paquetes externos.

**¿Por Qué es tan Efectivo para Aprender?**

*   **Sintaxis Limpia y Legible:** El código Python se parece mucho al inglés, lo que facilita su lectura y comprensión. No utiliza llaves `{}` para delimitar bloques, sino la indentación (espacios), obligando a escribir código más ordenado visualmente.
*   **Menos Código, Más Acción:** Python permite expresar conceptos complejos con menos líneas de código en comparación con otros lenguajes. Esto permite a los principiantes enfocarse en la lógica de la programación en lugar de enrevesadas reglas de sintaxis.
*   **Comunidad Gigante y Solidaria:** Al ser tan popular, existe una comunidad global inmensa. Esto se traduce en una cantidad casi infinita de tutoriales, foros de ayuda (como Stack Overflow), librerías y frameworks para casi cualquier cosa que imagines.
*   **Versatilidad Extrema:** Con Python puedes hacer de todo: desarrollo web (Django, Flask), análisis de datos (Pandas, NumPy), inteligencia artificial (TensorFlow, PyTorch), scripting para automatizar tareas, videojuegos y mucho más. Aprender Python abre un mundo de posibilidades.

## Introducción

El objetivo de esta sesión es repasar los conceptos básicos y fundamentales de Python de una manera práctica. La mejor forma de aprender a programar es programando, así que nos enfocaremos en ejercicios que te ayudarán a aplicar la teoría.

## Temario

1.  **Variables y Tipos de Datos**
    *   Qué son las variables y cómo se usan.
    *   Tipos de datos básicos: `int`, `float`, `str`, `bool`.
    *   Conversión de tipos de datos.
2.  **Operadores**
    *   Aritméticos: `+`, `-`, `*`, `/`, `%`, `**`, `//`
    *   De comparación: `==`, `!=`, `>`, `<`, `>=`, `<=`
    *   Lógicos: `and`, `or`, `not`
3.  **Estructuras de Datos**
    *   Listas: Creación, acceso, modificación, métodos.
    *   Tuplas: Creación, acceso.
    *   Diccionarios: Creación, acceso, modificación, métodos.
4.  **Control de Flujo**
    *   Condicionales: `if`, `elif`, `else`.
    *   Bucles: `for`, `while`.
5.  **Funciones**
    *   Definición y llamada de funciones.
    *   Parámetros y valores de retorno.

---

## Ejercicios Prácticos

### Ejercicio 1: Calculadora de Propinas

**Conceptos:** Variables, tipos de datos (float, int), operadores aritméticos, entrada/salida.

**Enunciado:**
Crea un programa que calcule la propina a dejar en un restaurante. El programa debe solicitar al usuario el total de la cuenta y el porcentaje de propina que desea dejar. Luego, debe imprimir el monto de la propina y el total a pagar.

**Pasos:**
1.  Pide al usuario que ingrese el total de la cuenta y guárdalo en una variable.
2.  Pide al usuario que ingrese el porcentaje de propina que desea dejar y guárdalo en otra variable.
3.  Calcula el monto de la propina.
4.  Calcula el total a pagar (cuenta + propina).
5.  Imprime los resultados de forma clara.

### Ejercicio 2: Adivina el Número

**Conceptos:** Bucles (`while`), condicionales (`if`, `elif`, `else`), entrada/salida, uso de la librería `random`.

**Enunciado:**
Crea un juego en el que la computadora elige un número al azar entre 1 y 100, y el usuario tiene que adivinarlo. El programa debe dar pistas al usuario si su número es mayor o menor que el número secreto. El juego termina cuando el usuario adivina el número.

**Pasos:**
1.  Importa la librería `random`.
2.  Genera un número aleatorio entre 1 y 100 y guárdalo en una variable.
3.  Inicia un bucle que se repita hasta que el usuario adivine el número.
4.  Dentro del bucle, pide al usuario que ingrese un número.
5.  Compara el número del usuario con el número secreto y da una pista (`"Demasiado alto"`, `"Demasiado bajo"`).
6.  Si el usuario adivina, imprime un mensaje de felicitación y termina el bucle.

### Ejercicio 3: Contador de Palabras

**Conceptos:** Cadenas de texto (strings), métodos de strings (`split`), diccionarios, bucles (`for`).

**Enunciado:**
Escribe un programa que cuente la frecuencia de cada palabra en una frase dada por el usuario.

**Pasos:**
1.  Pide al usuario que ingrese una frase.
2.  Convierte la frase a minúsculas para evitar contar la misma palabra dos veces (ej. "Hola" y "hola").
3.  Divide la frase en palabras.
4.  Crea un diccionario vacío para almacenar la frecuencia de las palabras.
5.  Recorre la lista de palabras y cuenta la frecuencia de cada una, almacenando el resultado en el diccionario.
6.  Imprime el diccionario con la frecuencia de cada palabra.

### Ejercicio 4: Lista de Tareas (To-Do List)

**Conceptos:** Listas, bucles (`while`), condicionales, funciones, entrada/salida.

**Enunciado:**
Crea un programa de línea de comandos para gestionar una lista de tareas. El programa debe permitir al usuario:
*   Añadir una tarea a la lista.
*   Ver todas las tareas de la lista.
*   Marcar una tarea como completada (eliminarla de la lista).
*   Salir del programa.

**Pasos:**
1.  Crea una lista vacía para almacenar las tareas.
2.  Inicia un bucle `while` que se ejecute indefinidamente hasta que el usuario decida salir.
3.  Dentro del bucle, muestra un menú de opciones al usuario.
4.  Pide al usuario que elija una opción.
5.  Según la opción elegida, realiza la acción correspondiente (añadir, ver, eliminar, salir).
6.  Utiliza funciones para organizar el código (ej. `agregar_tarea()`, `ver_tareas()`, etc.).
