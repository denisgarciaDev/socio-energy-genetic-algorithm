# --------------------------------------------------
# Projeto: Algoritmo Genético
# Autor: Denis Henrique Garcia Bonafé
# --------------------------------------------------
import os
import pymysql as pms

# Dados para otimização e parâmetros de entrada
class Common(object):

    # Abre Conexao
    def conexao(self):
        if self == 1:
            db = pms.connect("localhost", "root", "vertrigo", "ag")  # Abre conexao com Banco
        return db

    # Cabeçalho do Programa
    def GetHeader(PropNom, ParmId):

        os.system('cls' if os.name == 'nt' else 'clear')
        print("------------------------------------------------------------------------")
        print("                           Algoritmo Genético                           ")
        print("------------------------------------------------------------------------")
        print(" Propriedade: ", PropNom if not PropNom == 0 else '')
        print(" Parâmetro:   ", ParmId if not ParmId == 0 else '')
        print("------------------------------------------------------------------------")