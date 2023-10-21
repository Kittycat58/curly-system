class MoneyMachine:

    CURRENCY = "Rs"

    NOTE_VALUES = {
        "five_hundred": 500.00,
        "two_hundred": 200.00,
        "hundred": 100.00,
        "fifty": 50.00,
        "twenty": 20.00,
        "ten": 10.00
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_notes(self):
        """Returns the total calculated from notes inserted."""
        print("Please insert notes.")
        for note in self.NOTE_VALUES:
            self.money_received += int(input(f"How many {note}?: ")) * self.NOTE_VALUES[note]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_notes()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY} {change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
        
