from copy import deepcopy

from Grammar import Grammar


class Parser:
    def __init__(self) -> None:
        self.grammar = Grammar()
        #[[[],[]],[[]]]
        self.allSets = []
        #[[],[],[]]
        self.forCheckingAllSets = []
    
    #[["S'",["~","S"]],[...]]
    #["~","S"].index("~")
    
    def closureRecursive(self,elementArray,returnedSet):

        pointIndex = elementArray.index("~")
        nonterminal = elementArray[pointIndex+1]
        currentSet = []

        elementsAdded = False
        #goes through all the productions of the nonterminal and adds them after putting ~ first
        for each in self.grammar.productions[nonterminal]:
            eachCopy = each.copy()
            eachCopy.insert(0,"~")
            addedElement = [nonterminal,eachCopy]
            #since we know we added ~ as the first element we know we have to check the second element if it is a nonterminal
            if eachCopy[1] in self.grammar.nonterminals:
                currentSet.append(eachCopy)
            #we we check to make sure the element is not already in the new set
            if addedElement not in returnedSet:
                elementsAdded = True
                returnedSet.append(addedElement)
            
        #we continue to add elements to the newSet
        if elementsAdded:
            for eachElement in currentSet:
                self.closureRecursive(eachElement,returnedSet)


    def checkNewSet(self,newSet):
        newElement = False
        for each in newSet:
            if each and each not in self.forCheckingAllSets:
                newElement = True
                break
        if newElement:
            self.allSets.append(newSet)
            self.forCheckingAllSets += newSet

    #param
    #set - -array of individualSets, of form ["S'",["~","S"]]
    #it does not return anything, it tries to create a new set
    def closure(self, set):
        newSet = []
        #create the new set
        for individualSet in set:
            #we get the parts of each individual set
            individualSetElement = individualSet[0]
            individualSetArray = individualSet[1]
            pointIndex = individualSetArray.index("~")

            #case where ~ is the last element, we add the individualSet to the new set we are creating and stop
            newSet.append(individualSet)
            if pointIndex + 1 != len(individualSetArray):
                if individualSetArray[pointIndex+1] in self.grammar.nonterminals:
                    self.closureRecursive(individualSetArray,newSet)
        
        #check if the new set has new elements
        self.checkNewSet(newSet)
    
                


    #params: 
    #set -array of individualSets, of form ["S'",["~","S"]]
    #element - a string
    #it should call closure(set*), where set* is the array of individualSets that had ~ before element and now have it after element 
    def goto(self,set,element):
        allCLosureArray = []
        #we get each pair element-production
        for individualSet in set:
            individualSetElement = individualSet[0]
            individualSetArray = individualSet[1]
            #get the position of the ~ (element we use as .)
            pointIndex = individualSetArray.index("~")
            if pointIndex +1 <len(individualSetArray) and individualSetArray[pointIndex+1] == element:
                #make a copy of the production and swap the element with the point
                closureArray = deepcopy(individualSetArray)
                closureArray[pointIndex], closureArray[pointIndex+1] = closureArray[pointIndex+1], closureArray[pointIndex]
                allCLosureArray.append([individualSetElement,closureArray])
        #print(allCLosureArray)
        self.closure(allCLosureArray)
        


    def CanonicalCollection(self):
        self.closure([[self.grammar.startingSymbol+"`",["~",self.grammar.startingSymbol]]])
        i = 0
        while i < len(self.allSets):
            for term in self.grammar.nonterminals:
                self.goto(self.allSets[i],term)
            for term in self.grammar.terminals:
                self.goto(self.allSets[i],term)
            i +=1
        #work with ~ in place of .

    def prettyPrintSets(self):
        i = 0
        for set in self.allSets:
            print("set" + str(i) + ": " +str(set))
            i+=1

#print(["~","S"].index("~"))
a = Parser()
a.grammar.readFile("test.txt")
a.CanonicalCollection()
a.prettyPrintSets()
#a.closure([["A",["~","A"]]])
#print(a.allSets)
#a.goto([["S",["~","S"]],["A",["C","~","A"]],["A",["C","~","S"]]],"S")

