ipadresse = "127.0.0.1"
brugernavn = "root"
brugerpw = "alle1sql2specialister!"
mindatabase = "northwind"

class MySecrets:
    def __init__(self):
        self.name =  brugernavn
        self.pw = brugerpw
        self.mindb = mindatabase
        self.dbIP = ipadresse