from de.bypixels.TickTackToe import *


class Util():
    end = False
    bot = False

    def setBot(self, boolean):
        self.bot = boolean

    def isBot(self):
        return self.bot

    def fillSpielfeld(self):
        x = getterSetter.getSpielfeld()
        # [ [], [] , [] ]
        for item in x:
            # die einzelnen reihen
            for slot in range(3):
                # slots 0, 1, 2
                # item.append("-")
                # item = object in the list
                item.insert(slot, getterSetter.getFiller())

    def isEnd(self):
        return self.end

    def setEnd(self, end):
        self.end = end

    # todo: hier checken wies weitergeht!
    def checkWinning(self, letter):
        #had a bug -> not checked for correction
        for number in range(1, 4):
            if (self.getFieldCombi((number, 1)) == letter and self.getFieldCombi((number, 2)) ==  letter and self.getFieldCombi((number, 3)) == letter):
                self.setEnd(True)
                self.printSpielfeld()
                print("game done! " + letter + " hat gewonnen! ")
                exit()
                return
            elif (self.getFieldCombi((1, number)) == letter and self.getFieldCombi((2, number)) == letter and self.getFieldCombi((3, number)) == letter):
                self.printSpielfeld()
                print("Game done! " + letter + " hat gewonnen! ")
                self.setEnd(True)
                exit()
                return
            elif (self.getFieldCombi((1, 1)) == letter and self.getFieldCombi((2, 2)) == letter and self.getFieldCombi((3, 3)) == letter):
                self.printSpielfeld()
                print("game done! " + letter + " hat gewonnen! ")
                self.setEnd(True)
                exit()
                return
            elif (self.getFieldCombi((1, 3)) == letter and self.getFieldCombi((2, 2)) == letter and self.getFieldCombi((3, 1)) == letter):
                self.printSpielfeld()
                print("game done! " + letter + " hat gewonnen! ")
                self.setEnd(True)
                exit()
                return
            elif (self.getFieldCombi((1, 2)) == "X" and self.getFieldCombi((2, 2)) == "X" and self.getFieldCombi((3, 2)) == "X"):
                print("END!")

            elif (getterSetter.isSpielfeldFull()):
                self.printSpielfeld()
                print("es gibt keinen Gewinner!")
                self.setEnd(True)
                exit()
                #self.wipeSpielfeld()
                return
            else:
                return

    # still buggy have to be fixed sometime
    # def playagain(self):
    #     if (bool(input("nochmal spielen? \n"))):
    #         self.setend(false)
    #         self.withbot()
    #         ticktacktoe.main()

    def wipeSpielfeld(self):
        for a in range(0, 3):
            for b in range(0, 3):
                tickTackToe.modifySpielFeld(a, b, None)

    def printSpielfeld(self):
        for reihe in getterSetter.getSpielfeld():
            print(reihe)

    def getField(self, hoch, breit):
        return getterSetter.getSpielfeld()[hoch][breit]

    def getFieldCombi(self, combi):
        a = combi[0] - 1
        b = combi[1] - 1
        return getterSetter.getSpielfeld()[a][b]

    def withBot(self):
        try:
            x = str(input("\nmit o. ohne bot?!\n")).lower()
            if x == "ja" or x == "mit":
                print("es wird nun mit dem bot gespielt! \n")
                self.setBot(True)
            elif x == "nein" or x == "ohne":
                print("es wird nun ohne den bot gespielt! \n")
                self.setBot(False)
            else:
                print("bitte gib ja oder nein ein!")
                self.withBot()
        except Exception as exception:
            if (getterSetter.isdebug()):
                print(exception)
            print("bitte gib nur ja / mit oder nein / ohne ein!")
            self.withBot()

    def getFieldSlotByValues(self, value):
        if value < 4:
            number_a = 0
            number_b = value - 1
        elif value < 7:
            number_a = 1
            number_b = value - 4
        else:
            number_a = 2
            number_b = value - 7
        return (number_a, number_b)
