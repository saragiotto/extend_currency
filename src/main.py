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

    append = "centavos"
    connector = ""
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
        unitWord = switcher.get(int(unitValue), "").title()

    decimalWord = ""
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
        decimalWord = switcher.get(int(unitValue), "Invalid unitValue").title()
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
            decimalWord = switcher.get(int(decimalValue), "Invalid decimalValue")

    if decimalValue == "0":
        if unitValue == "1":
            append = "centavo"
        if unitValue == "0":
            append = ""
    else:
        if decimalValue != "1" and unitValue != "0":
            connector = "e"
        else: 
            unitWord = ""

    result = [decimalWord, connector, unitWord, append]
    finalList = list(filter(lambda x: len(x) > 0, result))

    print " ".join(finalList)

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
