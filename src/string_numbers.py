class StringNumbers():
    def unitString(self, number):
        switcher = {
            0: "zero",
            1: "Um",
            2: "Dois",
            3: "Tres",
            4: "Quatro",
            5: "Cinco",
            6: "Seis",
            7: "Sete",
            8: "Oito",
            9: "Nove"
        }
        return switcher.get(int(number), "Unable to parse int number" + number)

    def decimalString(self, decimals): 
        decimalDigit = int(decimals[0]) 
        unitDigit = int(decimals[1])

        if decimalDigit == 1:
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
            return switcher.get(unitDigit, "Unable to parse int number" + str(unitDigit))
        else: 
            if decimalDigit != 0:
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
                return switcher.get(decimalDigit, "Unable to part int number" + str(decimalDigit))

        return ""

