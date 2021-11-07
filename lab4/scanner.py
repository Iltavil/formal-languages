import re
import os
from Node import SymbolTable


#we try another way, by spliting the token.in in alphanumerical and non alphanumerical tokensin 2 lists, then when we find a 
# non alphanumerical character we see how many times that characters appears in the second list

#problem with negative numbers, roly solved by using emoji in place of -

def getTokens():
    alphanumericalList = []
    nonalphanumericalList = []
    with open("token.in") as inputFile:
        for line in inputFile:
            line = line.strip()
            if line.isalnum():
                alphanumericalList.append(line)
            else:
                nonalphanumericalList.append(line)
    return alphanumericalList,nonalphanumericalList

def genPIF(token,value,pifFile):
    fileHandler = open(pifFile,'a')
    fileHandler.write(token + " " + str(value) + "\n")
    fileHandler.close()

def removeFile(filename):
    try:
        os.remove(filename)
    except OSError:
        pass



def readFile(inputFileString):
    alnumTokens,nonAlnumTokens = getTokens()
    canBeNegative = False
    lineNr = 0
    symbolTable = SymbolTable()
    errorFound = False
    constantRE = "^[-+]?[1-9][0-9]*$|0"
    indentifierRE = "^[a-zA-z]\w*$"
    pifFile = "PIF.out"
    removeFile(pifFile)
    stFile = "ST.OUT"
    removeFile(stFile)
    with open(inputFileString) as inputFile:
        for line in inputFile:
            formatedLine = ""
            lineNr +=1
            #we try to separate the nonalphanumeric characters with a space so they are easier to tokenize
            i = 0
            while i < len(line):
                #if the character is a symbol and it is in token.in
                if sum(s.count(line[i]) for s in nonAlnumTokens):

                    #checks for - in negative numbers
                    if line[i] == "-" and line[i+1].isnumeric() and canBeNegative:
                        formatedLine = formatedLine +line[i]
                        i+=1
                        continue
                    
                    formatedLine = formatedLine + " " + line[i]
                    i +=1

                    #checks for a compound symbol
                    if i <  len(line) and line[i-1] + line[i] in nonAlnumTokens:
                        formatedLine += line[i]
                        i +=1
                    formatedLine += " "
                    canBeNegative = True

                #checks for other symbols
                elif line[i] not in (" ","\n","'") and not line[i].isalnum():
                    formatedLine = formatedLine + " " + line[i] + " "
                    i +=1
                    canBeNegative = False

                #meant for numbers and characters
                else:
                    formatedLine += line[i]
                    if line[i] != " ":
                        canBeNegative = False
                    i +=1
                    
            tokens = formatedLine.split()


            #we start adding the tokens to pif and check if they are lexically ok
            for eachToken in tokens:
                if eachToken in alnumTokens or eachToken in nonAlnumTokens:
                    genPIF(eachToken,-1,pifFile)
                elif re.match(constantRE,eachToken):
                    index = symbolTable.insert(eachToken)
                    genPIF("const",index,pifFile)
                elif re.match(indentifierRE,eachToken):
                    index = symbolTable.insert(eachToken)
                    genPIF("identifier",index,pifFile)
                else:
                    errorFound = True
                    print("Lexical error on line " + str(lineNr) +", problem with token " + eachToken)
        
    if not errorFound:
        fileHandler = open(stFile,'a')
        fileHandler.write(str(symbolTable))
        print("lexically correct")
        




#readFile("p1mini.txt")
#readFile("p2mini.txt")
readFile("p3mini.txt")
#readFile("p1errMini.txt")