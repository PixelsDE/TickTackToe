class TickTackToe():

    def inUse(self, hoch, breit):
        if subFileTwo.getField(hoch, breit) != None:
            print("Error, das Feld geht nicht! Bereits belegt! Nimm ein anderes!")
            self.userInput()
            return
        global letter
        if subFile.UserWechsel:
            letter ="O"
            subFile.UserWechsel = False
        else:
            letter = "X"
            subFile.UserWechsel = True
        #Feld ist frei
        spielfeld = subFile.getSpielfeld()
        liste = spielfeld[hoch]
        liste[breit] = letter
        subFileTwo.printSpielfeld()
        subFileTwo.checkWinning(letter)

    def userInput(self):
        try:
            x = list(map(int, input("dein Feld mit eintragen mit Hoch (Zahl) Max. 3, Breit (Zahl) Max. 3! \n").split(",")))
            a = x[0]
            b = x[1]
            subFile.setHoch_Breit(x[0]-1, x[1]-1)
            self.inUse(x[0] - 1, x[1] - 1)
        except Exception:
            self.userInput()

    def main(self):
        subFileTwo.fillSpielfeld()
        subFileTwo.printSpielfeld()
        while(not subFileTwo.getEnd()):
            self.userInput()

from de.bypixels.GettersSetters import GetterSetter
subFile = GetterSetter()

if __name__=='__main__':
    from de.bypixels.Util import testTwo
    tickTackToe = TickTackToe()
    subFileTwo = testTwo()
    tickTackToe.main()