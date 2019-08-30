import random as rd

##Funcoes
'''
def recombinar(posA, posB):

    ## recombinar
    torneio = rd.uniform(0, 1)
    if torneio <= 0.75:
        escolha = int(rd.uniform(1, 3))

        print('recombinar', torneio, '\nVariavel: ', escolha)

        if escolha == 1:
            aux = varA[posA]
            varA[posA] = varA[posB]
            varA[posB] = aux

        if escolha == 2:
            aux = varB[posA]
            varB[posA] = varB[posB]
            varB[posB] = aux

        if escolha == 3:
            aux = varC[posA]
            varC[posA] = varC[posB]
            varC[posB] = aux

    recombinado = [varA, varB, varC]
    return recombinado
'''

## MAIN
varA = [110, 90, 100] ## qtd gado
varB = [ 10,  6,   8] ## hrs confinamento
varC = [  7,  3,   5] ## qtd funcionarios
varS = [  0,  0,   0] ## status recombinar

posA = 0
posB = 1

print(varA, '\n', varB, '\n', varC, '\n')

## recombinação
def recombinacao(self):
    torneio = rd.uniform(0, 1)
    if torneio <= 0.5:
        escolha = int(rd.uniform(1, 3))

        print('recombinar', torneio, '\nVariavel: ', escolha)

        if escolha == 1:
            aux = varA[posA]
            varA[posA] = varA[posB]
            varA[posB] = aux

        if escolha == 2:
            aux = varB[posA]
            varB[posA] = varB[posB]
            varB[posB] = aux

        if escolha == 3:
            aux = varC[posA]
            varC[posA] = varC[posB]
            varC[posB] = aux

    vRecombinacao = [varA, varB, varC]
    return vRecombinacao


# Mutação
def mutacao(self):
    torneio = rd.uniform(0, 1)
    if torneio <= 0.5:
        escolha = int(rd.uniform(1, 3))

        print('recombinar', torneio, '\nVariavel: ', escolha)

        if escolha == 1:
            aux = varA[posA]
            varA[posA] = varA[posB]
            varA[posB] = aux

        if escolha == 2:
            aux = varB[posA]
            varB[posA] = varB[posB]
            varB[posB] = aux

        if escolha == 3:
            aux = varC[posA]
            varC[posA] = varC[posB]
            varC[posB] = aux

    vMutacao = [varA, varB, varC]
    return vMutacao
