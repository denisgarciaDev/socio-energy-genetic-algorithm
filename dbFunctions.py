import pymysql

class dbClass(object):

    def abrir(self):
        # Open database connection
        db = pymysql.connect("localhost", "root", "vertrigo", "ag")
        return db