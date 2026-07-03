class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None
        self.temp = None

    def createLL(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            self.temp = new_node
        else:
            self.temp.next = new_node
            self.temp = new_node

    def insertFirst(self, val):
        if self.head == None:
            self.createLL(val)
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node

    def insertPosition(self, val, pos):
        if not self.head:
            self.createLL(val)
        else:
            c = 1
            t = self.head

            while c < pos-1:
                c += 1
                t = t.next

            new_node = Node(val)
            new_node.next = t.next

            t.next = new_node

    def delFirst(self):
        if not self.head:
            print("Linked List is empty")
            return
        
        print("Removed element is", self.head.data)
        self.head = self.head.next

    def delLast(self):
        if not self.head:
            print("Linked List is empty")
            return
        
        t = self.head
        while t.next.next != None:
            t = t.next
        print("Removed element is", t.next.data)
        t.next = None
        self.temp = t

    def delPosition(self, pos):
        if not self.head:
            print("Linked List is empty")
            return
        
        c=1
        t = self.head

        while c < pos-1:
            c += 1
            t = t.next
        print("Removed element is", t.next.data)

        t.next = t.next.next
        
    def traverse(self):
        if not self.head:
            print("Linked List is empty")
            return
        
        t = self.head
        while t:
            print(t.data, end=" ")
            t = t.next


def menu():
    return int(input("""
                     0. Exit
                     1. Create LL
                     2. Insert first
                     3. Insert Position
                     4. Delete First
                     5. Delete Last
                     6 Delete Position
                     7. Traverse
                     Enter your choice: """))

ll = LinkedList()

while True:
    ch = menu()

    if ch == 0:
        print("Thank You")
        break

    elif ch==1:
        val = int(input("enter value: "))
        ll.createLL(val)

    elif ch==2:
        val = int(input("enter value: "))
        ll.insertFirst(val)

    elif ch==3:
        val = int(input("enter value: "))
        pos = int(input("enter position to insert: "))
        ll.insertPosition(val, pos)

    elif ch==4:
        ll.delFirst()

    elif ch==5:
        ll.delLast()

    elif ch==6:
        pos = int(input("enter position to delete: "))
        ll.delPosition(pos)

    elif ch==7:
        ll.traverse()

    else:
        print("Invalid Choice...")
