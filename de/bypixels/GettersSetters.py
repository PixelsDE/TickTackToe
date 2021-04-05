import random
class GetterSetter():
    Spielfeld = [[], [], []]
    hoch = None
    breit = None
    letter = "X"
    debug = True
    filler = " "

    def getFiller(self):
        return self.filler


    def changeLetter(self):
        if self.letter == "X":
            self.setLetter("O")
        else:
            self.setLetter("X")

    def isDebug(self):
        return self.debug

    def setDebug(self):
        try:
            x = input("Debug?\n").lower()
            if x == "nein" or x=="false" or x=="no":
                self.debug = False
            elif(x == "ja" or x=="yes" or x=="true"):
                self. debug = True
            else:
                raise Exception
        except Exception:
            print("Please enter True, Ja, Yes or False | No, Nein!")
            self.setDebug()

    def setHoch_Breit(self, hoch, breit):
        self.hoch = hoch
        self.breit = breit

    def getHoch(self):
        return self.hoch

    def getLetter(self):
        return self.letter

    def setLetter(self, letter):
        self.letter = letter

    def getBreit(self):
        return self.breit

    def getSpielfeld(self):
        return self.Spielfeld

    def setStartLetter(self):
        self.letter = random.choice(("X", "Y"))


    def isSpielfeldFull(self):
        for a in range(0, 3):
            for b in range(0, 3):
                if (self.getSpielfeld()[a][b] == self.getFiller()):
                    return False
                else:
                    continue
        return True
