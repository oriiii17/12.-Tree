class Node:
    def __init__(self, data, parent):
        self._data = data
        self._children = []
        self._parent = parent

    #menambahkan child
    def addChild(self, data):
        self._children.append(data)

    #mendapatkan isi elemen
    def operator(self):
        return self._data
    
    #mendapatkan node parent
    def parent(self):
        return self._parent
    
    #mendapatkan node children
    def children(self):
        return self._children
    
    #mengecek apakah node merupakan root
    def isRoot(self):
        return self._parent is None
    
    #mengecek apakah node merupakan external/leaf
    def isExternal(self):
        return len(self._children) == 0
    

root = Node(10, None)
a = Node(12, root)
b = Node(20, root)
c = Node(50, a)
d = Node(3, a)
e = Node(30, a)
f = Node(8, b)
a.addChild(c)
a.addChild(d)
a.addChild(e)
b.addChild(f)
root.addChild(a)
root.addChild(b)

#cetak data pada node d
print(d.operator())
#cetak data dari parent node e
print(e.parent().operator())
#cetak data children dari node a
for i in a.children():
    print(i.operator(), end = ' ')