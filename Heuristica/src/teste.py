import pylab
import sys
a = []
for i in range(120):
    a.append([])
    for j in range(90):
        a[i].append(0)
#print a
for i in a:
    print i
palavra = "Tiago"
    
matriz = [[1,4,9],[3,0,2],[7,4,2]]

saida = file('saida.txt', 'w')
saida.writelines(str(matriz) + "\n")
saida.writelines(palavra + "\n")

saida.close()
saida = file('saida.txt')