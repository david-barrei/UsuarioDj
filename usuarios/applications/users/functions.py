#Funciones extra de la aplicacion users
import random
import string

def code_generator(size = 6, chars= string.ascii_uppercase + string.digits):#incluye numeros o letras
    return ''.join(random.choice(chars) for _ in range(size))#Generar 6 letras aleatorias










