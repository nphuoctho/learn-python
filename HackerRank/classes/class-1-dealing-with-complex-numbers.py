"""

"""
import math

class Complex(object):  
    def __init__(self: 'Complex', real: float, imaginary: float) -> None:
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self: 'Complex', no: 'Complex') -> 'Complex':
      return Complex(self.real + no.real, self.imaginary + no.imaginary)
    
    def __sub__(self: 'Complex', no: 'Complex') -> 'Complex':
      return Complex(self.real - no.real, self.imaginary - no.imaginary)
    
    def __mul__(self: 'Complex', no: 'Complex') -> 'Complex':
      real_part = self.real * no.real - self.imaginary * no.imaginary
      imaginary_part = self.real * no.imaginary + self.imaginary * no.real
      return Complex(real_part, imaginary_part)
    
    def __truediv__(self: 'Complex', no: 'Complex') -> 'Complex':
        denom = math.pow(no.real, 2) + math.pow(no.imaginary, 2)
        real_part = (self.real * no.real + self.imaginary * no.imaginary) / denom
        imaginary_part = (self.imaginary * no.real - self.real * no.imaginary) / denom
        return Complex(real_part, imaginary_part)
      
    def mod(self: 'Complex') -> 'Complex':
        modulus = math.sqrt(math.pow(self.real, 2) + math.pow(self.imaginary, 2))
        return Complex(modulus, 0)
      
    def __str__(self: 'Complex') -> str:
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')