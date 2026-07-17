class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def createLL(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insertFirst(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertPosition(self, val, pos):
        if pos == 1:
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
        print("Removed element is:", self.head.val)

        self.head = self.head.next
        self.head.prev = None

    def delPosition(self, pos):
        if pos == 1:
            self.delFirst()
        else:
            c = 1
            temp = self.head
            while c < pos-1:
                temp = temp.next

            print("Removed elemnt is:", temp.next.val)
            temp.next = temp.next.next
            temp.next.prev = temp

    def delLast(self):
        print("Removed element is:", self.tail.val)

        self.tail = self.tail.prev
        self.tail.next = None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next

dll = DoublyLinkedList()

while True:
    ch = int(input("""\n0. Exit
1. Create DLL
2. Insert first
3. Insert Position
4. Delete First
5. Delete Position                    
6. Delete Last
7. Traverse                                                                                           
Enter your choice: """))
    
    if ch == 0:
        break
    
    elif ch == 1:
        val = int(input("enter element to insert: "))
        dll.createLL(val)
    
    elif ch == 2:
        val = int(input("enter element to insert: "))
        dll.insertFirst(val)
    
    elif ch == 3:
        val = int(input("enter element to insert: "))
        pos = int(input("enter position to insert: "))
        dll.insertPosition(val, pos)

    elif ch == 4:
        dll.delFirst()

    elif ch == 5:
        pos = int(input("enter posiiton to delete: "))
        dll.delPosition(pos)

    elif ch == 6:
        dll.delLast()

    elif ch == 7:
        dll.traverse()

    else:
        print("Invalid Choice...")
