
class GetterSetter():

    Spielfeld = [[], [], []]
    UserWechsel = False
    hoch = None
    breit = None

    def isUserWechsel(self):
        return self.UserWechsel

    def setHoch_Breit(self, hoch, breit):
        self.hoch = hoch
        self.breit = breit

    def getHoch(self):
     return  self.hoch

    def getBreit(self):
        return self.breit
    def getSpielfeld(self):
        return self.Spielfeld

