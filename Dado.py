
class Dados:
	def __init__(self, arquivo):
		tupla = self.ler_dados(arquivo)
		self.dim = tupla[0]
		self.matriz = tupla[1]
		

	def ler_dados(self, arquivo):
		try:
			mat = []
			with open(arquivo) as arq:
				for linha in arq:
					vec =[]
					aux =[]
					aux = linha.split()
	                  #print linha
					for caract in aux:
						if caract == '0' or caract == '1':
							vec.append(int(caract))
					mat.append(vec)
	                #arq.close()
				#mat = self.transposeMatrix(mat)
			
			return (len(mat[1])),mat

		except IOError:
			print('Erro ao abrir arquivo ', file)

		
		
