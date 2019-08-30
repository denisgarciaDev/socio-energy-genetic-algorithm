# Classe Propriedade
from AgFunctions import Common as common

class Propriedade():

    # Retorna propriedades cadastrados a partir de um ID
    def getData(self):

        sql = "SELECT * FROM propriedade WHERE PropriedadeId = " + str(self) + " ORDER BY PropriedadeId"
        try:
            # buscar propriedades
            db = common.conexao(1)
            cursor = db.cursor()

            cursor.execute(sql)
            tupla = cursor.fetchone()
            dicionario = {
                'propriedadeId': tupla[0],
                'propriedadeNome': tupla[1],
                'hrsConfinamento': tupla[2],
                'qtdCabecaGado': tupla[3],
                'precoCabecaGado': tupla[4],
                'custoAlimentacao': tupla[5],
                'qtdLeite': tupla[6],
                'precoLeite': tupla[7],
                'qtdFuncionarios': tupla[8],
                'salarioFuncionarios': tupla[9],
                'gastoEnergia': tupla[10],
                'valorKw': tupla[11],
                'orcamentoManut': tupla[12]
            }

        except:
            dicionario = 0

        db.close()

        # retorna dados convertidos em dicionario
        return dicionario

    # Edita ou adiciona nova parametrizacao
    def setData(self):

        db = common.conexao(1)
        cursor = db.cursor()

        # Inserir nova parametrizacao
        sql = "INSERT INTO propriedade (qtdDejetos, qtdDiasMes, convertBiogas, convertBioFer, convertBioEne) " \
              "VALUES (" + str(self[0]) + ", " + str(self[1]) + ", " + str(self[2]) + "," + str(
            self[3]) + "," + str(self[4]) + ");"

        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
            retorno = 'Parâmetro cadastrado com sucesso.'
        except:
            # Rollback in case there is any error
            db.rollback()
            retorno = 'Erro. Confira os dados inseridos.'

        db.close()
        return retorno

    def edtData(self):
        pass


# -------------------------
# TESTES DA CLASSE
# -------------------------

'''
dados = (1.075, 30, 25, 0.85, 6.5)
cadpropriedade = propriedade.setParm(dados)
print(cadpropriedade)
'''

'''
propriedade = Propriedade.getData(1)
print(propriedade)
'''
