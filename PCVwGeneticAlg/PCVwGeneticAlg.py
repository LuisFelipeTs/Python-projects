import random

#Flyflood V Alg genético
def generateIpopDistances(coords):
    eixo_xy = list(coords.keys())
    matriz_popi = {}
    for i in range(len(eixo_xy)):
        new_cr = eixo_xy[i]
        matriz_popi[new_cr] = []
        for n in range(len(eixo_xy) ):
            first_p = coords[new_cr]
            sec_p = coords[eixo_xy[n]]
            matriz_popi[new_cr].append(routeCalculator(first_p, sec_p))
    return matriz_popi

def markPoints(coords, nx , ny , value):
    if value not in coords.keys() :
        coords[value] = [nx, ny]
    else : print('Estas coords já foram inseridas')
    return coords

def routeCalculator(coordsA, coordsB):
    result = 0
    if coordsA[0] > coordsB[0] : result += (coordsA[0] - coordsB[0])
    else : result += (coordsB[0] - coordsA[0])

    if coordsA[1] > coordsB[1] : result += (coordsA[1] - coordsB[1])
    else : result += (coordsB[1] - coordsA[1])
    return result

#GERAR A POPULAÇÂO
def callRoutesPop(city_values , population_size):
    random_city_sample = (city_values)[:]
    random_city_sample.remove('R')
    new_pop = []
    for p in range(population_size):
        new_route = random.sample(random_city_sample,len(random_city_sample))
        new_route.append('R')
        new_route.insert(0,'R')
        new_pop.append(new_route)
    return(new_pop)

#ALGORITMO QUE MELHOR SE APTARÁ 
def calcCromoFit(cromoss , dist_matrz):
    route_dist_value = 0
    cromo_f = cromoss[:]
    lst_keys = list(dist_matrz.keys())
    for i in range(len(cromoss) - 1):
        dist_n_esp = dist_matrz[cromoss[i]]
        route_dist_value += dist_n_esp[lst_keys.index(cromoss[i + 1])]
    cromo_f.append(1 / route_dist_value)
    return cromo_f


def fitness(pop, matriz_dist):
    order_pop = [] #melhor pro pior
    for i in range(len(pop)):
        pos = 0
        cromo_f = calcCromoFit(pop[i] , matriz_dist)
        while pos <= (len(order_pop) - 1):
        #ordenando pelo coeficiente de fitness
            if cromo_f[-1] >= order_pop[pos][-1]: pos += 1
            else: break
        order_pop.insert(pos , cromo_f)
    return order_pop 

#CROSS
def crossOver(parent1 , parent2):
    cut_point = random.randint(1 ,len(parent1)-2)
    child1 = parent1[:cut_point] +  parent2[cut_point:]
    child2 = parent2[:cut_point] +  parent1[cut_point:]
    child1 = checkCross(child1, parent1)
    child2 = checkCross(child2, parent2) 
    return child1, child2

#ORGANIZAR FILHO
def checkCross(child, dad):
    control_dad = dad[:] 
    new_city = ""
    for i in range(len(child)):
        if child[i] in control_dad: control_dad.remove(child[i])
        else:
            new_city = random.randint(0,len(control_dad)-1) 
            while new_city in child : new_city = random.randint(0,len(control_dad)-1) 
            child[i] = control_dad[new_city]
            control_dad.remove(child[i])
    return child


#MUTAÇÂO 
def mutate(child, probability):
    fpoint = 0
    spoint = 0
    if random.randint(0,100) < probability:
        fpoint = random.randint(1, len(child)- 1 )
        spoint = random.randint(1, len(child)- 1 )
        while (fpoint == spoint) : spoint = random.randint(1,len(child)-1)
        old_child = child[:]
        child[fpoint] = old_child[spoint] 
        child[spoint] = old_child[fpoint] 
    return child

