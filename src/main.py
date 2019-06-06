# Python 2.7

import sys

def cleanUpNumber(numberStr):
    return numberStr.replace(".", "").replace(",", "")

def dealWithDecimals(value, singleName, pluralName):
    number = str(value)
    if len(number) < 2:
        number = "0" + number

    centsValue = number[-2:]
    unitValue = centsValue[1]
    decimalValue = centsValue[0]
    print "Decimal:", str(decimalValue)
    print "Unidade:", str(unitValue)
    print "-------------------------------------"

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
    result = list(decimals)
    if len(cents) > 0:
        centList = list(cents)
        result.append("e")
        result.extend(centList)
    
    return ' '.join(result)
        

def main():
    print "Script name:", sys.argv[0]
    print "Arg count:", len(sys.argv)
    print "-------------------------------------"

    for arg in sys.argv:
        print str(arg)

    number = str(sys.argv[1])
    clenedString = cleanUpNumber(number)
    singleCents = "centavo"
    pluralCents = "centavos"
    centsResult = dealWithDecimals(clenedString, singleCents, pluralCents)

    singleCurrency = "real"
    pluralCurrency = "reais"
    integerPart = clenedString[:-2]
    integerResult = dealWithDecimals(integerPart, singleCurrency, pluralCurrency)

    print integerResult + centsResult

    print "-------------------------------------"
    print glueDecimalAndCents(integerResult, centsResult)
    print "-------------------------------------"

main()
