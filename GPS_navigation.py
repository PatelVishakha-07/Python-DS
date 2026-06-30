""" H3) The GPS Navigation System (Backtracking)
You're building a GPS app like Google Maps for a hiking trail. The hiker moves through checkpoints. If they take a wrong tum, they hit "Go Back" to return to the previous checkpoint. But once they go back, they can also "Go Forward" if they change their mind again just like a browser's back/forward buttons
Operations:
visit(place)-move to a new place
back()- go to previous place
forward-go forward if available   """

class GPSNavigation:

    def __init__(self):
        self.checkpoints = []
        self.previous = []

    def visit(self, place):
        self.checkpoints.append(place)

    def back(self):
        if self.checkpoints:
            self.previous.append(self.checkpoints.pop()) 
        else:
            print("No place visited")   

    def forward(self):
        if self.previous:
            self.checkpoints.append(self.previous.pop())
        else:
            print("No place visited")   

    def currentPlace(self):
        if self.checkpoints:
            print(f"Current place: {self.checkpoints[len(self.checkpoints)-1]}")
        else:
            print("No place visited")   

gps = GPSNavigation()
gps.visit("Amalsad")
gps.visit("Bilimora")
gps.visit("Navsari")
gps.back()

gps.currentPlace()
gps.forward()
gps.currentPlace()

    