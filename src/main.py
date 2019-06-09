# Python 2.7

import sys
import fileinput

def cleanUpNumber(numberStr):
    return numberStr.replace(".", "").replace(",", "")

def dealWithDecimals(value, singleName, pluralName):
    number = str(value)
    if len(number) < 2:
        number = "0" + number

    centsValue = number[-2:]
    unitValue = centsValue[1]
    decimalValue = centsValue[0]
    # print "Decimal:", str(decimalValue)
    # print "Unidade:", str(unitValue)
    # print "-------------------------------------"

    append = pluralName 
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
            append = singleName
        if unitValue == "0":
            append = ""
    else:
        if decimalValue != "1" and unitValue != "0":
            connector = "e"
        else: 
            unitWord = ""

    result = [decimalWord, connector, unitWord, append]
    return list(filter(lambda x: len(x) > 0, result))

def glueDecimalAndCents(decimals, cents):
    if len(decimals) == 0:
        decimals = ["Zero reais"]

    result = list(decimals)
    if len(cents) > 0:
        centList = list(cents)
        result.append("e")
        result.extend(centList)
    
    return ' '.join(result)
        
def printNumberInWords(value):
    
    number = str(value)
    if len(number) < 2:
        number = "00" + number
    else:
        if len(number) < 3:
            number = "0" + number

    clenedString = cleanUpNumber(number)
    singleCents = "centavo"
    pluralCents = "centavos"
    centsResult = dealWithDecimals(clenedString, singleCents, pluralCents)

    singleCurrency = "real"
    pluralCurrency = "reais"
    integerPart = clenedString[:-2]
    integerResult = dealWithDecimals(integerPart, singleCurrency, pluralCurrency)

    # print integerResult + centsResult

    print number + "  ->  " + glueDecimalAndCents(integerResult, centsResult)

def sysoutUsage():
    print "usage: main.py [version] [help] [test] [number value]"
    print "   "
    print "   --vesion        print out the vesion of this program"
    print "   --help          Show some usefull information about this program"
    print "   --test          Execute some unit tests"
    print "   --file          Process a input file"
    print "   numberVlaue   Should be positive number, with two decimals, separeted by comma or period."

def sysoutHelp():
    print " Esse programa expressa numeros monetarios por extenso."

    print " Por exemplo: "
    print " $ python main.py 1,23"
    print " $ 1,23  ->  Um real e Vinte e Tres centavos"

def sysoutVersion():
    print "0.1.0" 

def processFile(fileName):
    for line in fileinput.input(fileName):
        cleanLine = line.rstrip()
        evalLine = cleanUpNumber(cleanLine)
        if evalLine.isdigit():
            printNumberInWords(cleanLine)


def main():

    if len(sys.argv) > 1:
        if str(sys.argv[1]) == "--test":
            for n in range(0, 9999):
                printNumberInWords(int(n))

            return

        if str(sys.argv[1]) == "--help":
            sysoutHelp()
            return

        if str(sys.argv[1]) == "--version":
            sysoutVersion()
            return

        if str(sys.argv[1]) == "--file":
            processFile(sys.argv[2])
            return

        evalNumber = cleanUpNumber(sys.argv[1])
        if not evalNumber.isdigit():
            print "Invalid number provided " + evalNumber
            return

    else: 
        sysoutUsage()
        return

    printNumberInWords(sys.argv[1])

main()
