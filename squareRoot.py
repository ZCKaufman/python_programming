import math

class SquareRoot():
    def sqrt(self, num) -> float:
        x0 = (1/2)*(num + 1.0)
        i = 0
        while(i <= 5):
            x0 = (1/2)*(x0 + (num/x0))
            i += 1
        return x0

obj = SquareRoot()
obj.sqrt(4)
obj.sqrt(10)
obj.sqrt(8)
obj.sqrt(6)
if __name__ == '__main__':
    obj = SquareRoot()
    i = 0
    while(i <= 100):
        print("Using Newton's method, the square root of " + str(i) + " is " + str(obj.sqrt(i)) + ". The Python Math library .sqrt() of " + str(i) + " is " + str(math.sqrt(i)) + ".")
        i += 1
