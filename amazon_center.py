""" H1) An Amazon fulfilment centre has a conveyor belt with exactly 8 slots numbered 0-7. Each slot holds one product. The warehouse manager needs to: check what's at a slot, find a product, update a slot, and check if the belt is full. The conveyor belt - fixed 8 slots
"""

class AmazonCenter:
    
    def __init__(self):
        self.belt = ["Laptop", "Mobile", "Bag", "SmartWatch", "Headphone", "Charger", "Googles"]

    def checkSlot(self):
        slot_no = int(input("enter slot no[0/7]: "))
        print(f"Product name at slot {slot_no} is {self.belt[slot_no-1]}")

    def findProduct(self):
        prd_name = input("enter product name to search: ") 
        if prd_name in self.belt:
            print(f"Product {prd_name} found")
        else:
            print(f"Product {prd_name} not found")
    
    def updateSlot(self):
        slot_no = int(input("enter slot no[0/7] to update: "))
        prd_name = input("enter new product name: ") 
        self.belt[slot_no-1] = prd_name

    def isBeltFull(self):
        return len(self.belt) == 8
    

centre = AmazonCenter()
centre.checkSlot()
centre.findProduct()
centre.updateSlot()
print("Conveyor Belt after modification:", centre.belt)
print("Is Conveyor belt full:",centre.isBeltFull())