# Python 2.7

import sys

print "Script name: ", sys.argv[0]
print "Arg count: ", len(sys.argv)

for arg in sys.argv:
    print str(arg)

number = str(sys.argv[1])
for chat in number:
    print(str(chat))
