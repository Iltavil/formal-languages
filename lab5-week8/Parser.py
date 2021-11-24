

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
    def closure(self,set):
        #["S'",["~","S"]]
        newSet = []
        elementArray = set[1]
        pointIndex = elementArray.index("~")
        if pointIndex + 1 == len(elementArray):
            newSet.push(set)
        else
        #if newSet has any new elements


    def goto(self,set,element):
        for individualSet in set:
            individualSetArray = individualSet[1]
            pointIndex = individualSetArray.index("~")
            if pointIndex<len(individualSetArray) and individualSetArray[pointIndex+1] == element:
                pass
        pass
    def CanonicalCollection(self):
        pass
        #work with ~ in place of .
#print(["~","S"].index("~"))

