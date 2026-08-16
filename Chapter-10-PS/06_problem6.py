# Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects.
import random


class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(slf, fromStation, toStation):
        print(f"Your ticket is booked for train number {slf.trainNo} from {fromStation} to {toStation}")

    def get_status(slf):
        print(f"The status of train number {slf.trainNo} is running on time")
    

    def get_fare(slf, fromStation, toStation):
        print(f"The fare of train number {slf.trainNo} from {fromStation} to {toStation} is {random.randint(100, 500)}")

t = Train(12345)
t.book("Karachi", "Lahore")
t.get_status()
t.get_fare("Karachi", "Lahore")
