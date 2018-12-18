from Decoder import Decoder
import numpy as np
from math import sqrt
import time, timeit
import random

import matplotlib.pyplot as plt #carrega a
                                #biblioteca pyplot
import matplotlib.gridspec as gridspec #carrega a
                                       # biblioteca gridspec

from localsearch import localsearch

import threading


class BRKGA(threading.Thread):
	def __init__(self, dados,tam_pop, max_gen, tx_cross,tx_mut, tx_elite):
		#Tamanho da populacao
		self.TAM_POP = int(tam_pop)
		#Criterio de parada
		self.MAX_GEN = max_gen
		#Matriz de custos
		self.custos = np.array(dados.matriz)
		#Numero de genes em cada cromossomo
		self.TAM_CROM = int(dados.dim)
		#Taxa de cruzamento
		self.TX_CROSS = tx_cross
		#Taxa de mutacao(Numero de mutantes criados)
		self.TX_MUT = tx_mut
		#Taxa da populacao que estara na populacao elite
		self.TX_ELITE = tx_elite

		threading.Thread.__init__(self)
		
		#Utilizado p medir o tempo
		#inicio = timeit.default_timer()
		#self.solucao, fim = self.brkga_init(inicio)
		self.solucao = -1
		
		#print ('duracao: %f' % (fim - inicio))
		

		
	def run(self):
		inicio = timeit.default_timer()
		#inicio = time.gmtime()[5]
		self.brkga_init(inicio)

	#Gera a populacao
	def gera_populacao(self):
		populacao = []
		for i in range(self.TAM_POP):
			#np.random.seed(time.gmtime()[5])
			np.random.seed(int((time.time()-int(time.time()))*10))

			#Gera um individuo com chaves aleatorias [0,1]
			self.cromossomo = np.random.rand(self.TAM_CROM)
			#Esse individuo eh adicionado a uma populacao
			populacao.append(self.cromossomo)
		return np.array(populacao)
		
	#Faz o calculo da aptidao(Fitness)
	def aptidao(self, cromossomo):
		decodificacao = Decoder(self.custos, sqrt(self.TAM_CROM))
		'''
		Transforma as chaves aleatorias em binarios, verifica as restricoes e 
		retorna o custo a ser minimizado
		'''
		Z = decodificacao.decode(cromossomo)
          
		return Z
		
	def decoder(self, cromossomo):
		decodificacao = Decoder(self.custos, sqrt(self.TAM_CROM))
		'''
		Transforma as chaves aleatorias em binarios, verifica as restricoes e 
		retorna o custo a ser minimizado
		'''	
		
		Z = decodificacao.dcd(cromossomo)
          
		return Z


    #Retorna a aptidao de cada individuo da populacao e adiciona em uma lista de aptidoes
	def calcula_aptidao(self, populacao):
		return [self.aptidao(individuo) for individuo in populacao]


	def selecao_roleta(self, aptidoes):
		
		percentuais = np.array(aptidoes)/float(sum(aptidoes))
		vet = [percentuais[0]]
		for p in percentuais[1:]:
			vet.append(vet[-1]+p)
		r = np.random.random()
		for i in range(len(vet)):
			if r <= vet[i]:
				return i


	def decode(self,cromossomos):
	    count = 0
	    size = len(cromossomos)
	    popaux = sorted(cromossomos)
	    pop = [0]*size
	    for gen in popaux:
	        for index in range(size):
	            if gen == cromossomos[index]:
	                pop[index] = int(count)            
	                count = count + 1

	    return cromossomos,pop

	def encode(self,cromossomosI):
	    count = 0 
	    size = len(cromossomosI)
	    
	    maxi = max(cromossomosI)
	    
	    mini = min(cromossomosI)
	    
	    novo = [0]*size
	    for index in cromossomosI:
	            novo[index] = abs(float((cromossomosI[index] - mini))/float((maxi-mini)))
	   
	    return novo


	def cruzamento(self,ind1,ind2):
		#For the value of a, Eshelman and Schaffer have used 0.5[6]. With our calculation, the value of a that pre-serves 
		#he variance of the parental population is 0.366
		#A Crossover Operator Using  Independent  Component  Analysis for Real-Coded Genetic Algorithms Takahashi
		
		filho1=[]
		filho2=[]
		alpha = 0.366
		for i in range(self.TAM_CROM):
			dif = abs(ind1[i]-ind2[i])
			minimum = min(ind1[i],ind2[i])
			maximum = max(ind1[i],ind2[i])
			filho1.append(random.uniform(minimum-(dif*alpha),maximum-(dif*alpha)))
			filho2.append(random.uniform(minimum-(dif*alpha),maximum-(dif*alpha)))
		return filho1,filho2



	'''
	def cruzamento(self,ind1, ind2):
	    ind1_x = self.decode(ind1)
	    ind2_x = self.decode(ind2)
	    ind1= ind1_x[1]
	    ind2= ind2_x[1]
	    size = min(len(ind1), len(ind2))
	    p1, p2 = [0]*size, [0]*size

	    # Initialize the position of each indices in the individuals
	    for i in xrange(size):
	        p1[ind1[i]] = i
	        p2[ind2[i]] = i

	    # Choose crossover points
	    cxpoint1 = random.randint(0, size)
	    cxpoint2 = random.randint(0, size - 1)
	    if cxpoint2 >= cxpoint1:
	        cxpoint2 += 1
	    else: # Swap the two cx points
	        cxpoint1, cxpoint2 = cxpoint2, cxpoint1

	    # Apply crossover between cx points
	    for i in xrange(cxpoint1, cxpoint2):
	        # Keep track of the selected values
	        temp1 = ind1[i]
	        temp2 = ind2[i]
	        # Swap the matched value
	        ind1[i], ind1[p1[temp2]] = temp2, temp1
	        ind2[i], ind2[p2[temp1]] = temp1, temp2
	        # Position bookkeeping
	        p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
	        p2[temp1], p2[temp2] = p2[temp2], p2[temp1]

	    ind1 = self.encode(ind1_x[1])
	    ind2 = self.encode(ind2_x[1])
	    return ind1, ind2
    	
    	
    #parametrized uniform crossover    

	def cruzamento(self, pai,mae):
		filhos = []
		for i in range(2):
			filho = []
			for j in range(self.TAM_CROM):
				#Vicio probabilistico
				vp = np.random.rand()
				if vp <= self.TX_CROSS:
					filho.append(mae[j])
				else:
					filho.append(pai[j])
				filhos.append(filho)
		
		return filhos[0], filhos[1]
	'''
	def separacao_da_populacao(self, aptidoes, populacao):
		#Elementos vai se tornar uma tupla composta por(aptidoes, populacao)
		elementos = []
		for i in range(len(aptidoes)):
			elementos.append([aptidoes[i], list(populacao[i])])
		
		qtd = int(self.TX_ELITE*self.TAM_POP)

		#Ordena do menor para o maior pelas aptidoes
		elementos = sorted(elementos)
		
		pop_elite = []
		apt_elite = []
		pop_nao_elite = []
		apt_nao_elite = []
		i = 0
		for x in elementos:
			if i< qtd:
				apt_elite.append(x[0])
				pop_elite.append(x[1])
			else:
				apt_nao_elite.append(x[0])
				pop_nao_elite.append(x[1])

			i += 1

		#Retorna os melhores e os piores
		return pop_elite, apt_elite, pop_nao_elite, apt_nao_elite 
	
	#Para continuar compondo a nova geracao, uma quantidade de mutantes eh criada.
	'''
	def mutacao(self):
		qtd = int(self.TX_MUT*self.TAM_POP)
		mutantes = []
		for i in range(qtd):
			#Gera um individuo com chaves aleatorias [0,1]
			np.random.seed(int((time.time()-int(time.time()))*10))
			self.cromossomo = np.random.rand(self.TAM_CROM)
			#Esse individuo eh adicionado a uma populacao
			mutantes.append(self.cromossomo)
		return mutantes
	'''
	def mutacao(self, pop):
		cromossomos = np.copy(pop)
		qtd = int(self.TX_MUT*self.TAM_CROM)
		tam = len(cromossomos)
		#print cromossomos[0]
		cromossomo = np.random.rand(self.TAM_CROM)
		mutantes = []
		for i in range(tam):
			cromossomo = np.random.rand(qtd)
			aux = np.random.randint(self.TAM_CROM, size=qtd)
			j=0
			for num in aux:
				cromossomos[i][num] = cromossomo[j]
				j=j+1
			
			#print(cromossomos[i])
			#Esse individuo eh adicionado a uma populacao
			mutantes.append(cromossomos[i])
		return mutantes
	

	def brkga_init(self, inicio):
		melhores = []
		print('Executando BRKGA...')
		#Cria a populacao
		populacao = self.gera_populacao()
		#Inicia com o calculo das aptidoes da populacao 
		aptidoes = self.calcula_aptidao(populacao) 
		#Melhores
		melhores.append(np.min(aptidoes))
		#Imprime o melhor de cada geracao
		print('0 - melhor:',np.min(aptidoes))

		#Criterio de parada: geracoes
		for geracao in range(self.MAX_GEN):
			
			'''
			Aqui o grande diferencial do BRKGA com o RKGA, ordena por aptidoes e separa em
			elite e nao elite a populacao
			'''
			populacao_elite,aptidao_elite, populacao_nao_elite , aptidao_nao_elite = self.separacao_da_populacao(aptidoes, populacao)

			#A populacao elite ja esta garantida para proxima geracao
			nova_populacao = [individuo for individuo in populacao_elite]

			#Geracao de individuos que sofreram mutacao sao adicionados a nova populacao
			mutantes = self.mutacao(populacao_elite)
			for individuo in mutantes:
				nova_populacao.append(individuo)

			#Agora faz o cruzamento e gerar os individuos restantes para compor a nova populacao
			for c in range(int((self.TAM_POP-len(nova_populacao))/2)):
				'''
				print(len(populacao))
				print(len(aptidoes))
				'''
				#Selecao depois do elitismo do BRKGA em separar a populacao
				pai = populacao_nao_elite[self.selecao_roleta(aptidao_nao_elite)]
				mae = populacao_elite[self.selecao_roleta(aptidao_elite)]

				#Cruzamento
				filho,filha = self.cruzamento(pai,mae)

				#Nova populacao sendo criada
				nova_populacao.append(filho)
				nova_populacao.append(filha)

			
			
			#A populacao atual passa a ser a nova geracao
			
			aptidao_nova = self.calcula_aptidao(nova_populacao)
			#populacao = nova_populacao

			#print(aptidoes)
			#Calcula as aptidoes da nova geracao
			kk = 0
			

			if min(aptidao_nova)<min(aptidoes):
				aptidoes[aptidoes.index(min(aptidoes))] == min(aptidao_nova)
				populacao[aptidoes.index(min(aptidoes))] = nova_populacao[aptidao_nova.index(min(aptidao_nova))]
			if len(aptidao_nova)<len(aptidoes):
				for apt in aptidao_nova:
					if aptidoes>aptidao_nova:
						populacao[kk] = nova_populacao[kk]
					kk=kk+1
			else:
				for apt in aptidoes:
					if aptidoes>aptidao_nova:
						populacao[kk] = nova_populacao[kk]
					kk=kk+1

			aptidoes = self.calcula_aptidao(populacao)

			#Utilizado para medir o tempo
			fim = timeit.default_timer()
			#Imprime o melhor de cada geracao
	

			#print(geracao+1,'- melhor:',melhores[0],' - tempo: ', fim)
			#print(geracao+1,'- melhor:',melhores[0],self.decoder(populacao_elite[0]))
			
			#print(geracao+1,'- BRKGA melhor:',melhores[0])


			
			#Melhores
			melhores.insert(0, np.min(aptidoes))
			ls=localsearch(self.decoder(populacao_elite[0]),self.custos)
			

			if(geracao%5==0 and geracao%7==0):
				ls.start()
				ls.join() 
			
			if ls.melhor<=melhores[0]:
					
					populacao[0]=self.encode(ls.solu)


		#print("############## "+str(ls.iterated_local_search(self.decoder(populacao_elite[0]))))
		#ls.iterated_local_search(self.decoder(populacao_elite[0]))
		
		
		self.solucao = melhores[0]
		fim = timeit.default_timer()
		#return np.min(melhores), fim 
