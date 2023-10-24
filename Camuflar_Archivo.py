#!/usr/bin/python
#-*- coding: latin-1 -*-


print("###############################################")
print("############## CAMUFLAR ARCHIVO ###############")
print("###############################################")

import os

################################################################
################################################################

def directorio_actual():
    os.getcwd()

directorio_actual()
##################################################################)
def camuflar_archivos():
    os.system("copy /b set_ap.exe + set_im.jpg set_imagen.jpg") #-> USAR ESTE COMANDO PARA CREAR LA IMAGEN.JPG

camuflar_archivos()

