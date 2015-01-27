#!/usr/bin/python

fich = open("/etc/passwd", "r")
lineas = fich.readlines()
dicc = {}

for linea in lineas:
    conf = linea.split(":")
    dicc[conf[0]] = conf[-1][:-1]
    print "Usuario: ", conf[0], "--------- Terminal: ", dicc[conf[0]]
    
print "Numero de usuarios de la maquina: ", str(len(dicc))
