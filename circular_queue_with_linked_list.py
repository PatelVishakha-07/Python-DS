class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class CircularQueue:
    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, val):
        new_node = Node(val)
        if not self.rear and not self.front:
            self.front = new_node
            new_node.next = self.front
            self.rear = new_node            
        else:
            new_node.next = self.front
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.rear and not self.front:
            print("Queue underflow")
            return
        print("Removed element is", self.front.val)

        if self.rear == self.front:
            self.rear = None
            self.front = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

    def display(self):
        if not self.rear and not self.front:
            print("Queue underflow")
            return
        temp = self.front
        while temp != self.rear:
            print(temp.val, end=" ")
            temp = temp.next
        print(self.rear.val)

cq = CircularQueue()
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
        cq.enqueue(val)
    elif ch==2:
        cq.dequeue()
    elif ch==3:
        cq.display()
    else:
        print("Invalid Choice...")