import csv
import glob
from sys import argv

def verificar_arquivo():
  caminho = 'arquivo/produtos'
  arquivo = caminho + '/dados.csv'
 
def ler_produtos(arquivo):
  arquivo_aberto = open(arquivo, 'rb')
  return csv.reader(arquivo_aberto,delimiter=',')
 


x = ('/home/mateus/Documentos/algoritmos de otimizacao/MOSP/ChallengeInstances2005/'+argv[1]+'/')
y = ('/home/mateus/Documentos/algoritmos de otimizacao/MOSP/ChallengeInstances2005/trial/')
listaArq = glob.glob(x+'*.txt')

for file in listaArq:
	f = open(file,'r')
	data = f.readlines()
	linha = []
	count = 0
	
	for line in data:
		words = line.split()

		if len(words)>5 and (words[0] == '0' or words[0] == '1'):
			ww = str(words)
			ww = ww.replace('[','')
			ww = ww.replace(']','')
			ww = ww.replace(',',' ')
			ww = ww.replace("'",'')
			linha.append(ww)
		elif words == []:
			arq = file.replace(x,'')
			arq = arq.replace('.txt','')
			
			z = open(y+argv[1]+'_'+arq+'_'+str(count)+'.txt','w+')
			for lin in linha:
				z.write(str(lin))
				z.write('\n')
			count = count + 1
			linha = []
			z.close()
		
