import traceback

#raise Exception('This is error message')

"""
*****************
*               *
*               *
*               *
*****************

"""

def printBox(symbol,width,height):
    if len(symbol) != 1:
        try:
            raise Exception('Symbols needs to be a string of length 1')
        except:
            errorFile = open('ErrorLog.txt','w')
            errorFile.write(traceback.format_exc())
            errorFile.close()

    print(symbol * width)   # Print Top
    for i in range(height - 2):  # Print Loop.
        print(symbol + (' ' *  (width-2)) + symbol)
    print(symbol * width)   # Print Bottom


printBox('**', 15, 6)
