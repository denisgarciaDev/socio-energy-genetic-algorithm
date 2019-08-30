## NÃO APENAS COMO REFERÊNCIA
## Algoritmo genetico - Modelo
import random as rd
import numpy as np

## Inicializando vetores
rA = [0]; rB = [0]; rC = [0]; rS = [1]; qtd = 1
mA = [0]; mB = [0]; mC = [0]; mS = [1]

## Funcoes
def recombina(a, b, var):
    if var == 'ab':## primeira var com segunda
        aux = mB[a]
        mB[a] = mB[b]
        mB[b] = aux
    elif var == 'ac':## primeira var com terceira
        aux = mB[a]
        mB[a] = mB[b]
        mB[b] = aux
    elif var == 'bc':## segunda com terceira
        aux = mC[a]
        mC[a] = mC[b]
        mC[b] = aux


## Declara variaveis com margem min e max
varA_MinMax = [110, 90]
varB_MinMax = [10, 6]
varC_MinMax = [7, 3]

## Gerando populacao
for x in range(0, 30):
    ## Gera posicoes aleatorias
    varA = int(rd.uniform(varA_MinMax[0], varA_MinMax[1]))
    varB = int(rd.uniform(varB_MinMax[0], varB_MinMax[1]))
    varC = int(rd.uniform(varC_MinMax[0], varC_MinMax[1]))

    ## Adiciona linha na matriz
    mA = np.append(mA, [[varA]])
    mB = np.append(mB, [[varB]])
    mC = np.append(mC, [[varC]])
    mS = np.append(mS, [[False]])

print(mA, '\n', mB, '\n', mC)

posA = round(rd.uniform(1, 30), 0)
posB = round(rd.uniform(1, 30), 0)

print(posA, posB)

indA = [int(varA[posA]), varB[posA], varC[posA]]
indB = [int(varA[posB]), varB[posB], varC[posB]]

#print('individuo A: ', indA)
print('individuo B: ', indB)

'''

## Recombinar
while qtd >= 0:
    recombinar = False
    while not recombinar:
        ## Selecionar individuos
        posA = int(rd.uniform(0, 30))
        posB = int(rd.uniform(0, 30))

        if posA != posB:
            if mS[posA] == 0 and mS[posB] == 0:
                recombinar = True
                recombina(posA, posB, 1)

                qtd -= 1

# Gera populacao
PopTemps = []
for x in range(0, 30):
    tempPop = random.uniform(tempMin,tempMax)
    tempPop = round(tempPop, 2)
    #print('Temp: ' + str(tempPop))
    PopTemps += [tempPop]
    
    
table =  [
# grid: 4 by 9
# 1   2   3   4
['A','B','C','D'],#1
['E','F','G','H'],#2
['I','J','K','L'],#3
['M','N','O','P'],#4
['Q','R','S','T'],#5
['U','V','W','X'],#6
['Y','Z','1','2'],#7
['3','4','5','5'],#8
['7','8','9','0'],#9
]
print(table[1][2], table[4][3])

print(table)
'''
