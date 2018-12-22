from Decoder import Decoder
from math import sqrt
from random import randint
import threading


class localsearch(threading.Thread):
  def __init__(self,sol,custos):
    self.sol = sol
    self.custos = custos
    self.TAM_CROM = len(sol)
    threading.Thread.__init__(self)
    self.solu = []
    self.melhor = 10000
  #get the list of indexes of the colours which comes for initialise(size) operator

  def run(self):
    #self.hillClimbingBest(self.sol)
    self.run_2opt(self.sol)
  
  def evaluate(self, cromossomo):
    decodificacao = Decoder(self.custos, sqrt(self.TAM_CROM))
    '''
    Transforma as chaves aleatorias em binarios, verifica as restricoes e 
    retorna o custo a ser minimizado
    '''
    Z = decodificacao.decode(cromossomo)
    return Z

  #swap/ Mutation operator
  def swap(self,sol):  #get the list of indexes of the colours which comes for initialise(size) operator
    l = len(sol)    #l gets the value of the length of sol list
    pos1 = pos2 = randint(0, l-1)   #set randomly position 1 and position 2
    while (pos1 == pos2):   #in order not to have the same values for pos1 and pos2
        pos2 = randint(0, l-1)
    value= sol[pos1]    #keep track of the value in pos1
    sol[pos1] = sol[pos2]   #replace value in pos1 with pos2 value
    sol[pos2] = value   #replace value in pos2 with pos1 value
    return sol  #return the list of indexes with the swap changes

#perturbation operator
  def perturbation(self,sol):  #get the list of indexes of the colours which comes from initialise(size) operator
    #it is the same process of swap function but here we do this twice
    l = len(sol)
    pos1 = pos2 = randint(0, l-1)
    while (pos1 == pos2):
        pos2 = randint(0, l-1)
    value= sol[pos1]
    sol[pos1] = sol[pos2]
    sol[pos2] = value
    pos3 = pos4 = randint(0, l-1)
    while (pos3 == pos4):
        pos4 = randint(0, l-1)
    value= sol[pos3]
    sol[pos3] = sol[pos4]
    sol[pos4] = value
    return sol

#inverse hill climber
  def reverse(self,sol):   #get the list of indexes of the colours which comes for initialise(size) operator
    new_sol=[]
    l = len(sol)
    pos1 = pos2 = randint(0, l-1)   #set randomly position 1 and position 2
    while (pos1 == pos2):   #in order not to have the same values for pos1 and pos2
        pos2 = randint(0, l-1)
    #print pos1, pos2
    if pos1<pos2:   #I set this condition in order to from which position do I have o start
        value=sol[pos1] #keep track of the value in pos1
        if pos1!=0:
            for j in sol[0:pos1]:   #the values between 0 and pos1
                new_sol.append(j)   #append the values that are before pos1 in the list
            for j in sol[pos2:pos1:-1]: #inverse the values between pos1 and pos2
                new_sol.append(j)   #append the inverted values in the list
                sol[pos2]=value     #change also the pos2 value because it does not change with the above process 
        else:
            for j in sol[pos2:pos1:-1]: #if pos1 = 0  inverse all the values between pos1 and pos2. It is in the beginning of the list
                new_sol.append(j)   #append the inverted values in the list
                sol[pos2]=value     #change also the pos2 value because it does not change with the above process 
        for j in sol[pos2:l]:   #all the values after pos2
            new_sol.append(j)   # append all the values after pos2
                        
    else:   #if pos1>pos2
        #it is the same process as above but this time we have pos2 before pos1
        value=sol[pos2] 
        if pos2!=0:
            for j in sol[0:pos2]:
                new_sol.append(j)
            for j in sol[pos1:pos2:-1]:
                new_sol.append(j)
                sol[pos1]=value
        else:
            for j in sol[pos1:pos2:-1]:
                new_sol.append(j)
                sol[pos1]=value
        for j in sol[pos1:l]:
            new_sol.append(j)
    return new_sol  #returns the solution that has been inverted


# 1pt- crossover. Input: 2 lists of indexes of colours. Returns a single offspring
  def xover_1pt(sol1, sol2):
    xp =randint(0,len(sol1)-1)
    return[sol1[:xp] + sol2[xp:]]    



#Hill Climber
  def hillClimbingBest(self,sol):  #get the list of indexes of the colours which comes from initialise(size) operator

    rand1 = sol     #keep track of sol

    best = self.evaluate(sol)    #evaluate the Euclidean distance of the list sol
    group_hill=[]

    for i in range(100):    #100 iterations
        sol=self.swap(sol)   #swap sol list
        solution = self.evaluate(sol)    #evaluate the Euclidean distance of the list sol after the swap
        if solution<best:   #check if the new solution is better than the previous
            best=solution   # if the new solution is better change the best value with the value of the new solution
            rand1=sol   #change rand1 with the new sol
        group_hill.append(best) #keep track of the best solution during the iteration in grou_hill list
        if(best<self.melhor):
            self.melhor = best
            self.solu = sol
    print("HillC - melhor = "+str(best))
    #return best, rand1, group_hill  #returns the best Euclidean distance of the 100 iterations, its corresponding list of indexes of colours and the list with the best solution during the iterations

