#!/bin/env python
# -*- coding: iso-8859-1 -*-
# Verifica se um n�mero � par ou impar
#
n = input("Entre com um inteiro: ")
if type(n) == int:
    if (n % 2) == 0:
        print '%d � um par' % n
    else:
        print '%d � impar' % n
else:
    print 'Este n�mero (%s) n�o � um inteiro!' % n