## NÃO APENAS COMO REFERÊNCIA
import random as rd
from dbFunctions import dbClass
from fitness import Fitness

def var():
    ValLeit = 0.8  # valor do litro do leite | Propriedade
    DiasMes = 30  # qtd mes em dias | Parametro [ok]
    QtdDeje = 1.046  # dejeto produzido por animal em kg | parametro [ok]
    QtdDejBio = 25  # dejeto necessario em kg
    QtdKwh = 6.5  # energia consumida em Kw/h
    ValKwh = 0.31  # valor do Kw/h cobrado em reais | propriedade OK
    PerDecomp = 0.85  # porcentagem decomposta | parametro OK
    ValFert = 5  # valor fertilizante em litros
    QtdDejBio = 25  # dejeto necessario em kg1

    G_Energia = 5026.77  # Gasto energia da empresa

    P_Gado = 2500  # preço por cabeça de gado
    C_ManutGerador = 60  # custo mensal com manutenção do gerador
    C_ManutLagoa = 20  # custo mensal com manutenção da lagoa
    C_ManutBioD = 40  # custo mensal com manutenção do biodigestor

    C_ImpInstalacao = 80  # custo de construção da instalação de confinamento por cabeça de gado
    C_ImpBiodigestor = 150  # custo de construção do biodigestor por cabeça de gado
    C_ImpLagoa = 70  # custo de construção da lagoa por cabeça de gado
    C_ImpGerador = 100  # custo de implantação do gerador por cabeça de gado
    Potencia = 20  # Potencia instalada em Kw

    # CT = G_e + (C_f * x) + C_ger + C_biod + C_lag

    SalarioFunc = 3000  # Custo total com funcionarios
    C_Alimentacao = 21726  # custo alimentacao
    C_ManutInstalacao = 80  # custo mensal com manutenção do gerador

    # C_Funcionario = 3000
    QtdFunc = 4    # qtd de funcionarios
    QtdGado = 170  # qtd de gado
    HrsConf = 15   # hrs de confinamento


GadoMin = var.QtdGado - (var.QtdGado * 0.5)
GadoMax = var.QtdGado + (var.QtdGado * 0.5)

FuncMin = var.QtdFunc - (var.QtdFunc * 0.5)
FuncMax = var.QtdFunc + (var.QtdFunc * 0.5)

ConfMin = var.HrsConf - (var.HrsConf * 0.2)
ConfMax = var.HrsConf + (var.HrsConf * 0.2)

db = dbClass.abrir()
for x in range(0,29):
    gado = rd.uniform(GadoMin, GadoMax)
    funcionario = rd.uniform(FuncMin, FuncMax)
    confinamento = rd.uniform(ConfMin, ConfMax)


## MAIN
varA = [187, 90, 100] ## qtd gado
varB = [ 15,  6,   8] ## hrs confinamento
varC = [  3,  3,   5] ## qtd funcionarios
varS = [  0,  0,   0] ## status recombinar

posA = 0; posB = 1; R_leite = 0; R_biod = 0; R_biof = 0

individuoA = [varA[posA], varB[posA], varC[posA]]
individuoB = [varA[posB], varB[posB], varC[posB]]

V_Manut = [var.SalarioFunc, var.QtdFunc, var.QtdGado, individuoA[0], var.C_Alimentacao, var.C_ManutInstalacao, var.C_ManutGerador, var.C_ManutBioD, var.C_ManutLagoa]

C_Manut = Fitness.restricao_orcamento(V_Manut)
O_Manut = 35000  # orçamento previsto para manutenção

if(C_Manut <= O_Manut):
    Pcm = 0
    print('valor da Restrição: ', C_Manut, '\n\nNão quebrou!!', '\n\nPcm: ', Pcm)
else:
    Pcm = C_Manut - O_Manut
    print('valor da Restrição: ', C_Manut, '\n\nQuebrou!!', '\n\nPcm: ', Pcm)

# C_Inv = Fitness.restricao_investimento(V_Investimento)
# O_Inv =