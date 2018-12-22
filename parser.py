import csv
import glob
from sys import argv
import os

def verificar_arquivo():
  caminho = 'arquivo/produtos'
  arquivo = caminho + '/dados.csv'
 
def ler_produtos(arquivo):
  arquivo_aberto = open(arquivo, 'rb')
  return csv.reader(arquivo_aberto,delimiter=',')
 


#x = ('/home/mateus/Documentos/algoritmos de otimizacao/MOSP/ChallengeInstances2005/'+argv[1]+'/')
x = (argv[1]+'/')
y = ('instancias/')
if not os.path.exists(y):
    os.mkdir(y)
    print("Directory " , y ,  " Created ")
else:    
    print("Directory " , y ,  " already exists")

listaArq = glob.glob(x+'*.txt')

print listaArq
for file in listaArq:
	arq = file.replace(x,'')
	arq = arq.replace('.txt','')

	with open(file) as f:
		data = f.readlines()
	
	linha = []
	count = 0
	for line in data:
		words = line.split()
		if len(words)>4 and (words[0] == '0' or words[0] == '1'):
			ww = str(words)
			ww = ww.replace('[','')
			ww = ww.replace(']','')
			ww = ww.replace(',','')
			ww = ww.replace("'",'')
			if count>0:
				with open(y+arq+'_'+str(count)+'.txt','a+') as z:
					z.write(str(ww))
					z.write('\n')
			else:
				with open(y+arq+'.txt','a+') as z:
					z.write(str(ww))
					z.write('\n')
		elif words == []:
			count = count + 1
	

		
