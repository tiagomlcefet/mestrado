#!/bin/env python
# -*- coding: iso-8859-1 -*-
# primo1.py: imprime os primos
print 'Imprime os n�meros primos de 1 at� n.\n'
 
# Entra com o limite:
n = input('Entre com o limite superior para o primo: ')
 
print '\nS�o primos:'
print 1,
for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print i,
    