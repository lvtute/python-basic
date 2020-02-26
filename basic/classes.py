import os
os.system('cls')

#classes
class Square:
    def __init__(self, size_lenght):
        self.size_lenght = size_lenght

    def area(self):
        return self.size_lenght * self.size_lenght


my_square = Square(10)
print('Square size lenght is: %s' % my_square.size_lenght)