import random


class TickTackToe():

    def Use(self, hoch, breit):
        if util.getField(hoch, breit) != getterSetter.getFiller():
            print("Error, das Feld geht nicht! Bereits belegt! Nimm ein anderes!")
            tickTackToe.userInput()
            return
        # Feld ist frei
        tickTackToe.modifySpielFeld(hoch, breit, getterSetter.getLetter())
        getterSetter.changeLetter()
        if util.isBot():
            tickTackToe.botInput()
        if (not util.isEnd()):
            util.printSpielfeld()

    def modifySpielFeld(self, hoch, breit, letter):
        spielfeld = getterSetter.getSpielfeld()
        liste = spielfeld[hoch]
        liste[breit] = letter
        #check if the game would end!
        util.checkWinning(getterSetter.getLetter())

    # Random Field selected if Free than put Latter in there if not repeat!
    def botInput(self):
        if (getterSetter.isSpielfeldFull()):
            return
        fieldSlot = random.randrange(1, 10)
        hoch = util.getFieldSlotByValues(fieldSlot)[0]
        breit = util.getFieldSlotByValues(fieldSlot)[1]
        while (util.getField(hoch, breit) != getterSetter.getFiller()):
            fieldSlot = random.randrange(1, 10)
            hoch = util.getFieldSlotByValues(fieldSlot)[0]
            breit = util.getFieldSlotByValues(fieldSlot)[1]
        self.modifySpielFeld(hoch, breit, getterSetter.getLetter())
        getterSetter.changeLetter()
    def userInput(self):
        try:
            x = list(map(int, input("dein Feld mit eintragen mit Hoch (Zahl) Max. 3, Breit (Zahl) Max. 3! \n").split(",")))
            a = x[0] - 1
            b = x[1] - 1
            getterSetter.setHoch_Breit(a, b)
            self.Use(getterSetter.getHoch(), getterSetter.getBreit())
        except Exception as exception:
            if (getterSetter.isDebug()):
                print(__name__)
                print(exception)
            self.userInput()

    def main(self):
        getterSetter.setDebug()
        # Soll mit oder Ohne Bot gespielt werden?! (Single vs. Multiplayer)
        util.withBot()
        getterSetter.setStartLetter()
        util.fillSpielfeld()
        util.printSpielfeld()
        while (not util.isEnd()):
            self.userInput()


from de.bypixels.GettersSetters import GetterSetter
getterSetter = GetterSetter()
tickTackToe = TickTackToe()
if __name__ == '__main__':
    from de.bypixels.Util import Util
    util = Util()
    tickTackToe.main()
