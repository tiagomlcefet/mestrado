# -*- coding: UTF-8 -*-

"""
  Este exemplo mostra como efetuar uma conexão
  com o MySQL usando o módulo MySQLdb.
"""
import MySQLdb
import sys

try:
    conn = MySQLdb.connect(host='localhost', user='root', 
    passwd='0807840507@', db='rede_sem_fio')
    print "Conexão efetuada com sucesso!"
except MySQLdb.Error, e:
    print "Falha na conexão. Erro %d: %s" % (e.args[0], 
    e.args[1])
    sys.exit(1)
