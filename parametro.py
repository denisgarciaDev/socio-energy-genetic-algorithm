# Classe Parametros
from AgFunctions import Common as common


class Parametro():
    # Retorna parametros cadastrados a partir de um ID
    def getData(self):
        # buscar parametros
        db = common.conexao(1)
        cursor = db.cursor()

        sql = "SELECT * FROM parametro WHERE ParmId = " + str(self) + " ORDER BY ParmId"
        cursor.execute(sql)
        tupla = cursor.fetchone()
        db.close()

        dicionario = {
            'parmId': tupla[0],
            'qtdDejetos': tupla[1],
            'qtdDiasMes': tupla[2],
            'convertBiogas': tupla[3],
            'convertBioFer': tupla[4],
            'convertBioEne': tupla[5],
            'precoBiofer': tupla[6],
            'custoManutGerador': tupla[7],
            'custoManutLagoa': tupla[8],
            'custoManutBiod': tupla[9],
            'custoManutConf': tupla[10],
            'custoImplaConf': tupla[11],
            'custoImplaBiod': tupla[12],
            'custoImplaLagoa': tupla[13],
            'custoImplaGerador': tupla[14]
        }
        # retorna dados convertidos em dicionario
        return dicionario


    # Edita ou adiciona nova parametrizacao
    def setData(self):

        db = common.conexao(1)
        cursor = db.cursor()

        # Inserir nova parametrizacao
        sql = "INSERT INTO parametro (qtdDejetos, qtdDiasMes, convertBiogas, convertBioFer, convertBioEne) " \
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

    def edtParm(self):
        pass


# -------------------------
# TESTES DA CLASSE
# -------------------------

'''
dados = (1.075, 30, 25, 0.85, 6.5)
cadParametro = Parametro.setParm(dados)
print(cadParametro)
'''

'''
parms = Parametro.getData(1)
print(parms)
'''