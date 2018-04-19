# Time analysis of python lists and its operations
# 
# Let's look at four different ways we might generate a list of `n`
# numbers starting at 0.
import timeit

# concatenation
def concatenationListTest():
    l = []
    for i in xrange(1000):
        l += [i]
    # print(l)
    
# append
def appendListTest():
    l = []
    for i in xrange(1000):
        l.append(i)

# list comprehension
def listComprehensionTest():
    l = [i for i in xrange(1000)]

# range function with constructor
def constructorListTest():
    l = list(xrange(1000))

def main():
    
    t1 = timeit.Timer("concatenationListTest()", "from __main__ import concatenationListTest")
    print("concat                ",t1.timeit(number=1000), "milliseconds")
    t2 = timeit.Timer("appendListTest()", "from __main__ import appendListTest")
    print("append                ",t2.timeit(number=1000), "milliseconds")
    t3 = timeit.Timer("listComprehensionTest()", "from __main__ import listComprehensionTest")
    print("comprehension         ",t3.timeit(number=1000), "milliseconds")
    t4 = timeit.Timer("constructorListTest()", "from __main__ import constructorListTest")
    print("list range constructor",t4.timeit(number=1000), "milliseconds")
    
if __name__ == '__main__':
    main()