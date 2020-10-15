
from DBConnection import DBConnection

class UserLoginCheck:

    def datacheck(self,uid,pwd):
        if uid == "" and pwd == "":
            return True
        else:
            return False
    @staticmethod
    def logincheck(uid,pwd):
        print(uid,pwd)
        database = DBConnection.getConnection()
        cursor = database.cursor()
        cursor.execute("select name from users where email='"+uid+"' and pwd='"+pwd+"' ")
        if cursor.fetchone() is not None:
            print("login success")
            return True
        else:
            return False
