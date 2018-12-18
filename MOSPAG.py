
import numpy as np
import random

bestfit = np.Inf
tPop = 100
import time







file = open('/home/mateus/Documentos/algoritmos de otimizacao/MOSP/ChallengeInstances2005/Miller/Miller19t.txt','r')


def reader(file):
	mat = []
	for linha in file:
		vec =[]
		aux =[]
		aux = linha.split()
		#print linha
		for caract in aux:	
			vec.append(int(caract))
		mat.append(vec)
	return mat


def preproc(mat2):
	mat3 = np.copy(mat2)
	ncol = mat2.shape[1]
	nlin = mat2.shape[0]
	for col in range(ncol):
		vsom = []
		vone = np.argwhere(mat2[:,col]==1)
		for au in range(vone[0],vone[-1]):
			mat3[au,col] = 1
	return mat3




def evalu(mat):
	maxV = -1
	lin = mat.shape[0]
	for linha in range(lin):
		soma = sum(mat[linha,:])
		if soma>maxV:
			maxV = soma
	return maxV



def change(mat,padroes):
	matAux = mat
	i = 0
	
	
	for p in padroes:
		aux = matAux[i,:]
		matAux[i,:] = mat[p,:]
		mat[p,:] = aux
		i+=i
	return matAux

		


def uniform(self, a, b):
    "Get a random number in the range [a, b) or [a, b] depending on rounding."
    return a + (b-a) *random.uniform(0, 1)
#Gera a populacao, nao tem return pq a pop eh global
#falta fazer um jeito de remover solucoes repetidas.
def geraPop(tpop,n):
	pop = []
	popaux = []
	for t in range(tpop):
		for i in range(n):
			#pop.append(random.sample(range(1,100), n))
			#np.random.seed(int(time.time()))
			gen = random.uniform(0, 1)
			popaux.append(gen)
		pop.append(popaux)
		popaux=[]
	
	
	return pop


def decoder(pop):
	popaux = sorted(pop)
	count = 0
	for gen in popaux:
		for index in range(len(pop)):	
			if gen == pop[index]:
				pop[index] = int(count)
				count = count + 1

				#for w in range(len(pop)):
				#	if pop[w] == count:
				#		pop[w] = int(count)
	pop = np.asarray(pop)			
	return pop.astype(int)						


#calcular as colunas com maior peso, estas deverao ser substituidas na mutacao/cruzamento

def cruzamento(fitness):
    n = len(popG)/10
    bestFit = np.where(xx == min(xx))
    nind = []
    novos = []
    j=0
    for i in range(n):
        for z in range(len(pop[bestFit[0][j]])):
            popG[fitness.index(max(xx))] = popG[bestFit[0][j]][z] + popG[bestFit[0][-(j+1)]][z]/2)
        novos.append(nind)
        nind=[]
        j=j+1


def mutacao:
	n = len(popG)/10
	#cada individuo tem uma chance de se mutar
	for i in range(n):
		pop[random.randint(1,100)] 

	
		if random.uniform(0, 1)>0.53:
			pop[t] 






def roleta(pop):



def selecao(pop):



mat = np.array(reader(file))
mat.astype(int)
nlin = mat.shape[0]

global pop
pop = geraPop(tPop,nlin)




xx=[]
for i in range(len(pop)):
	#print pop[i]
	#print "decoder i"
	#print decoder(pop[i])
	fitness.append(evalu(preproc(change(mat,decoder(pop[i])))))

xx = []
print min(fitness)
print max(fitness)