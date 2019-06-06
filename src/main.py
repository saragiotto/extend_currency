# Python 2.7

import sys

def cleanUpNumber(numberStr):
    return numberStr.replace(".", "").replace(",", "")

print "Script name: ", sys.argv[0]
print "Arg count: ", len(sys.argv)

for arg in sys.argv:
    print str(arg)

number = str(sys.argv[1])
invertedNumber = number[::-1]
clenedString = cleanUpNumber(invertedNumber)
for chat in clenedString:
    print(str(chat))


