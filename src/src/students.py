from collections import namedtuple
import csv
from collections import namedtuple
from datetime import datetime, date, timedelta
from parse import *

#----------------------------------------------------------------------------------------------
# Entrega 1
#----------------------------------------------------------------------------------------------

def lee_students(fichero):

  '''
    La función "leer_students" crea una variable con una tupla en ella. 
    A la vez se le da nombre a los elementos que contiene.
    Añadimos el archivo .csv de students.
    
    Creamos varias variables:
    @param fichero: nombre del fichero csv que vamos a leer
    @return: lista de tuplas con los datos del csv.
    @rtype: (str, str, str, str, int, int, int, datetime.date, boolean)
  '''

  students=namedtuple("students", "gender,race,parental_level_of_education,lunch,test_preparation_course,math_score,reading_score,writing_score,fecha_exa,es_publica")

  with open(fichero, encoding="utf-8") as archivo:
        lector=csv.reader(archivo,delimiter=",")
        next(lector)
        lista=[]

        for gender,race,parental_level_of_education,lunch,test_preparation_course,math_score,reading_score,writing_score,fecha_exa,es_publica in lector:
            gender=str(gender)
            race=str(race)
            parental_level_of_education=str(parental_level_of_education)
            lunch=str(lunch)
            test_preparation_course=str(test_preparation_course)
            math_score=int(math_score)
            reading_score=int(reading_score)
            writing_score=int(writing_score)
            fecha_exa=parsea_fecha(fecha_exa)
            es_publica=parsea_booleano(es_publica)

            lista.append(students(gender,race,parental_level_of_education,lunch,test_preparation_course,math_score,reading_score,writing_score,fecha_exa,es_publica))

        return lista

#-----------------------------------------------------------------------------------------------
# Entrega 2
#-----------------------------------------------------------------------------------------------

'''
 La función filtra_race crea una tupla vacía a la que se le va a añadir
 aquellos elementos que recoja de la columna "race" en nuestro archivo .csv y nos la devolverá
 ordenada alfabetica

 @param lista: lista que contiene los elementos del csv
 @type lista: (str, str, str, str, int, int, int, datetime.date, boolean)
 @return: devuelve los elementos de la columna race
 @rtype: str

 '''

def filtra_race(lista):
  razas=set()
  for i in lista:
    razas.add(i.race)

  razas=list(razas)
  razas.sort()
  return razas

#---------------------------------------------------------------------------------------------

'''
La función media_math crea una lista y nos devuelve la media de los 
elementos de esta.

@param lista: lista que contiene los elementos del csv
@type lista: (str, str, str, str, int, int, int, datetime.date, boolean)
@param nota: elemento de la columna race
@type nota: str
@return: media de los elementos de la columna math_score de un elemento de la columna race
@rtype: int

'''

def media_math(lista,nota):
  suma_nota_mates=[]
  for i in lista: 
    if nota==i.race:
     suma_nota_mates.append(i.math_score)
     x=sum(suma_nota_mates)
     media=x/len(suma_nota_mates)
     return media

#-----------------------------------------------------------------------------------------------

'''
La función max_reading_score recoge la nota más alta de un grupo 
de "race" en la lista "reading" y devuelve la más alta.

@param lista: lista que contiene los elementos del csv
@type lista: (str, str, str, str, int, int, int, datetime.date, boolean)
@param raza: elemento de la columna race
@type raza: str
@return: elemento mas grande de la lista 'reading'
@rtype: int

'''

def max_reading_score(lista,raza):
  reading=[]
  for i in lista:
    if raza == i.race:
      reading.append(i.reading_score)
  reading=max(reading)
  return reading

#----------------------------------------------------------------------------------------------

'''
La función tupla_por_curso crea una lista donde se añadiran
el valor del "writing_score" de aquellas personas que 
su test_preparation_course="completed".
Devuelve el nº de notas mayores que tu quieras.

@param lista: lista que contiene los elementos del csv
@type lista: (str, str, str, str, int, int, int, datetime.date, boolean)
@param num: numero de lista que queremos ver
@type num: int
@param curso: elemento de la columna test_preparation_course
@type curso: str
@return: numero de lista de tuplas que nosotros queramos con writing_score más alto y test_preparation_course="completed"
@rtype:(str, str, str, str, int, int, int, datetime.date, boolean)

'''

def tupla_por_curso(lista,num,curso):
  tupla=[]
  for i in lista:
    if curso==i.test_preparation_course:
      tupla.append(i)
  tupla.sort(key=lambda c: c.writing_score, reverse=True)
  return tupla[:num]

