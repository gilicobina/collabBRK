
# -*- Coding: UTF-8 -*-
#coding: utf-8
from Dado import Dados
from sys import argv
import numpy as np
from BRKGA import BRKGA
import glob	
import os
import datetime





#Tamanho da populacao
TAM_POP = 100
#Criterio de parada
MAX_GEN = 1000
#Taxa da populacao que estara na populacao elite
TX_ELITE = 0.6
#Taxa de cruzamento(Probabilidade de um filho herdar o gene do seu pai de elite)
TX_CROSS = 0.6
#Taxa de mutacao(Numero de mutantes criados)
TX_MUT = 0.17


#dados = Dados('../dados_atribuicao/'+argv[1], argv[2])
#dados = Dados('../dados_atribuicao/assign4.txt')
x = 'trial/'
sol = 'solucao/'
#dados = Dados('trial/'+argv[1])
# Create directory

 
# Create target Directory if don't exist
if not os.path.exists(sol):
    os.mkdir(sol)
    print("Directory " , sol ,  " Created ")
else:    
    print("Directory " , sol ,  " already exists")

listaArq = glob.glob(x+'*.txt')

for arq in listaArq:
	salve = arq.replace(x,'')
	salve = salve.replace('.txt','')
	if os.path.exists(sol+salve+'_solu.csv'):
		nlinhas = sum(1 for line in open(sol+salve+'_solu.csv'))
		print nlinhas
	else:
		nlinhas = 0 
	if nlinhas<10:
		for i in range(10-nlinhas):

			print arq
			dados = Dados(arq)
			matriz = np.array(dados.matriz)
			

			atribuicao = BRKGA(dados, TAM_POP,MAX_GEN, TX_CROSS, TX_MUT, TX_ELITE)
			atribuicao.start()
			atribuicao.join()
					
			
			
			with open(sol+salve+'_solu.csv','a') as z: 

				z.write(str(atribuicao.solucao))
				z.write('\n')
			z.close()
			now = datetime.datetime.now()
			now = str(now.strftime("%Y-%m-%d %H:%M"))
			#os.chdir('/solucao')
			#os.system('git add .')
			#os.system("git commit -a -m '%s'"%now)
			#os.system('git push origin master')
	
		
		print('Solucao '+ str(atribuicao.solucao))


