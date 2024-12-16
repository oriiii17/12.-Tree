def height(node):
    if node.isExternal():
        return 0
    else:
        h = 0
        for i in node.children():
            h = max(h, height(i))
        return 1+h

print(height(root))
print(height(a))
print(height(e))