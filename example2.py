from functools import reduce
from io import open
import re
# Ruta donde crearemos el fichero, w indica escritura (puntero al principio)
#fichero = open('workfile2.txt','w')  
fichero = open('workfile2.txt','r') 
mensaje = fichero.read()
print(mensaje)
print('\n\nComienzo del procesamiento')

number = re.findall(r"\w+", mensaje, re.MULTILINE)
for w in number:
    #print(w)
    wi = int(w, base=3) + 96
    
    if wi == 123:
        print(" ", end="")
    else:
        print (chr(wi),end="") #Valor que me da
fichero.close()
