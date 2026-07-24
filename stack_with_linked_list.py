class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        new_node = Node(val)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if not self.top:
            print("Stack underflow")
            return
        print("Removed element is", self.top.val)
        self.top = self.top.next

    def peek(self):
        if not self.top:
            print("Stack underflow")
            return
        print("Peeked element is", self.top.val)

    def display(self):
        if not self.top:
            print("Stack underflow")
            return
        temp = self.top
        while temp:
            print(temp.val, end=" ")
            temp = temp.next


s = Stack()

while True:
    ch = int(input("""\n0. Exit
1. Push
2. Pop
3. Peek
4. Display
Enter your choice: """))
    
    if ch==0:
        break
    elif ch==1:
        val = int(input("enter element: "))
        s.push(val)
    elif ch==2:
        s.pop()
    elif ch==3:
        s.peek()
    elif ch==4:
        s.display()
    else:
        print("Invalid Choice...")