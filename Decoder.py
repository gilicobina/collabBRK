import numpy as np

import time


class Decoder:
	def __init__(self, custos, tamanho):
		self.custos = custos
		self.tam = int(tamanho)
  
  	#Preenche matriz com indices 1

	def preproc(self,mat2):
		mat3 = np.copy(mat2)
		#print mat3
		#print mat3.shape
		nlin = mat2.shape[0]
		ncol = mat2.shape[0]
		for col in range(ncol):
			vone = np.argwhere(mat2[col,:]==1)
			if len(vone)>0:
				for au in range(vone[0],vone[-1]):
					mat3[col,au] = 1
		#print("#MAT3#")
		
		
		return mat3
    
    
    
    
	
	def evalu(self,mat):
	    	maxV = 0
	    	lin = mat.shape[0]
	    	col = mat.shape[1]
	    	somaC = [0]*col
	    	#print("linha")
	    	#print lin
	    	#print mat
	    	
	    	for col in range(col):
	    		for linha in range(lin):
	    			somaC[col] = somaC[col] + mat[linha][col]
	    		#print "SOMA"
	    		#print soma
	    		
	    		maxV = max(somaC)
	    		
	    	
	    	

	    	return maxV
    
    
    
	def change(self,mat,padroes):
		matAux = np.copy(mat)
  		
		
		i = 0
		#print "INICIANDO PADRONIZACAO"
		#print(padroes)
		
		for p in padroes:
				#print "i"+str(i)+'= p'+str(p)

				#print matAux[i,:]
			#print(p)
			#print(i)
			#print(mat)
			#print(mat[:,p])

			#modifica as linhas
			matAux[:,i] = mat[:,p]
			i=i+1
		
		return matAux


	def dcd(self, cromossomos):

		'''
		Cromossomos eh um vetor e redimensionado em uma matriz para a realizacao das 
		operacoes de restricao e funcao objetivo
		'''
		
		pop = np.zeros(len(cromossomos))
		#cromossomos = np.reshape(cromossomos,(self.tam,self.tam))
		
		popaux = sorted(cromossomos)
		count = 0
		for gen in popaux:
			for index in range(len(cromossomos)):
				if gen == cromossomos[index]:
					pop[index] = int(count)
     
					count = count + 1


		
		
		#Funcao objetivo
		pop = pop.astype(int)
		return pop
	def decode(self, cromossomos):

		'''
		Cromossomos eh um vetor e redimensionado em uma matriz para a realizacao das 
		operacoes de restricao e funcao objetivo
		'''
		
		pop = np.zeros(len(cromossomos))
		#cromossomos = np.reshape(cromossomos,(self.tam,self.tam))
		
		popaux = sorted(cromossomos)
		count = 0
		for gen in popaux:
			for index in range(len(cromossomos)):
				if gen == cromossomos[index]:
					pop[index] = int(count)
     				
					count = count + 1


		
		
		#Funcao objetivo

		pop = pop.astype(int)
		'''
		print "******************************************************************************************"
		print "populacao"
		print pop
		print "******************************************************************************************"
		print "matriz"
		print self.custos
		print "******************************************************************************************"
		print "mudada"
		chang = self.change(self.custos,pop)
		print chang
		print "******************************************************************************************"
		print "preprocess"
		preprocess = self.preproc(chang)
		print preprocess
		print "******************************************************************************************"
		'''
		Z = self.evalu(self.preproc(self.change(self.custos,pop)))

		return Z
