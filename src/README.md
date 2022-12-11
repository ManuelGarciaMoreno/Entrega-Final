# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso 22/23)
Autor/a: \<Manuel García Moreno\>   UVUS: \<CDJ6901>

El proyecto se centra en analizar los elementos del archivo ".csv" que se encuentran recogidos en 11 columnas y 1000 filas y contiene elementos de tipo str,int y datetime.date.

## Estructura de las carpetas del proyecto

\<Carpeta "/src">: Contiene los diferentes módulos de Python que conforman el proyecto.
El archivo \<students.py> recoge el código principal donde se definen los datos a trabajar.
El archivo \<students_test.py> recoge el código necesario para realizar las pruebs sobre el código principal.
El archivo \<parse.py> añadimos la función 'def parsea_fecha(cadena)' que convertiremos en datetime y la función 'def parsea_booleano(cadena)' que convertiremos en booleano.
El archivo \<grafica.py> recoge el código donde se crea la gráfica de nuesto proyecto.

\<Carpeta "/data">: Contiene el dataset o datasets del proyecto
En el archivo students.csv se en cuentran los datos sobre los que se va a trabajar.
    
## Estructura del *dataset*

**gender** : de tipo <str>, representa el género del estudiante
**race_or_ethnicity** : de tipo <str>, representa el grupo(A,B,C,D o E).
**parental_level_of_education** : de tipo <str>, representa el nivel de educación de los padres.
**test_preparation_course** : de tipo <str>, representa el curso de preparación para los exámenes.
**math_score** : de tipo <int>, representa la nota sacada en matemáticas. 
**reading_score** : de tipo <int>, representa la nota sacada en lectura.
**writing_score** : de tipo <int>, representa la nota sacada en escritura.
**fecha_exa** : de tipo <datetime.date>, representa el día,mes y año en el que se hizo el examen.
**es_publica** : de tipo <boolean>, representa si la escuela es pública o no.

## Tipos implementados

La nametuple que defino en el proyecto es:namedtuple("students", "gender,race_or_ethnicity,parental_level_of_education,lunch,test_preparation_course,math_score,reading_score,writing_score,fecha_exa,es_publica") con el fin de recoger en ella las diferentes columnas del csv; los tipos son: (str, str, str, str, int, int, int, datetime.date, boolean)

## Funciones implementadas
Han sido implementadas 11 funciones, separadas por los bloques explicados a continuación:

 ## <modulo students>

 ## Primera Entrega
**<leer_fichero(fichero)>**:lee los datos del fichero csv y devuleve una lista de tuplas.

 ## Segunda Entrega
**<filtra_race(lista)>**: Crea una tupla donde añade los elementos de la columna race, convierte la tupla en una lista para ordenarla después alfabéticamente y finalmente devolverla.

**<media_math(lista,nota)>**: Crea una lista llamada suma_nota_mates donde añadira los valores de la columna math_score de un determinado elemento de race, sumará todos los valores y finalmente devolverá la media.

**<max_reading_score(lista,raza)>**: Crea una lista llamada reading donde añadira los elementos de la columna reading_score de una determinada raza, finalmente devolvera el valor más alto añadido a la lista.

**<tupla_por_curso(lista,num,curso)>**: Crea una lista llamada tupla donde añadira a las personas cuyo elemento de la columna test_preparation_course sea 'completed', entonces las ordenará de mayor según su writing_score y te devolvera el numero de tuplas que tu le pidas.

**<sep_por_publica(lista)>**: Crea dos listas vacías llamadas si y no; si el elemento de la columna es 'SI', es decir es True, se añadirá a la lista si, en el caso contrario, sea False, se añadira a la lista no. Finalmente nos devolverá un diccionario que recogera la primera fila del csv que cumpla cada condición.

 ## Tercera Entrega
**<numero_de_tuplas_de_una_clave(lista)>**: Crea un diccionario vacío donde cada clave del dicccionario será un elemento de la columna gender, y por cada vez que aparezca, su valor aumentará en 1.

**<dicc_max_min(lista,parametro,raza)>**: Crea un diccionario vacío al que se le va a añadir como clave los elemenos de la columna race y valor la suma de sus respectivos elementos de la columna writing_score. Si nuestra variable parametro es igual a 'máximo' nos devolvera el grupo con mayor puntuación, si parametro es igual a 'mínimo' nos devolverá el grupo con menor puntuación.

**<max_nota_mates_por_g(lista)>**: Crea un diccionario vacío donde las claves seran cada elemento de la columna race y el valor sera un elemento de la columna math_score, que se ira sustituyendo cuando el valor que lea sea mayor que el anterior. Finalmente nos devolverá el valor mas alto de la columna math_score de cada elemento de la columna race.

**<menor_nota_reading_por_g(lista,n)>**: El diccionario que nos va a devolver esta funcion tendrá como clave un elemento de la columna gender, y su valor nos mostrará el número de filas de la persona con el elemento de la columna reading_score más bajo.

**<grafica(titulo,x,y)>** (en <modulo grafica>)

 ## <modulo parse>
**<parsea_booleano(cadena)>**: le damos una cadena del tipo str nos la devuelve como los valores booleanos True, cuando valga SI y False, cuando valga NO.
**<parsea_fecha(cadena)>**: le damos una cadena del tipo fecha en formato dia/mes/año (%d/%m/%Y) y nos la devuleve como una cadena.

## <test student_test>
 **<main>**: es la función principal que llama a las siguientes funciones:
    test_leer_fichero()
    test_filtra_race()
    test_media_math()
    test_max_reading_score()
    test_tupla_por_curso()
    test_sep_por_publica()
    test_numero_de_tuplas_de_una_clave()
    test_max_nota_mates_por_g()
    test_dicc_max_min()
    test_menor_nota_reading_por_g()
    test_grafica()







