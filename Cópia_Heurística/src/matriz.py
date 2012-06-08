# -*- coding: UTF-8 -*-

import MySQLdb
import sys
# Exemplo de Matriz
"""
matriz = [[1,4,9],[3,0,2],[7,4,2]]
for conteudo in matriz:
    print conteudo
print "Elemento 2x3", matriz[1][2]
"""
"""
  Este exemplo mostra como efetuar uma conexão
  com o MySQL usando o módulo MySQLdb.
"""

try:
    conn = MySQLdb.connect(host='localhost', user='root', 
    passwd='0807840507@', db='rede_sem_fio')
    print "-->> Conexão efetuada com sucesso! <<--"
except MySQLdb.Error, e:
    print "Falha na conexão. Erro %d: %s" % (e.args[0], 
    e.args[1])
    sys.exit(1)
cursor = conn.cursor()
cursor.execute('SELECT * FROM pontos_de_acesso')
# Recupera o resultado
recordset = cursor.fetchall()
#Imprime o Resultado
print '## Immprimindo Tabela ##'
#for record in recordset:
#    print record
matriz = []
for linha in recordset:
    matriz.append(list(linha))
for conteudo in matriz:
    print conteudo
    
# Isso em cima pode-se fazer igual embaixo
#    matriz= [list(linha) for linha in recordset]
# Fecha a conexão

conn.close()