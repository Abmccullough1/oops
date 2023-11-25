class Glass:
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def pour_in(self, amount):
        space_available = self.capacity - self.amount
        if amount <= space_available:
            self.amount += amount
        else:
            self.amount = self.capacity  # Fills the glass to its maximum capacity
            print("Glass is full")

    def pour_out(self, amount):
        if amount <= self.amount:
            self.amount -= amount
        else:
            self.amount = 0  