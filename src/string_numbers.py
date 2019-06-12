class StringNumbers():
    @staticmethod
    def unitString(number):
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