#----------------------------------------------------------------------------------------------

'''
La función sep_por_publica separa a todas aquellas
personas que hayan estudiado en una escuela pública
de los que no en las listas si y no y te devuelve los tres primeros.

@param lista: lista que contiene los elementos del csv
@type lista: (str, str, str, str, int, int, int, datetime.date, boolean)
@return: diccionario con las tres primeras personas que estan en escuela pública y las tres primeras que no
@rtype:dict((str, str, str, str, int, int, int, datetime.date, boolean))
'''

def sep_por_publica(lista):
  si=[]
  no=[]
  for i in lista:
    if i.es_publica == True:
      si.append(i)
    if i.es_publica == False:
      no.append(i)
  si=si[:3]
  no=no[:3]
  diccionario={'La primera persona de la lista en escuela pública es:':si,'La primera persona de la lista en escuela privada es:':no}
  return diccionario


#----------------------------------------------------------------------------------------------
# Entrega 3
#----------------------------------------------------------------------------------------------
'''
la función numero_de_tuplas_de_una_clave crea un diccionario vacío,
luego cuenta las veces que aparece un elemento de la columna gender
y lo añade al valor del diccionario.

@param lista: lista que contiene los elementos del csv
@type lista: (str, str, str, str, int, int, int, datetime.date, boolean)
@return: devuelve el diccionario con clave un elemento de gender y valor el número de veces que aparece
@rtype: dict(str:int)
'''

def numero_de_tuplas_de_una_clave(lista):
    diccionario=dict()
    for p in lista:
        if p.gender not in diccionario.keys():
          diccionario[p.gender]= 1
        else:
          diccionario[p.gender]+= 1 
    return diccionario

#----------------------------------------------------------------------------------------------

''''
La función dicc_max_min crea un diccionario vacío al que se le añadirá como 
clave un elemento de la columna race y valor la suma de los elementos de writing_score
de cada clave. Finalmente nos devolverá la clave y valor máxima o mínima según le pidamos.

@param lista: lista que contiene los elementos del csv
@type lista: (str, str, str, str, int, int, int, datetime.date, boolean)
@param parametro: introduciremos el valor que queramos ver (máximo o mínimo)
@type parametro: str
@return: diccionario con el mayor valor o el menor
@rtype: (str,int)
'''
def dicc_max_min(lista, parametro):
  diccionario = {}
  for i in lista:
    suma = diccionario.get(i.race, 0) + i.writing_score
    diccionario[i.race] = suma

  if parametro == 'máximo':   
    max_score = max(diccionario.values())   
    max_race = [race for race, score in diccionario.items() if score == max_score]
    return (max_race, max_score)

  elif parametro == 'mínimo':    
    min_score = min(diccionario.values())
    min_race = [race for race, score in diccionario.items() if score == min_score]
    return (min_race, min_score)
    

#----------------------------------------------------------------------------------------------

'''
La función max_nota_mates_por_g crea y devuelve diccionario vacío 
cuya clave será un elemento de la columna race y su valor será
el elemeno más grande de la columna math_score.

@param lista: lista que contiene los elementos del csv
@type lista: (str, str, str, str, int, int, int, datetime.date, boolean)
@return: diccionario con el mayor elemento de math_score de cada elemento de race
@rtype: dict(str:int)
'''
def max_nota_mates_por_g(lista):
  diccionario=dict()
  for i in lista:
    if i.race in diccionario:
      if i.math_score > diccionario.get(i.race):
        diccionario[i.race]=i.math_score
    else:
      diccionario[i.race]=i.math_score  
  return diccionario

#----------------------------------------------------------------------------------------------

'''
La función menor_nota_por_g hace que un diccionario tenga como clave un elemento de la columna gender
y como valor su elemento de reading_score. Finalmente nos devolvera un diccionario con las notas más bajas 
en reading de cada genero, además te dirá de que raza es.

@param lista: lista que contiene los elementos del csv
@type lista: (str, str, str, str, int, int, int, datetime.date, boolean)
@param n: introduciremos el número de personas que queramos ver
@type n: int
@return:diccionario con las notas más bajas en reading de cada genero y su raza
@rtype:dicc(str:[int,str])
'''
def menor_nota_reading_por_g(lista,n):
  claves=(i.gender for i in lista)
  diccionario={clave:0 for clave in claves}
  for key in diccionario:
    diccionario[key]=sorted([('Con',i.reading_score,'la raza es', i.race) for i in lista if i.gender==key])[:n]
  return diccionario
