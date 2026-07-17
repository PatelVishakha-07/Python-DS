class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class CircularlinkedList:

    def __init__(self):
        self.head = None    
        self.tail = None    

    def enqueue(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = self.head            
        
        else:  
            new_node.next = self.head
            self.tail.next = new_node    
            self.tail = new_node        
        
    def insertFirst(self, val):
        if not self.head:
            self.enqueue(val)

        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head

    def insertPosition(self, val, pos):
        if not self.head:
            self.enqueue(val)
        elif pos == 1:
            self.insertFirst(val)
        else:
            c = 1
            temp = self.head
            while c < pos-1:
                temp = temp.next
                c += 1

            new_node = Node(val)
            new_node.next = temp.next
            temp.next = new_node

    def dequeue(self):
        print("Reoved element is:", self.tail.val)
        temp = self.tail.next

        while temp.next != self.tail:
            temp = temp.next
        
        temp.next = self.head
        self.tail = temp

    def delFirst(self):
        print("Removed element is:", self.head.val)

        self.head = self.head.next
        self.tail.next = self.head

    def delPosition(self, pos):
        if pos == 1:
            self.delFirst()

        else:
            c = 1
            temp = self.head

            while c < pos-1:
                temp = temp.next
                c += 1

            print("Removed element is:", temp.next.val)
            temp.next = temp.next.next

    def traverse(self):
        print("Queue Elements are: ")
        temp = self.tail.next
        while temp != self.tail:
            print(temp.val, end=" ")
            temp = temp.next
        print(temp.val)
        

cq = CircularlinkedList()

while True:
    ch = int(input("""\n0. Exit
1. Enqueue
2. Dequeue
3. Traverse
4. Insert first
5. Insert Position
6. Delete First
7. Delete Position                                                                                            
Enter your choice: """))
    
    if ch == 0:
        break
    elif ch == 1:
        val = int(input("enter element to insert: "))
        cq.enqueue(val)

    elif ch == 2:
        cq.dequeue()

    elif ch == 3:
        cq.traverse()

    elif ch == 4:
        val = int(input("enter element to insert: "))
        cq.insertFirst(val)

    elif ch == 5:
        val = int(input("enter element to insert: "))
        pos = int(input("enter position to insert: "))
        cq.insertPosition(val, pos)

    elif ch == 6:
        cq.delFirst()

    elif ch == 7:
        pos = int(input("enter position to insert: "))
        cq.delPosition(pos)

    else:
        print("Invalid Choice...")
