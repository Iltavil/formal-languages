

from os import truncate


class FAreader:
    states = []
    alphabet = []
    transitions = []
    finalStates = []
    initial = ""
    inputFileFA = ""

    def __init__(self,FaFIleString):
        self.inputFileFA = FaFIleString
        self.readFile()

    def addToArray(self, mode, line):
        if mode == "-STATES":
            for state in line.split(','):
                self.states.append(state)
        elif mode == "-INITIAL":
            self.initial = line
        elif mode == "-ALPHABET":
            for letter in line.split(','):
                self.alphabet.append(letter)
        elif mode == "-FINAL":
            for state in line.split(','):
                self.finalStates.append(state)
        elif mode == "-TRANSITIONS":
            elements = line.split('~')
            transitionAlphabet = []
            for letter in elements[1]:
                transitionAlphabet.append(letter)
            self.transitions.append((elements[0],transitionAlphabet.copy(),elements[2]))
        else:
            print("there is a problem with mode: " + mode + " and line: " + line)

    def printMenu(self):
        print("1: all states")
        print("2: initial state")
        print("3: alphabet")
        print("4: all transitions")
        print("5: final states")

    def menu(self):
        while(True):
            self.printMenu()
            command = input(">")
            if command == "exit" or command == "quit":
                return
            elif command == "1":
                print(self.states)
            elif command == "2":
                print(self.initial)
            elif command == "3":
                print(self.alphabet)
            elif command == "4":
                print(self.transitions)
            elif command == "5":
                print(self.finalStates)

    

    def __check(self,state,currentLetter,givenSequence):
        
        if currentLetter not in self.alphabet:
            return False
            #when there is nothing left
        returnValue = False
        for transaction in self.transitions:
            if state == transaction[0] and currentLetter in transaction[1]:
                if not givenSequence:
                    if state in self.finalStates:
                        return True
                    return False
                returnValue = returnValue or self.__check(transaction[2],givenSequence[0],givenSequence[1:])
        return returnValue

        
        

    def checkWrapper(self,sequence):
        return self.__check(self.initial,sequence[0],sequence[1:])
        
    def readFile(self):
        with open(self.inputFileFA) as fileHandler:
            mode = ""
            lines = fileHandler.readlines()
            for line in lines:
                line = line.strip()
                if line in ["-STATES","-INITIAL","-ALPHABET","-FINAL","-TRANSITIONS"]:
                    mode = line
                else:
                    self.addToArray(mode,line)
        
        

#a = FAreader("FA.in")
#a.readFile()
#print(a.checkWrapper("ab2cd222aA"))
#n = FAreader("numberFA.in")
#n.readFile()
#print(n.checkWrapper("2"))
#a.menu()
