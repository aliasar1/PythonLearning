class Train:

    def __init__(self, name, totalSeats, fare):
        self.name = name
        self.totalSeats = totalSeats
        self.fare = fare

    def getFare(self):
        print(f"The fare of train {self.name} is: Rs {self.fare}")     

    def getInfo(self):
        print(f"The name of train is {self.name} and total seat are {self.totalSeats}")    

    def bookSeat(self):
        if self.totalSeats > 0:
            print("Your seats is booked successfully.")
            self.totalSeats = self.totalSeats - 1
        else:
            print("Sorry, train is full.")

    def cancelTicket(self):
        self.totalSeats = self.totalSeats + 1 
        print("Successfully cancelled!")

shalimar = Train("Shalimar Express: 101", 2, 300)      
shalimar.getInfo()
shalimar.getFare()
shalimar.bookSeat()

shalimar.getInfo()
shalimar.bookSeat()

shalimar.getInfo()
shalimar.cancelTicket()
shalimar.bookSeat()

shalimar.getInfo()
shalimar.bookSeat()
