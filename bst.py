class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def insert(self, root, val):
        if not root:
            root = Node(val)
            return root

        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.val, end=" ")
            self.preorder(root.left)            
            self.preorder(root.right)

    def postorder(self, root):
        if root:            
            self.postorder(root.left)            
            self.postorder(root.right)
            print(root.val, end=" ")

b = BST()
root = None
while True:
    ch = int(input("""\n0. Exit
1. Insert
2. InOrder
3. PreOrder
4. PostOrder
Enter your choice: """))
    
    if ch == 0:
        break
    elif ch == 1:
        val = int(input("enter value: "))
        root = b.insert(root,val)

    elif ch == 2:
        b.inorder(root)
    
    elif ch == 3:
        b.preorder(root)

    elif ch == 4:
        b.postorder(root)

    else:
        print("Invalid Choice...")