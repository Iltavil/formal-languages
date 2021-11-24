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
        for each in self.grammar.productions[nonterminal]:
            eachCopy = each.copy()
            addedElement = [nonterminal,eachCopy.insert(0,"~")]
            if eachCopy[1] in self.grammar.nonterminals:
                currentSet.push(eachCopy)
            if addedElement not in returnedSet:
                elementsAdded = True
                returnedSet.push(addedElement)
            
        if elementsAdded:
            for eachElement in currentSet:
                self.closureRecursive(eachElement,returnedSet)
            
    
    def closure(self,set):
        #["S'",["~","S"]]
        newSet = []
        elementArray = set[1]
        pointIndex = elementArray.index("~")
        
        if pointIndex + 1 == len(elementArray):
            newSet.push(set)
        else:
            newSet.push(set)
            if elementArray[pointIndex+1] in self.grammar.nonterminals:
                self.closureRecursive(elementArray,newSet)
        
        newElement = False
        for each in newSet:
            if each not in self.forCheckingAllSets:
                newElement = True
                break
        if newElement:
            self.allSets.push(newSet)
            self.forCheckingAllSets += newSet
                
        #if newSet has any new elements


    def goto(self,set,element):
        for individualSet in set:
            individualSetArray = individualSet[1]
            pointIndex = individualSetArray.index("~")
            if pointIndex<len(individualSetArray) and individualSetArray[pointIndex+1] == element:
                closureArray = deepcopy(individualSetArray)
                closureArray[pointIndex], closureArray[pointIndex+1] = closureArray[pointIndex+1], closureArray[pointIndex]
                self.closure(closureArray)
                return
    def CanonicalCollection(self):
        pass
        #work with ~ in place of .
#print(["~","S"].index("~"))

