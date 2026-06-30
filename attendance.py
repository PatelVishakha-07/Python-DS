""" Roll No. 1 Index 0
Roll No. 2 Index 1
Styles
Roll No. 30- Index 29
Since every student has a fixed slot (index), the teacher can directly go to any student's attendance without checking the previous records.
For example:
If the teacher wants to mark the attendance of Roll No. 16, they can directly access index 15.
There is no need to search from Roll No. 1 to Roll No. 16
This is called direct (random) access, which is the most important feature of an array
"""

class Attendance:

    def __init__(self):
        self.atd_sheet = ["AB"] * 30

    def markAttendance(self):
        rno = int(input("enter roll no: "))
        self.atd_sheet[rno-1] = "P"

    def showAttendance(self):    
        print("Attendance: ")
        print(self.atd_sheet)

atd = Attendance()
atd.markAttendance()
atd.showAttendance()