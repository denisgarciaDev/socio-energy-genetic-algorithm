import random as rd
from AgFunctions import Common as common


class popInicial(object):

    def gera_pop(self):
        i = self[3]  # Id da Propriedade
        j = 0        # qtd de individuos gerados

        QtdFunc = self[0]
        QtdGado = self[1]
        HrsConf = self[2]

        GadoMin = QtdGado - (QtdGado * 0.5)  # Quantidade Mínima de Gado
        GadoMax = QtdGado + (QtdGado * 0.5)  # Quantidade Máxima de Gado

        FuncMin = QtdFunc - (QtdFunc * 0.5)  # Quantidade Mínima de Funcionários
        FuncMax = QtdFunc + (QtdFunc * 0.5)  # Quantidade Máxima de Funcionários

        ConfMin = HrsConf - (HrsConf * 0.2)  # Qtd. Mínima de Horas de Confinamento
        ConfMax = HrsConf + (HrsConf * 0.2)  # Qtd. Máxima de Horas de Confinamento

        db = common.conexao(1)
        cursor = db.cursor()

        sql = "SELECT count(id) FROM pop_inicial WHERE i = " + str(i) + " ORDER BY id"
        cursor.execute(sql)
        listaInividuos = cursor.fetchone()
        qtdIndividuos = int(listaInividuos[0])

        if qtdIndividuos > 0:
            print('\nPopulação Inicial já existe!\nDeseja atualizar os dados?')
            resp = (input('Sim/Nao: '))
        else:
            resp = 'S'

        if resp.upper() == 'S' or resp.upper() == 'SIM':
            # Gerando nova população
            for x in range(0, 30):
                y = x + 1

                gado = rd.uniform(GadoMin, GadoMax)
                funcionario = rd.uniform(FuncMin, FuncMax)
                confinamento = rd.uniform(ConfMin, ConfMax)

                # prepare a cursor object using cursor() method
                cursor = db.cursor()

                # Prepare SQL query to UPDATE required records
                sql = "INSERT INTO pop_inicial(id, gado, funcionario, confinamento, i) VALUES (" + str(
                    y) + ", " + str(gado) + ", " + str(
                    funcionario) + ", " + str(confinamento) + ", " + str(i) + ")"
                try:
                    # Execute the SQL command
                    cursor.execute(sql)
                    # Commit your changes in the database
                    db.commit()
                    j = j + 1
                except:
                    # Rollback in case there is any error
                    db.rollback()

            # Gerando nova população
            print('\nPopulação Gerada com Sucesso!')



        else:
            # Mantendo População atual
            print('\nA população existente foi mantida.')

        # disconnect from server
        db.close()