class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
        
    def __add__(self, fraction):
        newNum = self.numerator * fraction.denominator + fraction.numerator * self.denominator
        newDen = self.denominator * fraction.denominator
        divisor = gcd(newNum, newDen)
        return Fraction(newNum / divisor, newDen / divisor)
        
    def __eq__(self, fraction):
        return self.numerator * fraction.denominator == fraction.numerator * self.denominator
        
    def __sub__(self, other):
        newNum = self.numerator * other.denominator - other.numerator * self.denominator
        newDen = self.denominator * other.denominator
        if (newNum == 0):
            return 0
        divisor = gcd(newNum, newDen)
        return Fraction(newNum / divisor, newDen / divisor)
    
    def __mul__(self, other):
        newNum = self.numerator * other.numerator
        newDen = self.denominator * other.denominator
        divisor = gcd(newNum, newDen)
        return Fraction(newNum / divisor, newDen /divisor)
    
    def __div__(self, other):
        newNum = self.numerator * other.denominator
        newDen = self.denominator * other.numerator
        if (newNum == newDen):
            return 1
        divisor = gcd(newNum, newDen)
        return Fraction(newNum / divisor, newDen / divisor)
    
    def __lt__(self, other):
        return self.numerator / float(self.denominator) < other.numerator / float(other.denominator)
    
    def __gt__(self, other):
        return self.numerator / float(self.denominator) > other.numerator / float(other.denominator)
        
        
    
def gcd( m, n):
    while m % n != 0:
        oldM = m
        oldN = n
        
        m = oldN
        n = oldM % oldN
    return n

def main():    
    fraction = Fraction(1, 2)
    frac2 = Fraction(1, 4)
    print(fraction)
    print(fraction + frac2)
    frac3 = Fraction(1, 2)
    frac4 = Fraction(3, 1)

    print(fraction == frac3)
    print("\nSubstract:")
    print(fraction - frac3)
    print(fraction - frac2)

    print("\nMultiply:")
    print(fraction * frac2)
    print(fraction * frac3)
    print(frac2 * frac3)

    print("\nDivide:")
    print(fraction / frac4)
    print(fraction / frac3)

    print("\nComparison:")
    print("%s < %s: %s" %(fraction, frac3, fraction < frac3))
    print("%s < %s: %s" %(fraction, frac2, fraction < frac2))
    print("%s < %s: %s" %(frac2, fraction, frac2 < fraction))
    print("%s > %s: %s" %(fraction, frac3, fraction > frac3))
    print("%s > %s: %s" %(fraction, frac2, fraction > frac2))
    print("%s > %s: %s" %(frac2, fraction, frac2 > fraction))

if __name__ == '__main__':
    main()