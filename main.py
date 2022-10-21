from math import sqrt
from prettytable import PrettyTable
i = 0
print("Выберите кол-во фигур - ", end='')
n = int(input())
th = ["Фигуры"]
ts = ["Площади"]
tp = ["Периметры"]


while i < n:
    print("Выберите фигуру - треугольник, круг, четырехугольник")
    a = str(input())
    if a == "треугольник" or a == "Треугольник":
        print("Введите 3 координаты - точки пересечения сторон")
        print("x1 = ", end='')
        p1_x = int(input())
        print("y1 = ", end='')
        p1_y = int(input())
        print("x2 = ", end='')
        p2_x = int(input())
        print("y2 = ", end='')
        p2_y = int(input())
        print("x3 = ", end='')
        p3_x = int(input())
        print("y3 = ", end='')
        p3_y = int(input())
        th.append(a)
    elif a == "круг" or a == "Круг":
        print("Введите 2 координаты - центр окружности и любая точка окружности")
        print("x1 = ", end='')
        p1_x = int(input())
        print("y1 = ", end='')
        p1_y = int(input())
        print("x2 = ", end='')
        p2_x = int(input())
        print("y2 = ", end='')
        p2_y = int(input())
        th.append(a)
    elif a == "четырехугольник" or a == "Четырехугольник":
        print("Введите 4 координаты - точки пересечения сторон")
        print("x1 = ", end='')
        p1_x = int(input())
        print("y1 = ", end='')
        p1_y = int(input())
        print("x2 = ", end='')
        p2_x = int(input())
        print("y2 = ", end='')
        p2_y = int(input())
        print("x3 = ", end='')
        p3_x = int(input())
        print("y3 = ", end='')
        p3_y = int(input())
        print("x4 = ", end='')
        p4_x = int(input())
        print("y4 = ", end='')
        p4_y = int(input())
        th.append(a)

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __str__(self):
            return '({},{})'.format(self.x , self.y)
        def __add__(self, other):
            return Point(self.x + other.x, self.y + other.y)

    class figures:
        def __init__(self, lenght, width, hight):
            self.lenght = lenght
            self.width = width
            self.hight = hight
        def area(self):
                return self.width * self.lenght

    class triangle(figures):
        def __init__(self, t1, t2, t3):
            self.t1 = t1
            self.t2 = t2
            self.t3 = t3

        def sides(self):
            x1 = self.t1.x
            y1 = self.t1.y
            x2 = self.t2.x
            y2 = self.t2.y
            x3 = self.t3.x
            y3 = self.t3.y

            ab = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            bc = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
            ac = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
            return ab, bc, ac
        def p(self):
            ab, bc, ac = self.sides()
            p = ab + bc + ac
            return p
        def s(self):
            ab, bc, ac = self.sides()
            p = ab + bc + ac
            s = ((p / 2) * (((p / 2) - ab) * ((p / 2) - bc) * ((p / 2) - ac))) ** 0.5
            return s

    class fourangle(figures):
        def __init__(self, t6, t7, t8, t9):
            self.t6 = t6
            self.t7 = t7
            self.t8 = t8
            self.t9 = t9
        def sides(self):
            x1 = self.t6.x
            y1 = self.t6.y
            x2 = self.t7.x
            y2 = self.t7.y
            x3 = self.t8.x
            y3 = self.t8.y
            x4 = self.t9.x
            y4 = self.t9.y

            ab = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            bc = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
            cd = sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
            ad = sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)
            return ab, bc, cd, ad

        def po(self):
            ab, bc, cd, ac = self.sides()
            po = (ab+bc+cd+ac)
            return po
        def so(self):
            ab, bc, cd, ac = self.sides()
            so = (ab * cd)
            return so
    class circle(figures):

        def __init__(self, t4, t5):
            self.t4 = t4
            self.t5 = t5

        def sides(self):
            x4 = self.t4.x
            y4 = self.t4.y
            x5 = self.t5.x
            y5 = self.t5.y
            dc = sqrt((x5 - x4) ** 2 + (y5 - y4) ** 2)
            return dc

        def area2(self):
            dc = self.sides()
            results_3 = (dc ** 2) * 3.14
            return results_3
        def area3(self):
            dc = self.sides()
            results_4 = (dc * 2 * 3.14)
            return results_4

    if a == "круг" or a == "Круг":
        p1 = Point(p1_x, p1_y)
        p2 = Point(p2_x, p2_y)
        circ = circle(p1, p2)
        z5 = circ.area2()
        ts.append(z5)
        z6 = circ.area3()
        tp.append(z6)
    if a == "четырехугольник" or a == "Четырехугольник":
        p1 = Point(p1_x, p1_y)
        p2 = Point(p2_x, p2_y)
        p3 = Point(p3_x, p3_y)
        p4 = Point(p4_x, p4_y)
        four = fourangle(p1, p2, p3, p4)
        z3 = four.so()
        ts.append(z3)
        z4 = four.po()
        tp.append(z4)
    elif a == "треугольник" or a == "Треугольник":
        p1 = Point(p1_x, p1_y)
        p2 = Point(p2_x, p2_y)
        p3 = Point(p3_x, p3_y)
        tre = triangle(p1, p2, p3)
        z1 = tre.s()
        ts.append(z1)
        z2 = tre.p()
        tp.append(z2)
    i += 1

columns = len(th)

table = PrettyTable(th)

td_data = ts[:]
tp_data = tp[:]
while td_data:
    table.add_row(td_data[:columns])
    td_data = td_data[columns:]
while tp_data:
    table.add_row(tp_data[:columns])
    tp_data = tp_data[columns:]

print(table.get_string(sortby="Круг"))  # Печатаем таблицу


