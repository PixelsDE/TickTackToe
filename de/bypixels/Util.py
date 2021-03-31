from de.bypixels.TickTackToe import *

class testTwo():
    end = False

    def fillSpielfeld(self):
        x = subFile.getSpielfeld()
        # [ [], [] , [] ]
        for item in x:
            # die einzelnen reihen
            for slot in range(3):
                # slots 0, 1, 2
                item.append(None)

    def getEnd(self):
        return self.end

    def setEnd(self, end):
        self.end = end

    def checkWinning(self, letter):
        for number in range(1,4):
            if (self.getFieldCombi((number,1))  ==  letter  and self.getFieldCombi((number,2))  ==  letter and self.getFieldCombi((number,3))  ==  letter) \
                    or (self.getFieldCombi((1,number))  ==  letter  and self.getFieldCombi((2,number))  ==  letter and self.getFieldCombi((3,number))  ==  letter) \
                    or(self.getFieldCombi((1, 1)) == letter and self.getFieldCombi((2, 2)) == letter  and self.getFieldCombi((3, 3)) == letter ) \
                    or (self.getFieldCombi((1, 3)) == letter and self.getFieldCombi((2, 2)) == letter  and self.getFieldCombi((3, 1)) == letter ):
                self.setEnd(True)

        print("Game Done")

    def printSpielfeld(self):
        for reihe in subFile.getSpielfeld():
            print(reihe)


    def getField(self, hoch, breit):
        return subFile.getSpielfeld()[hoch][breit]
    def getFieldCombi(self, combi):
        a = combi[0]-1
        b = combi[1]-1
        return subFile.getSpielfeld()[a][b]




