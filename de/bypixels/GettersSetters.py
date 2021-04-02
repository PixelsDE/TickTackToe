
class GetterSetter():
    Spielfeld = [[], [], []]
    hoch = None
    breit = None
    letter = "X"
    debug = False

    def changeLetter(self):
        if self.letter == "X":
            self.setLetter("O")
        else:
            self.setLetter("X")

    def isDebug(self):
        return self.debug

    def setDebug(self, debug):
        self.debug = debug
    def setHoch_Breit(self, hoch, breit):
        self.hoch = hoch
        self.breit = breit

    def getHoch(self):
     return  self.hoch

    def getLetter(self):
        return self.letter
    def setLetter(self, letter):
        self.letter = letter
    def getBreit(self):
        return self.breit
    def getSpielfeld(self):
        return self.Spielfeld

    def isSpielfeldFull(self):
        for a in range(0, 3):
            for b in range(0, 3):
                if (self.getSpielfeld()[a][b] ==  None):
                    return False
                else:
                    continue
        return True