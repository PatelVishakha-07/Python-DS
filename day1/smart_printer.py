""" c3) The Smart Printer Queue (Priority Queue)
An office printer handles jobs in order, BUT jobs marked URGENT must be printed before normal jobs Design a system using two queues one for urgent, one for normal-and always drain urgent first   """

from collections import deque
class PrinterQueue:

    def __init__(self, max_size):
        self.urgent = deque(maxlen=max_size)
        self.normal = deque(maxlen=max_size)

    def schedulePrint(self, job_name, priority="Normal"):
        if priority.lower() == "urgent":
            self.urgent.append(job_name)
        else:
            self.normal.append(job_name)

    def printJob(self):
        if self.urgent:
            while self.urgent:
                print(self.urgent.popleft())
        
        while self.normal:
            print(self.normal.popleft())

n = int(input("enter size of queue: "))
pq = PrinterQueue(n)

pq.schedulePrint("DS.docx")
pq.schedulePrint("Python.pdf")
pq.schedulePrint("Java.docx","Urgent")
pq.schedulePrint("Dbms.pdf","Urgent")
pq.schedulePrint("OOPS.docx")

pq.printJob()