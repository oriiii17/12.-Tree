def depth(node):
    if node.isRoot():
        return 0;
    else:
        return 1+depth(node.parent())
    
print(depth(root))
print(depth(a))
print(depth(e))