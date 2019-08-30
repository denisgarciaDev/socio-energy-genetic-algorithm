import random as rd
import pymysql as pms

class popIntermediaria(object):
    def gera_pop(self):
        # Abre conexao com banco
        db = pms.connect("localhost", "root", "vertrigo", "ag")  # Abre conexao com Banco
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        i = self  # Iteracao
        try:
            # Execute the SQL command
            sql = "SELECT COUNT(*) FROM pop_intermediaria WHERE i = " + str(i)
            cursor.execute(sql)
            c = cursor.fetchone()
            x = int(c[0])
        except:
            print("Erro Count")

        while x <= 28:
            ok = False  # individuos diferentes
            indB = 0  # inicializa variavel

            indA = int(rd.uniform(1, 30))
            while not ok:
                indB = int(rd.uniform(1, 30))
                if indA != indB:
                    ok = True

            print(indA, indB)
            ok = False

            try:
                # Execute the SQL command
                sqlA = "SELECT * FROM pop_inicial WHERE id = %s"
                sqlB = "SELECT * FROM pop_inicial WHERE id = %s"
                cursor.execute(sqlA, indA)
                resultA = cursor.fetchone()
                print(resultA)

                cursor.execute(sqlB, indB)
                resultB = cursor.fetchone()
                print(resultB)
            except:
                print('Erro')

            sql = "SELECT * FROM pop_intermediaria WHERE (indA = %a AND indB = %b) OR (indA = %b AND indB = %a)"
            try:
                cursor.execute(sql, resultA[0], resultB[0])
                result = cursor.fetchone()
                print(result)
            except:
                # Individuo intermediario nao existe
                ok = True

            if ok is True:
                sqlA = "INSERT INTO pop_intermediaria (indA, indB, gado, funcionario, confinamento, i) VALUES (" + str(
                    resultA[0]) + ", " + str(resultB[0]) + ", " + str(resultA[1]) + ", " + str(resultA[2]) + ", " + str(
                    resultA[3]) + ", " + str(resultA[4]) + ")"

                sqlB = "INSERT INTO pop_intermediaria (indA, indB, gado, funcionario, confinamento, i) VALUES (" + str(
                    resultB[0]) + ", " + str(resultA[0]) + ", " + str(resultB[1]) + ", " + str(resultB[2]) + ", " + str(
                    resultB[3]) + ", " + str(resultB[4]) + ")"
                try:
                    cursor.execute(sqlA)
                    cursor.execute(sqlB)
                    db.commit()
                    print('Cadastrado com Sucesso')
                except:
                    print('Erro de Insert')
                    db.rollback()

            try:
                # Execute the SQL command
                sql = "SELECT COUNT(*) FROM pop_intermediaria WHERE i = " + str(i)
                cursor.execute(sql)
                c = cursor.fetchone()
                x = int(c[0])
            except:
                print("Erro Count")

        print('População Intermediária gerada com sucesso!')
        # fecha conexao
        db.close()

'''
    
    def conta_pop(self):
        # Abre conexao com banco
        db = pms.connect("localhost", "root", "vertrigo", "ag")  # Abre conexao com Banco
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        try:
            # Execute the SQL command
            sql = "SELECT COUNT(*) FROM pop_intermediaria WHERE i = " + str(self)
            cursor.execute(sql)
            c = cursor.fetchone()
            x = int(c[0])
        except:
            print("Erro Count")

        return x

    def gera_pop(self):
        # Abre conexao com banco
        db = pms.connect("localhost", "root", "vertrigo", "ag")  # Abre conexao com Banco
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        while self <= 28:
            ok = False  # individuos diferentes
            indB = 0  # inicializa variavel

            indA = int(rd.uniform(1, 30))
            while not ok:
                indB = int(rd.uniform(1, 30))
                if indA != indB:
                    ok = True

            print(indA, indB)
            ok = False

            try:
                # Execute the SQL command
                sqlA = "SELECT * FROM pop_inicial WHERE id = %s"
                sqlB = "SELECT * FROM pop_inicial WHERE id = %s"
                cursor.execute(sqlA, indA)
                resultA = cursor.fetchone()
                print(resultA)

                cursor.execute(sqlB, indB)
                resultB = cursor.fetchone()
                print(resultB)
            except:
                print('Erro')

            sql = "SELECT * FROM pop_intermediaria WHERE (indA = %a AND indB = %b) OR (indA = %b AND indB = %a)"
            try:
                cursor.execute(sql, resultA[0], resultB[0])
                result = cursor.fetchone()
                print(result)
            except:
                # Individuo intermediario nao existe
                ok = True

            if ok:
                sqlA = "INSERT INTO pop_intermediaria (indA, indB, gado, funcionario, confinamento, i) VALUES (" + str(
                    resultA[0]) + ", " + str(resultB[0]) + ", " + str(resultA[1]) + ", " + str(resultA[2]) + ", " + str(
                    resultA[3]) + ", " + str(resultA[4]) + ")"

                sqlB = "INSERT INTO pop_intermediaria (indA, indB, gado, funcionario, confinamento, i) VALUES (" + str(
                    resultB[0]) + ", " + str(resultA[0]) + ", " + str(resultB[1]) + ", " + str(resultB[2]) + ", " + str(
                    resultB[3]) + ", " + str(resultB[4]) + ")"
                try:
                    cursor.execute(sqlA)
                    cursor.execute(sqlB)
                    db.commit()
                    print('Cadastrado com Sucesso')
                except:
                    print('Erro de Insert')
                    db.rollback()

        #fecha conexao
        db.close()

'''