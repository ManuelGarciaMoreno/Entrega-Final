from datetime import *

def parsea_fecha(cadena):
    return datetime.strptime(cadena, "%d/%m/%Y").date()

def parsea_booleano(cadena):
    res=None
    cadena=cadena.upper()
    if cadena == 'SI':
        res = True
    else: 
        cadena=='NO'
        res = False
    return res