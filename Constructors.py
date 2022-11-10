class Plane:
    def __init__(self, company, model, seats):
            self.company = company
            self.model = model
            self.seats = seats
    def wiki(self):
            print('The {} {} has {} seats'.format(self.company, self.model, self.seats))
    
p = Plane('Boeing', '737-MAX', 150)
p.wiki()
#Should print out 'The Boeing 737 Max has 150 seats'
