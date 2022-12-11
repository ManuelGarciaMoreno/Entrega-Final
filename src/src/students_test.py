from students import * 

fichero='proyecto_1c_python_ic1_2-ManuelGarciaMoreno-main\data\students.csv'

def test_leer_fichero():
        lista=lee_students(fichero)
        print(lista[:3])
        print(lista[-3:])
        print('En total hay', len(lista), 'datos.')


def test_filtra_race():
        lista=lee_students(fichero)
        raza='race'
        razas=filtra_race(lista)
        print(razas)

def test_media_math():
        lista=lee_students(fichero)
        nota = 'group A'
        media=media_math(lista,nota)     
        print("La media de las notas es :",media)

def test_max_reading_score():
        lista=lee_students(fichero)
        raza ="group D"
        reading = max_reading_score(lista,raza)
        print("La nota mas alta del grupo D es:", reading)

def test_tupla_por_curso():
        num=int(input('Las notas de cuantas personas quieres ver:'))
        lista=lee_students(fichero)
        curso = "completed"
        tupla=tupla_por_curso(lista,num,curso)
        if num==1:
                print('La persona con la mejor nota en writing y el curso de preparacion completado es:',tupla)
        else:
                print('Las',num,'personas con las mejores notas en writing y el curso de preparacion completado son:', tupla)
def test_sep_por_publica():
        
        lista=lee_students(fichero)
        dict=sep_por_publica(lista)
        print(dict)

def test_numero_de_tuplas_de_una_clave():
        lista=lee_students(fichero)
        diccionario=numero_de_tuplas_de_una_clave(lista)
        print('numero de tuplas:',diccionario)

def test_dicc_max_min():
        lista=lee_students(fichero)
        parametro=input('Escribe "máximo" si quieres ver la nota más alta o "mínimo" si quieres ver la más baja:')     
        diccionario=dicc_max_min(lista,parametro)
        if parametro=='máximo':
                print('El grupo con la suma de puntos de la nota de writing más alta es:',diccionario)
        if parametro=='mínimo':
                print('El grupo con la suma de puntos de la nota de writing más baja es:',diccionario)
        

def test_max_nota_mates_por_g():
        lista=lee_students(fichero)
        diccionario=max_nota_mates_por_g(lista)
        print('La nota más alta de cada grupo de raza es:')
        print(diccionario)

def test_menor_nota_reading_por_g():
        n=int(input('¿Cuántas de las notas más bajas en reading quieres ver por sexo:'))
        lista=lee_students(fichero)
        diccionario=menor_nota_reading_por_g(lista,n)
        if n==1:
                print('La nota más baja es:',diccionario)
        else:
                print('Las notas más bajas son:',diccionario)

def test_grafica():
        lista=lee_students(fichero)
        diccionario=max_nota_mates_por_g(lista)
        titulo='Nota de mates'
        y=diccionario.values()
        x=diccionario.keys()
        print(grafica(titulo,x,y))

        



def main():
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
        #test_grafica()


if __name__== '__main__':
        main()