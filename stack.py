class Stack(object):
    
    # Initializes an empty stack
    def __init__(self):
        self.items = []
    
    # Add the item to top
    def push(self, item):
        self.items.append(item)
    
    # Removes and returns the item at the top
    def pop(self):
        return self.items.pop()
    
    # Preview the item at top without removing it
    def peek(self):
        return self.items[self.size() - 1]
        
    # Check if the stack contains any elements
    def isEmpty(self):
        return self.size() < 1
    
    # Returns the number of items on the stack    
    def size(self):
        return len(self.items)
        
    def printStack(self):
        for item in self.items:
            print item,
    
    def __str__(self):
        string = "";
        for item in self.items:
            string += " " + str(item)
        return string
        
def main():
    
    # Testing Stack
    print("New Stack:")
    stack = Stack()
    print("Empty? %s" %(stack.isEmpty()))
    
    elem = 1
    print("Adding item: %i" %(elem))
    stack.push(elem)
    print("Empty? %s" %(stack.isEmpty()))
    print("Stack: %s" %(stack))
    # print("%s" %(stack))
    print("push more items...")
    stack.push(5)
    print("current size: %i" %(stack.size()))

    stack.push(0)
    print("current size: %i" %(stack.size()))

    stack.push(9)
    print("Stack: %s" %(stack))
    print("current size: %i" %(stack.size()))
    
    print("pop item...")
    stack.pop()
    print("Stack: %s" %(stack))
    print("current size: %i" %(stack.size()))

    
    print("peek...")
    elem = stack.peek()
    print("Stack: %s" %(stack))
    print("Peeked element: %i" %elem)
    print("current size: %i" %(stack.size()))
    
    string = "this is crazy!"
    print("\"%s\": reversed: \"%s\"" %(string, reverseString(string)))
    

def reverseString(string):
    stack = Stack()
    for ch in string:
        stack.push(ch)
    
    reversed = ''
    while not stack.isEmpty():
        reversed += stack.pop()
        
    return reversed
    
    # reverse = []
    # for i in range(stack.size()):
    #     reverse.append(stack.pop())
    # 
    # return "".join(reverse)
    
    # reversed = Stack()
    # for i in range(stack.size()):
    #     reversed.push(stack.pop())
    # 
    # return reversed.__str__()
    
if __name__ == "__main__":
    main()