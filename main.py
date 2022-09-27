a = int(input())
b = int(input())
class figure:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    def obj(self):
        print("{} - Длина\n{} - Ширина".format(self.lenght, self.width))
    def s(self):
        print("{} - Площадь".format())
squar = figure(a, b)
squar.obj()