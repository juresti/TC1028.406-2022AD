import os
print(os.getcwd())
os.chdir("C:\\Users\\L00423103\\Desktop")
print(os.getcwd())

def leeArchivoRead(nombre):
    miArchivo = open(nombre + ".txt","r")
    contenido = miArchivo.read()
    miArchivo.close()
    
    print(contenido)
    return contenido

def leeArchivoReadline(nombre):
    miArchivo = open(nombre + ".txt","r")
    
    linea = miArchivo.readline()
    while(linea != ""):
        print(linea)
        linea = miArchivo.readline()
        
    miArchivo.close()

def leeArchivoReadlines(nombre):
    miArchivo = open(nombre + ".txt","r")
    contenido = miArchivo.readlines()
    miArchivo.close()
    
    print(contenido)
    return contenido

def escribeArchivoWrite(nombre):
    miArchivo = open(nombre + ".txt","w")
    miArchivo.write("lo que yo quiera, pero que no me de verguenza")
    miArchivo.close()
    print("Archivo escrito a disco")
    
def escribeArchivoWritelines(nombre):
    miArchivo = open(nombre + ".txt","w")
    miArchivo.writelines(["Linea 1\n","Linea 2\n","Linea 3\n","Linea 4\n"])
    miArchivo.close()
    print("Archivo escrito a disco")
