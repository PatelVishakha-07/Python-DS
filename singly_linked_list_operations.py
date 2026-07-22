class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def createLL(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def insertFirst(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertPosition(self, val, pos):
        if not self.head:
            self.insertFirst(val)
        else:
            c=1
            temp = self.head
            while c < pos-1:
                temp = temp.next
                c += 1
            new_node = Node(val)
            new_node.next = temp.next
            temp.next = new_node

    def delFirst(self):
        if not self.head:
            print("List is Empty")
        else:
            print("Removed element is", self.head.val)
            self.head = self.head.next

    def delLast(self):
        if not self.head:
            print("List is Empty")
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            print("Removed element is", temp.next.val)
            self.tail = temp
            self.tail.next = None

    def delPosition(self, pos):
        if not self.head:
            print("List is Empty")
        elif pos==1:
            self.delFirst()
        else:
            c=1
            temp = self.head
            while c<pos-1:
                temp = temp.next
                c += 1
            print("Removed element is", temp.next.val)
            temp.next = temp.next.next

    def traverse(self):
        if not self.head:
            print("List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.val, end = " ")
                temp = temp.next

    def reverseList(self):
        if not self.head:
            print("List is Empty")
        else:
            prev = None
            temp = self.head
            cur = self.head

            while temp:
                temp = temp.next
                cur.next = prev
                prev = cur
                cur = temp       
            self.head = prev

    def sortList(self):
        if not self.head:
            print("List is Empty")
        else:
            t1 = self.head            

            while t1:
                f = 1
                t2 = t1
                while t2:
                    if t1.val > t2.val:
                        t1.val, t2.val = t2.val, t1.val
                        f=0
                    t2 = t2.next
                if f==1:
                    break
                t1 = t1.next


sll = SinglyLinkedList()
while True:
    ch = int(input("""\n0. Exit
1. Create LL
2. Insert First
3. Insert Position
4. Delete First
5. Delete Last
6. Delete Position
7. Traverse
8. Reverse LL
9. Sort List
Enter your choice: """))
    
    if ch==0:
        print("Thank You!!!")
        break

    elif ch==1:
        val = int(input("enter element: "))
        sll.createLL(val)

    elif ch==2:
        val = int(input("enter element: "))
        sll.insertFirst(val)

    elif ch==3:
        val = int(input("enter element: "))
        pos = int(input("enter positon: "))
        sll.insertPosition(val, pos)

    elif ch==4:
        sll.delFirst()

    elif ch==5:
        sll.delLast()

    elif ch==6:
        pos = int(input("enter position: "))
        sll.delPosition(pos)

    elif ch==7:
        sll.traverse()

    elif ch==8:
        sll.reverseList()
    
    elif ch==9:
        sll.sortList()

    else:
        print("Invalid Choice....")