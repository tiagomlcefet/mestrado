# -*- coding: iso-8859-1 -*-
import copy
import time
import random
import sys
arquivo = open("saida.txt","w")
possiveis_pontos={}
clientes={}
possiveis_pontos["Ponto1"]=(2, 8)
possiveis_pontos["Ponto2"]=(3, 20)
possiveis_pontos["Ponto3"]=(2, 38)
possiveis_pontos["Ponto4"]=(8, 2)
possiveis_pontos["Ponto5"]=(10, 25)
possiveis_pontos["Ponto6"]=(14, 33)
possiveis_pontos["Ponto7"]=(20, 20)
possiveis_pontos["Ponto8"]=(17, 35)
possiveis_pontos["Ponto9"]=(22, 5)
possiveis_pontos["Ponto10"]=(27, 10)
possiveis_pontos["Ponto11"]=(25, 49)
possiveis_pontos["Ponto12"]=(30, 28)
possiveis_pontos["Ponto13"]=(34, 22)
possiveis_pontos["Ponto14"]=(38, 55)
possiveis_pontos["Ponto15"]=(31, 4)
possiveis_pontos["Ponto16"]=(42, 30)
possiveis_pontos["Ponto17"]=(39, 18)
possiveis_pontos["Ponto18"]=(29, 12)
for p in range(18):
    for i in range (18):
        x1= possiveis_pontos.values()[p][0]
        y1= possiveis_pontos.values()[p][1]
        x2= possiveis_pontos.values()[i][0]
        y2= possiveis_pontos.values()[i][1]
        distancia = ((((x1-x2)**2)+((y1-y2)**2))**0.5)*10
        distancia = round(distancia, 0) 
        arquivo.write(str(distancia))
        arquivo.write(" ")
    arquivo.write('\n')
arquivo.write('\n')
arquivo.write('\n')
arquivo.write('\nDistancia Ponto x Cliente')
arquivo.write('\n')
arquivo.write('\n')
clientes["cliente1"]=(6, 9)
clientes["cliente2"]=(7, 9)
clientes["cliente3"]=(8, 11)
clientes["cliente4"]=(8, 12)
clientes["cliente5"]=(8, 20)
clientes["cliente6"]=(9, 20)
clientes["cliente7"]=(14, 22)
clientes["cliente8"]=(14, 24)
clientes["cliente9"]=(15, 24)
clientes["cliente10"]=(16, 26)
clientes["cliente11"]=(14, 28)
clientes["cliente12"]=(9, 29)
clientes["cliente13"]=(9, 30)
clientes["cliente14"]=(9, 31)
clientes["cliente15"]=(11, 33)
clientes["cliente16"]=(14, 33)
clientes["cliente17"]=(13, 35)
clientes["cliente18"]=(25, 24)
clientes["cliente19"]=(27, 22)
clientes["cliente20"]=(27, 23)
clientes["cliente21"]=(29, 25)
clientes["cliente22"]=(26, 20)
clientes["cliente23"]=(36, 22)
clientes["cliente24"]=(6, 40)
clientes["cliente25"]=(7, 40)
clientes["cliente26"]=(8, 40)
clientes["cliente27"]=(11, 45)
clientes["cliente28"]=(11, 46)
clientes["cliente29"]=(9, 47)
clientes["cliente30"]=(7, 48)
clientes["cliente31"]=(24, 31)
clientes["cliente32"]=(24, 33)
clientes["cliente33"]=(25, 36)
clientes["cliente34"]=(27, 36)
clientes["cliente35"]=(21, 40)
clientes["cliente36"]=(21, 41)
clientes["cliente37"]=(21, 42)
clientes["cliente38"]=(23, 40)
clientes["cliente39"]=(14, 51)
clientes["cliente40"]=(15, 51)       
for p in range(18):
    for i in range (40):
        x1= possiveis_pontos.values()[p][0]
        y1= possiveis_pontos.values()[p][1]
        x2= clientes.values()[i][0]
        y2= clientes.values()[i][1]
        distancia = ((((x1-x2)**2)+((y1-y2)**2))**0.5)*10
        distancia = round(distancia) 
        arquivo.write(str(distancia))
        arquivo.write(" ")
    arquivo.write('\n')
print possiveis_pontos.values()
arquivo.close()