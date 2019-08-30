import random as rd
from prettytable import PrettyTable
from AgFunctions import Common as common


# ----------------------------------- --
# CLASSE POPULACAO
# ----------------------------------- --
class Populacao(object):
    # ------------------------------- --
    # CADASTRA POPULAÇÃO INICIAL

    def setPopInicial(self):
        # ------------------------------- --
        # ABRE CONEXAO COM BANCO DE DADOS
        db = common.conexao(1)
        cursor = db.cursor()

        # PREPARA CONFIGURAÇÃO INICIAL COM BASE NOS DDOS DA PROPRIEDADE
        sql = "SELECT propriedadeId, qtdCabecaGado, qtdFuncionarios, hrsConfinamento FROM propriedade WHERE propriedadeId = " + str(
            int(self))
        try:
            cursor.execute(sql)
            tplProp = cursor.fetchone()
            dicProp = {'propriedadeId': tplProp[0], 'qtdCabecaGado': tplProp[1], 'qtdFuncionarios': tplProp[2],
                       'hrsConfinamento': tplProp[3]}
        except:
            print('\nPropriedade Inexistente')
        db.close()
        # ------------------------------- --


        # ------------------------------- --
        # ABRE CONEXAO COM BANCO DE DADOS
        db = common.conexao(1)
        cursor = db.cursor()

        # RETORNA A QUANTIDADE DE INDIVIDUOS DA POPULACAO INCIAL DA PROPRIEDADE
        sql = "SELECT count(id) FROM pop_inicial WHERE i = " + str(dicProp['propriedadeId']) + " ORDER BY id"
        try:
            cursor.execute(sql)
            listaInividuos = cursor.fetchone()
            qtdIndividuos = int(listaInividuos[0])
        except:
            print('\nErro ao contar população')
        db.close()
        # ------------------------------- --


        # ------------------------------- --
        # VERIFICA SE A POPULAÇÃO INICIAL ESTÁ COMPLETA - 30 INDIVIDUOS
        if qtdIndividuos == 30:
            print('\nPopulação Inicial já existe. Deseja atualizar os dados?')
            resp = (input('Sim/Nao: '))

        # REMOVE INDIVIVUOS, CASO EXISTAM REGISTROS INSUFICIENTES
        elif qtdIndividuos > 0 and qtdIndividuos < 30:

            resp = Populacao.remover(dicProp['propriedadeId'])

        # CASO NÃO EXISTA NENHUMA REGISTRO PARA A POPULAÇÃO INICIAL
        else:
            resp = 'S'
        # ------------------------------- --


        # ------------------------------- --
        # GERA POPULAÇÃO INICIAL PARA A PROPRIEDADE
        if resp.upper() == 'S' or resp.upper() == 'SIM':

            # ------------------------------- --
            # REMOVE DADOS ANTIGOS
            if qtdIndividuos > 0:
                rmv = Populacao.remover(dicProp['propriedadeId'])
            else:
                IsOk = True

            if rmv == 'S':
                IsOk = True
            else:
                print('\nErro ao remover população população antiga :(')
            # ------------------------------- --

            if IsOk == True:
                j = 0  # QTD DE INIDIVÍDUOS GERADOS

                # ------------------------------- --
                # ABRE CONEXAO COM BANCO DE DADOS
                db = common.conexao(1)
                cursor = db.cursor()

                # ------------------------------- --
                # ADICIONA NOVO INDIVÍDUO
                for x in range(0, 30):
                    y = x + 1

                    indMin = dicProp['qtdCabecaGado'] - (dicProp['qtdCabecaGado'] * 0.5)
                    indMax = dicProp['qtdCabecaGado'] + (dicProp['qtdCabecaGado'] * 0.5)
                    gado = rd.uniform(indMin, indMax)

                    indMin = dicProp['qtdFuncionarios'] - (dicProp['qtdFuncionarios'] * 0.5)
                    indMax = dicProp['qtdFuncionarios'] + (dicProp['qtdFuncionarios'] * 0.5)
                    funcionario = rd.uniform(indMin, indMax)

                    indMin = dicProp['hrsConfinamento'] - (dicProp['hrsConfinamento'] * 0.5)
                    indMax = dicProp['hrsConfinamento'] + (dicProp['hrsConfinamento'] * 0.5)
                    confinamento = rd.uniform(indMin, indMax)

                    sql = "INSERT INTO pop_inicial(id, gado, funcionario, confinamento, i)" \
                          "VALUES (" + str(y) + ", " + str(gado) + ", " + str(funcionario) + ", " + str(
                        confinamento) + "," \
                                        " " + str(dicProp['propriedadeId']) + ")"
                    try:
                        cursor.execute(sql)
                        db.commit()
                        j += 1
                    except:
                        db.rollback()
                        print('Não foi possível adicionar o indivíduo ', str(y))
                        # FIM DO FOR
                        # ------------------------------- --
                db.close()
            # ------------------------------- --

            if j == 30:
                print('\nPopulação atualizada com sucesso!')
                return True
            return False

        elif qtdIndividuos == 30:
            print('\nPopulação mantida!')
            return True
        else:
            # Mantendo População atual
            print('\nPopulação insuficiente')
            return False

        # ---

    # FIM DA FUNCAO setPopInicial()
    # ------------------------------- --

    # ------------------------------- --
    # RETORNA POPULAÇÃO INICIAL

    def getPopIncial(self):
        # STRING COM ERROS
        Error = 'Erros: '

        tblPop = PrettyTable(['#', 'Qtd. Gado', 'Funcionario', 'Hrs Confinamento'])

        # ------------------------------- --
        # ABRE CONEXAO COM BANCO DE DADOS
        db = common.conexao(1)
        cursor = db.cursor()

        # ------------------------------- --
        # RECUPERA DADOS DA POPULAÇÃO INICIAL DA PROPRIEDADE
        sql = "SELECT id, gado, funcionario, confinamento FROM pop_inicial WHERE i = " + str(self)
        try:
            cursor.execute(sql)
            tupla = cursor.fetchall()
            for x in range(0, len(tupla)):
                tblPop.add_row(list(tupla[x]))

        except:
            Error += 'Propriedade Inexistente/'
        db.close()

        return tblPop

    # FIM DA FUNCAO setPopInicial()
    # ------------------------------- --

    # ------------------------------- --
    # REMOVE POPULACAO INICIAL

    def remover(self):
        # ABRE CONEXAO COM BANCO DE DADOS
        db = common.conexao(1)
        cursor = db.cursor()

        # REMOVE REGISTROS INSUFICIENTES
        sql = "DELETE FROM pop_inicial WHERE i = " + str(int(self))
        try:
            cursor.execute(sql)
            db.commit()
            resp = 'S'
        except:
            db.rollback()
            resp = 'N'
        db.close()

        return resp

    # FIM DA FUNCAO REMOVER
    # ------------------------------- --

    # ------------------------------- --
    # SELEÇÃO POPULAÇÃO

    def selecionar(i, j):

        # SELECIONA INDIVIDUOS DIFERENTES
        IsOk = False
        while IsOk is False:
            selecao = [int(rd.uniform(0, 30)), int(rd.uniform(0, 30))]
            if not selecao[0] == selecao[1]:

                # ------------------------------- --
                # VERIFICA SE JÁ EXISTE FILHO COM OS PAIS SELECIONADOS
                sql = "SELECT COUNT(fa) FROM pop_intermediaria WHERE (indA = " + str(selecao[0]) + " OR indA = " + str(
                    selecao[1]) + ") AND (indB = " + str(selecao[0]) + " OR indB = " + str(
                    selecao[1]) + ") AND i = " + str(i) + " AND j = " + str(j)

                try:
                    # ABRE CONEXAO COM BANCO DE DADOS
                    db = common.conexao(1)
                    cursor = db.cursor()

                    cursor.execute(sql)
                    qtdInd = cursor.fetchone()
                    db.close()
                except:
                    print('Erro selecionar')

                if not int(qtdInd[0]) > 0:
                    IsOk = True

        return selecao
        # ----------------------------------- --
        # FIM DA FUNCAO selecionar


    # ------------------------------- --
    # SELEÇÃO DE INDIVÍDUOS
    def buscaIndividuo(id, prop, i):
        if i == 1:
            # SELECIONA INDIVÍDUO DE pop_inicial
            sql = "SELECT gado,funcionario,confinamento FROM pop_inicial WHERE id = " + str(id) + " AND i = " + str(
                prop)
            try:
                # ABRE CONEXAO COM BANCO DE DADOS
                db = common.conexao(1)
                cursor = db.cursor()

                cursor.execute(sql)
                ind = cursor.fetchone()
                db.close()
            except:
                print('Erro selecionar individuo em pop_inicial')

        else:
            # SELECIONA INDIVIDUO DE pop_intermediaria
            sql = "SELECT gado,funcionario,confinamento FROM pop_intermediaria WHERE id = " + str(
                id) + " AND i = " + str(prop) + " AND j = " + str(i)
            try:
                # ABRE CONEXAO COM BANCO DE DADOS
                db = common.conexao(1)
                cursor = db.cursor()

                cursor.execute(sql)
                ind = cursor.fetchone()
                db.close()
            except:
                print('Erro selecionar individuo em pop_inicial')

        return ind





    # ----------------------------------- --
    # TESTE DE CLASSE
    # ----------------------------------- --
    # result = Populacao.setPopInicial(1)
    # print(result)

    # result = Populacao.getPopIncial(1)
    # print(result)