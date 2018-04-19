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
    

if __name__ == '__main__':
    main()