#MÉTODO ROLETA
def roletaSelector(order_pop, values_mtrz, nGenerations):
    final_route = "N/A"
    control_coef = 0
    for i in range(nGenerations):
        fit_list = []
        population_size = len(order_pop)
        for n in range(population_size):
            fit_list.append(order_pop[n][-1])
        roll_result = random.choices(order_pop, weights = fit_list , k = 2)
        parent1 = roll_result[0][:-2]
        parent2 = roll_result[1][:-2]
        child1, child2 = crossOver(parent1 , parent2)
        child1 = mutate(child1, 5) # 5% de probabilidade
        child2 = mutate(child2, 5)

        child1.append("R")
        child2.append("R")

        coef1 = calcCromoFit(child1 , values_mtrz)
        coef1_a = coef1[-1]
        if coef1_a > control_coef : 
            final_route = child1
            control_coef = coef1_a

        coef2 = calcCromoFit(child2 , values_mtrz)
        coef2_a = coef1[-1]
        if coef2_a > control_coef : 
            final_route = child2
            control_coef = coef2_a
        
    return(final_route) 

#LENDO ARQUIVOS
arquivoRead = open('tst2.txt')
entryTest = arquivoRead.readlines()
entrygeral = str(entryTest[0]).replace('\n', '')
y, x = entrygeral.split(" ")
y, x = int(y) , int(x)

if y != 0:
    coords = {}
    for i in range(y): 
        new_entrytreat = str(entryTest[i + 1]).replace('\n', '')
        new_entry = new_entrytreat.split(" ")
        for a in range(x):
            if new_entry[a] != '0':
                coords = markPoints(coords, a , i, new_entry[a])
            
    entrygeral = str(entryTest[i+2]).replace('\n', '')
    nGener , population_size = entrygeral.split(" ")
    nGener , population_size = int(nGener) , int(population_size)

    values_city = list(coords.keys())
    finax = callRoutesPop( values_city , population_size) #pop size
    distances = generateIpopDistances(coords)
    resp = roletaSelector(fitness(finax , distances),distances , nGener)
    print(' '.join(resp[:-1])) #n generations

else : print("insira um valor válido")


#Flyflood First Version
"""
def try_route( coords , new_route, dms , best_dms, best_route):
    chaves = list(coords.keys())
    for i in range(len(chaves)):
        value = chaves[i]
        move = 0
        if (value not in new_route) and (value != "end_R"):
            move = route_calculator(coords[new_route[-1]], coords[value])
            dms += move
            new_route.append(value)
            
            new_route, best_route, dms, best_dms = try_route( coords , new_route, dms , best_dms , best_route)
            new_route.pop()

        if len(new_route) + 1 == len(chaves):
            move = route_calculator(coords[new_route[-1]] , coords[chaves[-1]])
            dms += move
            if (dms <= best_dms) or (best_dms == 0) :
                best_dms = dms
                best_route = list(new_route)
            dms -= move
            return new_route, best_route, dms, best_dms
    
        dms -= move
    return new_route, best_route, dms, best_dms
def route_calculator(coordsA, coordsB):
    result = 0
    if coordsA[0] > coordsB[0] : result += (coordsA[0] - coordsB[0])
    else : result += (coordsB[0] - coordsA[0])

    if coordsA[1] > coordsB[1] : result += (coordsA[1] - coordsB[1])
    else : result += (coordsB[1] - coordsA[1])
    return result
def define_route(coords):
    dms = 0 #donometro da rota atual
    best_dms = 0 #menor donômetro
    best_route = [] #melhor rota
    if "R" in list(coords.keys()):
        new_route = ["R"] #nova rota de teste
        coords = mark_points(coords, coords["R"][0], coords["R"][1], "end_R")
        new_route, best_route, dms, best_dms = try_route( coords , new_route, dms , best_dms , best_route)
        return ' '.join(best_route[1:])
    else : return "Inserir um ponto de partida" 
def mark_points(coords, nx , ny , value):
    if value not in coords.keys() :
        coords[value] = [nx, ny]
    else : print('Estas coords já foram inseridas')
    return coords
"""