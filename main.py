from time import sleep
import AgFunctions as ag
from fitness import Fitness as fit
from parametro import Parametro
from propriedade import Propriedade
from populacao import Populacao

'''
qtdFunc = 0
while qtdFunc <= 0:
    print("\nQual a quantidade de funcionários atualmente?")
    qtdFunc = int(input("Digite: "))

qtdGado = 0
while qtdGado <= 0:
    print("\nQual a quantidade de cabeças de Gado?")
    qtdGado = int(input("Digite: "))

hrsConf = 0
while hrsConf <= 0:
    print("\nQual o tempo de confinamento em horas atualmente?")
    hrsConf = int(input("Digite: "))
    
codigo = 0
while codigo <= 0:
    print("\nDigite o código da propriedade ou pressione [ENTER] para cadastrar: ")
    codigo = int(input("Digite: "))
'''

# -------------------------------------------------------- --
# BLOCO 01 - DADOS DA PROPRIEDADE
# -------------------------------------------------------- --

PropId = 0
while PropId <= 0:
    # Cabecalho do Algoritmo
    ag.Common.GetHeader(0, 0)
    PropId = int(input("\nDigite o código da propriedade: "))

    if Propriedade.getData(PropId) == 0:
        print('Propriedade não encontrada...')
        sleep(2)
        PropId = 0
    else:
        propriedade = Propriedade.getData(PropId)
        # print(Propriedade.getData(PropId))

ParmId = 0
while ParmId <= 0:
    # Cabecalho do Algoritmo
    ag.Common.GetHeader(propriedade['propriedadeNome'], 0)
    ParmId = int(input("\nDigite o código do parâmetro: "))

    if Parametro.getData(ParmId) == 0:
        print('Parâmetro não encontrado...')
        sleep(2)
        ParmId = 0
    else:
        parametro = Parametro.getData(ParmId)
        # print(Parametro.getData(ParmId))

# -------------------------------------------------------- --
# BLOCO 02 - INICIALIZA A POPULAÇÃO
# -------------------------------------------------------- --

# Configuracao inicial para teste x = [4, 170, 15]
ag.Common.GetHeader(propriedade['propriedadeNome'], ParmId)
setPop = Populacao.setPopInicial(propriedade['propriedadeId'])
sleep(2)

ag.Common.GetHeader(propriedade['propriedadeNome'], ParmId)
tblPop = Populacao.getPopIncial(propriedade['propriedadeId'])
print(tblPop)
sleep(5)

# -------------------------------------------------------- --
# BLOCO 03 - SELEÇÃO DOS INDIVIDUOS
# -------------------------------------------------------- --

ag.Common.GetHeader(propriedade['propriedadeNome'], ParmId)

# REALIZA N INTERAÇÕES
qtdI = 100
for x in range(0, qtdI):
    selecao = Populacao.selecionar(propriedade['propriedadeId'], x + 1)
    indA = Populacao.buscaIndividuo(selecao[0], propriedade['propriedadeId'], x + 1)
    indB = Populacao.buscaIndividuo(selecao[1], propriedade['propriedadeId'], x + 1)

    indA = {'gado': indA[0], 'funcionario': indA[1], 'confinamento': indA[2]}
    indB = {'gado': indB[0], 'funcionario': indB[1], 'confinamento': indB[2]}

    print('INTERAÇÃO N. ', x + 1)
    print('Indivíduo ', selecao[0], ': ', indA)
    print('Indivíduo ', selecao[1], ': ', indB)

    # -------------------------------------------------------- --
    # BLOCO 04 - FITNESS
    # -------------------------------------------------------- --

    # -------------------------------------------------------- --
    # CALCULA RENDA TOTAL
    # Quantidade de gado POP | Valor do litro do leite | Dias do mes
    vRendaLeite = [indA['gado'], propriedade['precoLeite'], parametro['qtdDiasMes']]
    rendaLeite = fit.renda_leite(vRendaLeite)
    print('\nRenda do Leite:\n', vRendaLeite, ' => ', rendaLeite)

    # Quantidade de gado POP | Quantidade de Dejetos produzidos | Dias do mes
    # Quantidade de dejetos necessarios em kg | energia consumida em Kw/h
    # valor do Kw/h cobrado em reais

    #vBioFMes = [indA['confinamento'], parametro['qtdDejetos'], parametro['qtdDiasMes'], parametro['convertBioFer']]
    # rendaBioF = fit.biofertilizanteMes(vBioFMes)  # * parametro['precoBiofer']
    #print(vBioFMes)
    #print('\nRenda do Leite:\n', vBioFMes, ' => ', rendaBioF)

    #

# -------------------------------------------------------- --
# BLOCO 04 - RECOMBINAÇÃO
# -------------------------------------------------------- --


'''
ag.Common.GetHeader(0)
# Buscar parametros do Programa
parms = Parametro.getParm(1)
print(str(parms) + '\n\n')

# Informações da propriedade
propr = Propriedade.getData(codigo)

'''

## -------------------------------------
# Calcula Renda Total
## -------------------------------------




# Grava Melhor Invividuo

# Gera segunda populacao
# intermed.gera_pop(i)

# Recombinacao

# Mutacao

input("\nPressione [ENTER] para finalizar...")