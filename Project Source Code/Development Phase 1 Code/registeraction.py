
from DBConnection import DBConnection

class RegisterAction:

    def datacheck(self,name, email, contact,city, pwd):
        if name == "" or email == "" or contact == "" or city == "" or pwd == "":
            return True
        else:
            return False

    @staticmethod
    def signup(name, email, contact,city, pwd):
        print(name, email, contact,city, pwd)
        database = DBConnection.getConnection()
        cursor = database.cursor()
        query = "insert into users values(%s,%s,%s,%s,%s)"
        values = (name, email, contact,city, pwd)
        print(values)
        cursor.execute(query, values)
        database.commit()
        # rows=str(sheet.nrows)
        print("inserted")
        return True

if __name__ == "__main__":
    RegisterAction.signup("sss","ss","ss","ss","ss")
