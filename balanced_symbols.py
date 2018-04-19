from stack import Stack

def is_balanced(string):
    # stack for opening parentheses
    open_symbols = Stack()
    
    for ch in string:
        if ch in '({[':
            open_symbols.push(ch)
        elif ch in ')}]':
            if not open_symbols.isEmpty():
                top = open_symbols.pop()
                if not matches(top, ch):
                    return False
            else:
                return False
    
    return open_symbols.isEmpty();
    
def matches(top, ch):
    open = "({["
    close = ")}]"
    return open.index(top) == close.index(ch)

def main():
    print(is_balanced('{{([][])}()}'))
    print(is_balanced('[{()]'))

if __name__ == '__main__':
    main()