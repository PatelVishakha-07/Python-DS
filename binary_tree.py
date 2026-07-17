class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:

    def create(self, val, root):
        root = Node(val)
        return root
    
    def insert(self):
        val = int(input("enter value [-1 for null]: "))
        if val == -1:
            return None
        
        root = self.create(val, None)

        print(f"enter value for {val} left: ")
        root.left = self.insert()

        print(f"enter value for {val} right: ")
        root.right = self.insert()

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

bt = BinaryTree()
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
        root = bt.insert()

    elif ch == 2:
        bt.inorder(root)
    
    elif ch == 3:
        bt.preorder(root)

    elif ch == 4:
        bt.postorder(root)

    else:
        print("Invalid Choice...")