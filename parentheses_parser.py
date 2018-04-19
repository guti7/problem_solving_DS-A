from stack import Stack


    
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    
    strLen = len(symbolString)
    
    while index < strLen and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else: 
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
                
        index += 1
        
    return balanced and s.isEmpty()

def main():
    
    parString = "()"
    isValid = is_balanced_parentheses_string(parString)
    isValidParser = "true" if parChecker(parString) else "false"
    print("%-12s: valid? %s, parser: %s" %(parString, "true" if isValid else "false", isValidParser))
    
    parString = "(())"
    isValid = is_balanced_parentheses_string(parString)
    isValidParser = "true" if parChecker(parString) else "false"
    print("%-12s: valid? %s, parser: %s" %(parString, "true" if isValid else "false", isValidParser))
    
    parString = "(()()()())"
    isValid = is_balanced_parentheses_string(parString)
    isValidParser = "true" if parChecker(parString) else "false"
    print("%-12s: valid? %s, parser: %s" %(parString, "true" if isValid else "false", isValidParser))
    
    parString = "(((())))"
    isValid = is_balanced_parentheses_string(parString)
    isValidParser = "true" if parChecker(parString) else "false"
    print("%-12s: valid? %s, parser: %s" %(parString, "true" if isValid else "false", isValidParser))
    
    parString = "((((((())"
    isValid = is_balanced_parentheses_string(parString)
    isValidParser = "true" if parChecker(parString) else "false"
    print("%-12s: valid? %s, parser: %s" %(parString, "true" if isValid else "false", isValidParser))
    
    parString = "()))"
    isValid = is_balanced_parentheses_string(parString)
    isValidParser = "true" if parChecker(parString) else "false"
    print("%-12s: valid? %s, parser: %s" %(parString, "true" if isValid else "false", isValidParser))
    
    parString = "(()()(()"
    isValid = is_balanced_parentheses_string(parString)
    isValidParser = "true" if parChecker(parString) else "false"
    print("%-12s: valid? %s, parser: %s" %(parString, "true" if isValid else "false", isValidParser))
    
    
if __name__ == "__main__":
    main()