class Rational(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, r):
        # a/b + c/d = (ad + bc) / bd
        a = self.a * r.b + self.b * r.a
        b = self.b * r.b
        return(Rational(a, b))

    def __sub__(self, r):
        a = self.a * r.b - self.b * r.a
        b = self.b * r.b
        return(Rational(a, b))

    def __mul__(self, r):
        a = self.a * r.a
        b = self.b * r.b
        return(Rational(a, b))

    def __truediv__(self, r):
        a = self.a * r.b
        b = self.b * r.a
        return(Rational(a, b))

    def __gt__(self, r):
        return self.a * r.b > self.b * r.a

    def __lt__(self, r):
        return self.a * r.b < self.b * r.a

    def __eq__(self, r):
        return self.a * r.b == self.b * r.a

    def __str__(self):
        return f'{self.a} / {self.b}'

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
