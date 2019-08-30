class Fitness(object):
    # INÍCIO DAS FUNÇÕES
    # --------------------------------------------------- --

    # Calculo de restricao de investimento
    def restricao_investimento(self):
        InvGado = self[0]  # Preco da cabeca de gado                            | PROPRIEDADE
        InvConf = self[1]  # Investimeto com instalacao confinamento por cabeca | PROPRIEDADE
        InvBiod = self[2]  # Preco do Biodigestor por Cabeca                    | PROPRIEDADE OU PARAMETRO
        InvGera = self[3]  # Preco do Gerador por cabeca                        | PROPRIEDADE OU PARAMETRO
        InvLago = self[4]  # Preco da lagoa por cabeca                          | PROPRIEDADE OU PARAMETRO
        QtdGado = self[5]  # Quantidade de Gado que ja possui                   | PROPRIEDADE OU PARAMETRO
        InvQtdG = self[6]  # Quantidade de Gado                                 | POPULACAO

        return ((InvGado + InvConf + InvBiod + InvGera + InvLago) * InvQtdG) - (InvGado * QtdGado)

    # calcula a quantidade de biomassa produzida
    def biomassaMes(self):
        ConfHra = self[0]  # Horas de confinamento            | PROPRIEDADE OU POPULACAO
        QtdDeje = self[1]  # Quantidade de Dejetos produzidos | PARAMETRO [OK]
        DiasMes = self[2]  # Dias do mês                      | PARAMETRO [OK]

        return ConfHra * QtdDeje * DiasMes

    # calcula a quantidade de biogás (m³) produzida por cabeça de gado por mês
    def biogasMes(self):
        biomassaMes = Fitness.biomassaMes(self)
        ConBioM = self[3]  # quantidade de dejetos (kg) necessária para produzir 1m³ | PARAMETRO [OK] convertBiogas

        return biomassaMes / ConBioM

    # quantidade de biofertilizante produzido por mês por cabeça
    # Ao digerir a matéria orgânica há uma perda de 10 a 20% de matéria
    def biofertilizanteMes(self):
        v = [self[0], self[1], self[2]]
        biomassaMes = Fitness.biomassaMes(v)
        ConBioF = self[3]  # % Material digerido com a perda  | PARAMETRO [OK] convertBiofer

        return biomassaMes * ConBioF

    def energiaMes(self):
        ConfHra = self[0]  # Horas de confinamento                           | POPULACAO
        QtdDeje = self[1]  # Qtd de Dejetos produzidos                       | PARAMETRO [OK] qtdDejetos
        DiasMes = self[2]  # Dias do mês                                     | PARAMETRO [OK] qtdDiasMes
        ConBioM = self[3]  # Qtd. de dejetos (kg) necessária p/ produzir 1m³ | PARAMETRO [OK] convertBiogas
        ConBioE = self[4]  # kW que cada m³ de biogás produz                 | PARAMETRO [OK] convertBioEne

        return ((ConfHra * QtdDeje * DiasMes) / ConBioM) * ConBioE

    # Orcamento manutencao geral
    def restricao_orcamento(self):
        SalFunc = self[0]  # Valor total da folha de pagamento dos funcionarios  | PROPRIEDADE
        QtdFunc = self[1]  # Quantidade de funcionarios                          | PROPRIEDADE
        QtdGado = self[2]  # Quantidade de Gado                                  | PROPRIEDADE
        CstAlim = self[3]  # Custo total com alimentacao                         | PROPRIEDADE
        CstConf = self[4]  # Custo total com manutencao do local de confinamento | PROPRIEDADE
        CstGera = self[5]  # Custo total com manutencao do gerador               | CALCULO
        CstBiod = self[6]  # Custo total com manutencao do biodigestor           | CALCULO
        CstLago = self[7]  # Custo total com manutencao da lagoa                 | CALCULO

        QtdGPop = self[8]  # Quantidade de Gado (populacao)

        CstFunc = (SalFunc / QtdFunc) * (QtdFunc / QtdGado)
        CstAlim = CstAlim / QtdGado
        CstConf = CstConf / QtdGado

        print('C_Funcionario: ', CstFunc, '\nC_Alimentacao: ', CstAlim, '\nC_ManutInstalacao: ', CstConf)
        # retorna
        return (CstFunc + CstAlim + CstConf) * QtdGPop + CstGera + CstBiod + CstLago

    # renda obtida com o leite
    def renda_leite(self):
        QtdGado = self[0]  # Quantidade de gado      | POPULACAO
        ValLeit = self[1]  # Valor do litro do leite | PROPRIEDADE
        DiasMes = self[2]  # Dias do mes             | PARAMETRO

        QtdLeite = QtdGado * 10  # qtd total de leite produzido, sendo 10 a qtd de litros produzidas por cabeça

        return ValLeit * QtdLeite * DiasMes

    # renda obtida com o biodigestor
    def renda_biodigestor(self):
        QtdGado = self[0]  # Quantidade de gado                      | POPULACAO
        QtdDeje = self[1]  # Quantidade de Dejetos produzidos        | PARAMETRO
        DiasMes = self[2]  # Dias do mes                             | PARAMETRO [ok]
        QtdDejB = self[3]  # Quantidade de dejetos necessarios em kg | PARAMETRO [ok]
        QtdeKwh = self[4]  # energia consumida em Kw/h               | PROPRIEDADE
        ValrKwh = self[5]  # valor do Kw/h cobrado em reais          | PROPRIEDADE

        return round((((QtdGado * QtdDeje * DiasMes) / QtdDejB) * QtdeKwh) * ValrKwh, 2)

    # renda obtida pelo biofertilizante
    def renda_biofertilizante(self):
        v = [self[0], self[1]]
        bioFMes = Fitness.biofertilizanteMes(v)
        ValFert = self[2]  # valor fertilizante em litros            | PROPRIEDADE

        return round((bioFMes * ValFert), 2)