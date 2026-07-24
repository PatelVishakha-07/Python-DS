class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SimpleQueue:
    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self,val):
        new_node = Node(val)

        if not self.rear and not self.front:
            self.rear = new_node
            self.front = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.rear and not self.front:
            print("Queue Underflow")
            return
        print("Removed element is", self.front.val)
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
    
    def display(self):
        if not self.rear and not self.front:
            print("Queue Underflow")
            return
        
        temp = self.front
        while temp:
            print(temp.val, end=" ")
            temp = temp.next


q = SimpleQueue()

while True:
    ch = int(input("""\n0. Exit
1. Enqueue
2. Dequeue
3. Display
Enter your choice: """))
    
    if ch==0:
        break
    elif ch==1:
        val = int(input("enter element: "))
        q.enqueue(val)

    elif ch==2:
        q.dequeue()
    elif ch==3:
        q.display()
    else:
        print("Invalid Choice...")