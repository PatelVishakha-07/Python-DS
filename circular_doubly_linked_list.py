class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def createLL(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail.prev = new_node
            self.head.next = new_node
    
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.tail.next = new_node
            self.tail = new_node

    def insertFirst(self, val):
        if not self.head:
            self.createLL(val)

        else:
            new_node = Node(val)
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.head = new_node
            self.tail.next = self.head

    def insertPosition(self, val, pos):
        if not self.head:
            self.createLL(val)
        elif pos==1:
            self.insertFirst(val)
        else:
            c = 1
            temp = self.head

            while c < pos-1:
                temp = temp.next
                c += 1

            new_node = Node(val)
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node

    def delFirst(self):
        if not self.head:
            print("Linked List is empty")
            return

        print("Removed element is", self.head.val)
        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head

    def delLast(self):
        if not self.head:
            print("Linked List is empty")
            return
        print("Removed element is", self.tail.val)
        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail

    def delPosition(self, pos):
        if not self.head:
            print("Linked List is empty")
            return
        temp = self.head
        c=1
        while c < pos-1:
            temp = temp.next
            c += 1
        print("Removed element is", temp.next.val)
        temp.next.next.prev = temp
        temp.next = temp.next.next

    def traverse(self):
        if not self.head:
            print("Linked List is empty")
            return
        temp = self.head
        while True:
            print(temp.val, end=" ")
            temp = temp.next
            if temp == self.head:
                break


cdll = CircularDoublyLinkedList()
while True:
    ch = int(input("""\n0. Exit
    1. Create LL
    2. Insert First
    3. Insert Position
    4. Delete First
    5. Delete Last
    6. Delete Position
    7. Traverse
    Enter your choice: """))

    if ch == 0:
        break
    elif ch == 1:
        val = int(input("Enter element: "))
        cdll.createLL(val)
    elif ch==2:
        val = int(input("Enter element: "))
        cdll.insertFirst(val)
    elif ch == 3:
        val = int(input("Enter element: "))
        pos = int(input("Enter position: "))        
        cdll.insertPosition(val, pos)
    elif ch == 4:
        cdll.delFirst()
    elif ch == 5:
        cdll.delLast()
    elif ch == 6:
        pos = int(input("Enter position: "))
        cdll.delPosition(pos)
    elif ch == 7:
        cdll.traverse()
    else:
        print("Invalid Choice...")