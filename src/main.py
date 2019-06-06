# Python 2.7

import sys

def cleanUpNumber(numberStr):
    return numberStr.replace(".", "").replace(",", "")

def dealWithCents(value):
    if len(value) < 3:
        return

    centsValue = value[-2:]
    unitValue = centsValue[1]
    decimalValue = centsValue[0]
    print "Centavos:", str(centsValue)
    print "Unidade:", str(unitValue)
    print "Decimal:", str(decimalValue)
    print "-------------------------------------"

    unitWord = ""
    if unitValue != "0":
        switcher = {
            1: "um",
            2: "dois", 
            3: "tres",
            4: "quatro",
            5: "cinco",
            6: "seis",
            7: "sete",
            8: "oito",
            9: "nove"
            }
        unitWord = switcher.get(int(unitValue), "") 

    unitWord = unitWord + " centavos!"
    word = ""
    if decimalValue == "1":
        switcher = {
            0: "Dez", 
            1: "Onze",
            2: "Doze",
            3: "Treze",
            4: "Quatorze",
            5: "Quinze",
            6: "Dezesseis",
            7: "Dezessete",
            8: "Dezoito",
            9: "Dezenove"
            }
        word = switcher.get(int(unitValue), "Invalid unitValue")
        print word + " centavos!"
    else:
        if decimalValue != "0":
            switcher = {
                2: "Vinte",
                3: "Trinta",
                4: "Quarenta",
                5: "Cinquenta",
                6: "Sessenta",
                7: "Setenta",
                8: "Oitenta",
                9: "Noventa"
                }
            word = switcher.get(int(decimalValue), "Invalid decimalValue")
        print word + " e " + unitWord

    print "-------------------------------------"

def main():
    print "Script name:", sys.argv[0]
    print "Arg count:", len(sys.argv)
    print "-------------------------------------"

    for arg in sys.argv:
        print str(arg)

    number = str(sys.argv[1])
    invertedNumber = number[::-1]
    clenedString = cleanUpNumber(invertedNumber)
    dealWithCents(cleanUpNumber(number))
    for chat in clenedString:
        print(str(chat))

main()
