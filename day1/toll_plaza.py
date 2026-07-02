""" h2) Toll Plaza Simulation (Circular Queue)
A toll plaza has a fixed capacity of 5 vehicles. If full, new vehicles must wait Implement a Circular Queue to simulate this, since it reuses empty slots without wasting memory.
"""

from collections import deque

class TollPlaza:

    def __init__(self, maxsize):
        self.capacity = deque(maxlen=maxsize)
        self.wait = deque()
        self.maxsize = maxsize

    def addVehicles(self, vno):
        if len(self.capacity) == self.maxsize:
            self.wait.append(vno)
            return
        self.capacity.append(vno)

    def removeVehicle(self):
        if self.capacity:
            print(f"Removed vehicle: {self.capacity.popleft()}")
            if self.wait:
                self.capacity.append(self.wait.popleft())

    def viewVehicles(self):
        if self.capacity:
            for v in self.capacity:
                print(v)

maxsize = 5
tp = TollPlaza(maxsize)
tp.addVehicles(5678)
tp.addVehicles(1234)
tp.addVehicles(2345)
tp.addVehicles(3478)
tp.addVehicles(9077)
tp.addVehicles(1093)
tp.addVehicles(3029)

tp.viewVehicles()

tp.removeVehicle()
tp.viewVehicles()