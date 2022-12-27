class Test:
    def __init__(self, a, b, c, d):
        self.A = a
        self.B = b
        self.C = c
        self.D = d

    def addAll(self):
        return self.A + self.B + self.C + self.D

    def minus(self,m,n):
        return m - n

    def multiply(self):
        return self.A * self.B * self.C * self.D

test = Test(6, 2, 3, 4)
print(test.A)
print(test.addAll())
print(test.minus(100,1))
print(test.multiply())