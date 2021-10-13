from Node import SymbolTable

st = SymbolTable()
print(st.insert(5))
print(st.insert(55))
print(st.insert(3))
print(st.insert(4))
print(st.insert(20))

st.printInOrderWrapper()
print(st.get(3))
