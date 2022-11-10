class Post:
    def __init__(self, title, name, date, count):
            self.title = title
            self.name = name
            self.date = date
            self.count = count
    def printPost(self):
            print('The title is {}, name is {}, date is {}, count is {}'.format(self.title, self.name, self.date, self.count))
    
p = Post('Title Test', 'Aneal', '10/11/2022', 100)
p.printPost()
#Should print out 'The title is Title Test, name is Aneal, date is 10/11/2022, count is 100'
