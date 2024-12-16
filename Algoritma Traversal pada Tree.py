def preorder(node):
    print(node.operator(), end = ' ')
    for i in node.children():
        preorder(i)
 
def postorder(node):
    for i in node.children():
        postorder(i)
    print(node.operator(), end = ' ')

preorder(root)
postorder(root)