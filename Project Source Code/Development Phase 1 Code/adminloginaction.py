

class AdminLoginCheck:

    def datacheck(self,uid,pwd):
        if uid == "" and pwd == "":
            return True
        else:
            return False
    @staticmethod
    def logincheck(uid,pwd):
        if uid == "admin" and pwd == "admin":
            return True
        else:
            return False
