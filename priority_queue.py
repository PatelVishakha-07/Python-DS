class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, val):
        new_node = Node(val)
        if not self.front and not self.rear:
            self.rear = new_node
            self.front = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            print("Queue Underflow")
            return
        temp = self.front
        t = self.front
        prev = None
        highest_prev = None

        while temp:
            if t.val < temp.val:    
                highest_prev = prev          
                t = temp  

            prev = temp                          
            temp = temp.next
            

        if not highest_prev:
            print("Removed element is", self.front.val)
            self.front = self.front.next

            if not self.front:
                self.rear = None
            return

        print("Removed element is", t.val)
        if t == self.rear:
            self.rear = highest_prev
            self.rear.next = None

        highest_prev.next = t.next

    def display(self):
        if not self.front:
            print("Queue Underflow")
            return
        temp = self.front
        while temp:
            print(temp.val, end=" ")
            temp = temp.next

pq = PriorityQueue()
while True:
    ch = int(input("""\n0. Exit
1. Enqueue
2. Dequeue
3. Display
4. Enter your choice: """))

    if ch==0:
        break
    elif ch==1:
        val = int(input("enter element: "))
        pq.enqueue(val)
    elif ch==2:
        pq.dequeue()
    elif ch==3:
        pq.display()
    else:
        print("Invalid choice...")