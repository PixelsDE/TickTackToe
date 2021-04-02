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
                item.append(None)

    def isEnd(self):
        return self.end

    def setEnd(self, end):
        self.end = end




#TODO: hier checken wies weitergeht!
    def checkWinning(self, letter):
        for number in range(1,4):
            if (self.getFieldCombi((number,1))  ==  letter  and self.getFieldCombi((number,2))  ==  letter and self.getFieldCombi((number,3))  ==  letter):
                print("Game Done! " + letter + " hat Gewonnen! 1")
                self.setEnd(True)
                return
            elif (self.getFieldCombi((1,number))  ==  letter  and self.getFieldCombi((2,number))  ==  letter and self.getFieldCombi((3,number))  ==  letter) :
                print("Game Done! " + letter + " hat Gewonnen! 2")
                self.setEnd(True)
                return
            elif(self.getFieldCombi((1, 1)) == letter and self.getFieldCombi((2, 2)) == letter  and self.getFieldCombi((3, 3)) == letter ) :
                print("Game Done! " + letter + " hat Gewonnen! 3")
                self.setEnd(True)
                return
            elif (self.getFieldCombi((1, 3)) == letter and self.getFieldCombi((2, 2)) == letter  and self.getFieldCombi((3, 1)) == letter ):
                print("Game Done! " + letter +" hat Gewonnen! 4")
                self.setEnd(True)
                return
            elif (getterSetter.isSpielfeldFull()):
                self.setEnd(True)
                print("Es gibt keinen Gewinner!")
                self.wipeSpielfeld()
                return
            else:
                return

    #Still buggy have to be fixed sometime
    # def playAgain(self):
    #     if (bool(input("Nochmal Spielen? \n"))):
    #         self.setEnd(False)
    #         self.withBot()
    #         tickTackToe.main()

    def wipeSpielfeld(self):
        for a in range(0, 3):
            for b in range(0, 3):
                tickTackToe.modifySpielFeld(a, b , None)

    def printSpielfeld(self):
        for reihe in getterSetter.getSpielfeld():
            print(reihe)


    def getField(self, hoch, breit):
        return getterSetter.getSpielfeld()[hoch][breit]

    def getFieldCombi(self, combi):
        a = combi[0]-1
        b = combi[1]-1
        return getterSetter.getSpielfeld()[a][b]

    def withBot(self):
        try:
            x = str(input("\nMit o. Ohne Bot?!\n")).lower()
            if x == "ja" or x == "mit":
                print("Es wird nun mit dem Bot gespielt! \n")
                self.setBot(True)
            elif x == "nein" or x == "ohne":
                print("Es wird nun ohne den Bot gespielt! \n")
                self.setBot(False)
            else:
                print("Bitte gib Ja oder Nein ein!")
                self.withBot()
        except Exception as exception:
            if (getterSetter.isDebug()):
                print(exception)
            print("Bitte gib nur ja / mit oder nein / ohne ein!")
            self.withBot()

    def getFieldSlotByValues(self, value):
        if value < 4:
            number_a = 0
            number_b = value-1
        elif value < 7:
                number_a = 1
                number_b = value - 4
        else:
            number_a = 2
            number_b = value - 7
        return (number_a, number_b)




