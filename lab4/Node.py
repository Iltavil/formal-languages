class Node:
    def __init__(self, key, position = 0):
        self.position = position
        self.key = key
        self.value = 0
        self.left = None
        self.right = None

class SymbolTable:
    def __init__(self):
        self.head = None
        self.position = 0
        self.nodes = []

    def insert(self,key):
        position = self.position
        if self.head is None:
            self.head = Node(key,position)
            self.position = self.position + 1
            self.nodes.append(self.head)
        else:
            current = self.head
            while True :#middle
                if current.key == key:
                    return current.position
                #left side
                elif current.key > key:
                    if current.left is None:
                        current.left = Node(key,position)
                        self.position = self.position + 1
                        self.nodes.append(current.left)
                        break
                    else:
                        current = current.left
                else: #right side
                    if current.right is None:
                        current.right = Node(key,position)
                        self.position = self.position + 1
                        self.nodes.append(current.right)
                        break
                    else:
                        current = current.right
        return position

    def exists(self,key):
        current = self.head
        while True:
            if current.key == key:
                return True
            if current.key > key:
                if current.left is None:
                    return False
                else:
                    current = current.left
            else:
                if current.right is None:
                    return False
                else:
                    current = current.right

    def get(self,position):
        return self.nodes[position].key

    
    def printInOrderWrapper(self):
        self.__printInOrder(self.head)

    def __str__(self) -> str:
        string = ""
        for node in self.nodes:
            string += str(node.key) + " " +str(node.position) + "\n"
        return string
    
    def __printInOrder(self,root):
        if root:
            self.__printInOrder(root.left)
            print(str(root.key) + " " +str(root.position))
            self.__printInOrder(root.right)