#function that runs the hill climber 20 times
  def hill_climb_20runs(self,sol): #get the list of indexes of the colours which comes from initialise(size) operator
    hc_sol=[]
    hc_rand=[]
    for j in range(20): #20 runs

        
         rand_hill_climb = self.hillClimbingBest(sol)[1] #store the list of indexes of colours of the best Euclidean distance in hill climber
         sol_hill_climb = self.hillClimbingBest(sol)[0]  #store the best Euclidean distance of hill climber
         hc_sol.append(sol_hill_climb)  #append the best Euclidean distance of hill climberin hc_sol list
         hc_rand.append(rand_hill_climb)    #append its corresponding lists of indexes in hc_rand list
    min_sol = hc_sol[0]     #set the first value of the hc_sol as the best
    min_rand = hc_rand[0]   #set the corresponding list of indexes of colours as the best
    for i in range(1,20):   #I start from 1 because I have set the first value as the best
        if min_sol> hc_sol[i]:  #check if any value in hc_sol is better than min_sol
            min_sol = hc_sol[i]     #if the condition is correct change min_sol to the value of the condition
            min_rand = hc_rand[i]   # change the corresponding list of indexes of colours

        if(min_sol<self.melhor):
            self.melhor = min_sol
            self.solu = sol
    print("HillC - Melhor solucao = "+str(min_sol),str(sol))
    #return min_sol, min_rand, hc_sol, hc_rand   #returns the best Euclidean distance of the 20 runs of hill climber, its corresponding lists of indexes of  list with the 20 Euclidean distances of hill climber, and the 20 lists of indexes of colours
         


#iterated local search

  def iterated_local_search(self,sol): #get the list of indexes of the colours which comes for initialise(size) operator

        iter_100 = []
        iter_100_rand = []
        
        
        best = self.hillClimbingBest(sol)[1] #store the list of indexes of colours of the best Euclidean distance in hill climber
        best_sol = self.hillClimbingBest(sol)[0] #store the best Euclidean distance of hill climber
        for j in range(100):    #100 iterations
            sol = self.perturbation(sol) #perturbate the list of indexes of colours that the function gets
            sol = self.hillClimbingBest(sol)[1]  #implement hill climbing to the perturbated list
            sol1 = self.evaluate(sol)    #evaluate the Euclidean distance of the list of colours after perturbation and hill climbing
            if sol1<best_sol:   #check if sol1 is better than best_sol
                best= sol   #if the condition is correct change best with sol
                best_sol = sol1     #if the condition is correct change best_sol with sol1
            iter_100.append(best_sol)   #append the 100 best_sol Euclidean distances that we get
            iter_100_rand.append(best)  #append their corresponding list of indexes of colours
        best2 = iter_100[0]     #set the first value of the iter_100 as the best
        best2_rand = iter_100_rand[0]   #set the corresponding list of indexes of colours as the best
        for i in range(1,100):  #I start from 1 because I have set the first value as the best
            if best2>iter_100[i]:    #check if any value in iter_100 is better than best2
                best2 = iter_100[i]     #if the condition is correct change best2 to the value of that satisfies the condition
                best2_rand = iter_100_rand[i]   # change the corresponding list of indexes of colours
        print("ILS - Melhor solucao = "+str(self.evaluate(sol))+" array "+str(sol))
        
       # return best2, best2_rand, iter_100, iter_100_rand   #returns the best Euclidean distance of the 100 iterations of iterated local search, its corresponding list of indexes of  list with the 100 Euclidean distances of iterated local search, and the 100 lists of indexes of colours
  def swap_2opt(self,route, i, k):
    
    """
    swaps the endpoints of two edges by reversing a section of nodes,
        ideally to eliminate crossovers
    returns the new route created with a the 2-opt swap
    route - route to apply 2-opt
    i - start index of the portion of the route to be reversed
    k - index of last node in portion of route to be reversed
    pre: 0 <= i < (len(route) - 1) and i < k < len(route)
    post: length of the new route must match length of the given route
    """
    assert i >= 0 and i < (len(route) - 1)
    assert k > i and k < len(route)
    new_route = route[0:i]
    
   
   
    if type(new_route)!=list:
        new_route = new_route.tolist()
   
    new_route.extend(reversed(route[i:k + 1]))
    new_route.extend(route[k + 1:])
    assert len(new_route) == len(route)
    return new_route
     
  def run_2opt(self,route):
    """
    improves an existing route using the 2-opt swap until no improved route is found
    best path found will differ depending of the start node of the list of nodes
        representing the input tour
    returns the best path found
    route - route to improve
    """
    improvement = True
    best_route = route
    best_distance = self.evaluate(route)
    while improvement:
        improvement = False
        for i in range(len(best_route) - 1):
            for k in range(i + 1, len(best_route)):
                new_route = self.swap_2opt(best_route, i, k)
                new_distance = self.evaluate(new_route)
                if new_distance < best_distance:
                    best_distance = new_distance
                    best_route = new_route
                    improvement = True
                    break  # improvement found, return to the top of the while loop
            if improvement:
                break
    assert len(best_route) == len(route)
    if best_distance<self.melhor:
        self.solu = best_route
        self.melhor = best_distance
    

    print("MELHOR 2-OPT ",str(best_distance))
    return best_route

  