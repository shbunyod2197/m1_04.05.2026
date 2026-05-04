class Ota:
    def __init__(self, fulname):
        self.fulname = fulname
        self.__money = 0

    def pul_qosh(self, t_pul):
        self.__money += t_pul

    def info(self):
        print(f"Egasi: {self.fulname}")
        print(f"Pul: {self.__money}")


o1 = Ota("ali vali")

o1.pul_qosh(1)
o1.info()
