#!/usr/bin/python

fich = open("/etc/passwd", "r")
lineas = fich.readlines()

# bien!

dicc = {}

for linea in lineas:
    conf = linea.split(":")
    
    username = conf[0]
    shell = conf[-1][:-1]
    dicc[username] = shell

    dicc[conf[0]] = conf[-1][:-1]
    
print "root", dicc["root"]
