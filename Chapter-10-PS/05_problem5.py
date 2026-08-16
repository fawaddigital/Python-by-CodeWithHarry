# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

import random


class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fromStation, toStation):
        print(f"Your ticket is booked for train number {self.trainNo} from {fromStation} to {toStation}")

    def get_status(self):
        print(f"The status of train number {self.trainNo} is running on time")
    

    def get_fare(self, fromStation, toStation):
        print(f"The fare of train number {self.trainNo} from {fromStation} to {toStation} is {random.randint(100, 500)}")

t = Train(12345)
t.book("Karachi", "Lahore")
t.get_status()
t.get_fare("Karachi", "Lahore")

