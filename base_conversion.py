from stack import Stack

def divide_by_2(number):
    converted = Stack()
    
    if (number == 0):
        converted.push(0)
    
    while (number != 0):
        converted.push(number % 2)
        number /= 2
    
    convertedString = ""
    while not converted.isEmpty():
        convertedString += str(converted.pop())
        
    return convertedString

def baseConverter(decimal, base):
    digits = "0123456789ABCDEF"
    
    converted = Stack()
    
    if (decimal == 0) :
        converted.push(0)
        
    while decimal > 0:
        digit = decimal % base
        converted.push(digits[digit])
        decimal /= base
        
    convertedString = ""
    while not converted.isEmpty():
        convertedString += converted.pop()
    
    return convertedString
    

def main():
    
    numberToConvert = 2
    convertedToBinary = divide_by_2(numberToConvert)
    print("number: %3i, base2: %10s" %(numberToConvert, convertedToBinary))
    
    numberToConvert = 5
    convertedToBinary = divide_by_2(numberToConvert)
    print("number: %3i, base2: %10s" %(numberToConvert, convertedToBinary))
    
    numberToConvert = 10
    convertedToBinary = divide_by_2(numberToConvert)
    print("number: %3i, base2: %10s" %(numberToConvert, convertedToBinary))
    
    numberToConvert = 42
    convertedToBinary = divide_by_2(numberToConvert)
    print("number: %3i, base2: %10s" %(numberToConvert, convertedToBinary))
    
    numberToConvert = 233
    convertedToBinary = divide_by_2(numberToConvert)
    print("number: %3i, base2: %10s" %(numberToConvert, convertedToBinary))
    
    numberToConvert = 0
    convertedToBinary = divide_by_2(numberToConvert)
    print("number: %3i, base2: %10s" %(numberToConvert, convertedToBinary))
    
    numberToConvert = 233
    convertedToBinary = baseConverter(numberToConvert, 8)
    print("number: %3i, base%2i: %10s" %(numberToConvert, 8, convertedToBinary))
    convertedToBinary = baseConverter(numberToConvert, 16)
    print("number: %3i, base%2i: %10s" %(numberToConvert, 16, convertedToBinary))
    
    numberToConvert = 10
    convertedToBinary = baseConverter(numberToConvert, 8)
    print("number: %3i, base%2i: %10s" %(numberToConvert, 8, convertedToBinary))
    convertedToBinary = baseConverter(numberToConvert, 16)
    print("number: %3i, base%2i: %10s" %(numberToConvert, 16, convertedToBinary))
    
    numberToConvert = 25
    convertedToBinary = baseConverter(numberToConvert, 2)
    print("number: %3i, base%2i: %10s" %(numberToConvert, 2, convertedToBinary))
    convertedToBinary = baseConverter(numberToConvert, 8)
    print("number: %3i, base%2i: %10s" %(numberToConvert, 8, convertedToBinary))
    convertedToBinary = baseConverter(numberToConvert, 16)
    print("number: %3i, base%2i: %10s" %(numberToConvert, 16, convertedToBinary))
    

if __name__ == '__main__':
    main()