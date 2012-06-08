#!/bin/env python
# -*- coding: iso-8859-1 -*-
# Verifica se um número é par ou impar
#
n = input("Entre com um inteiro: ")
if type(n) == int:
    if (n % 2) == 0:
        print '%d é um par' % n
    else:
        print '%d é impar' % n
else:
    print 'Este número (%s) não é um inteiro!' % n