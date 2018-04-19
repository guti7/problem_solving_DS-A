class LogicGate(object):
    def __init__(self, n):
        self.label = n
        self.output = None
        
    def getLabel(self):
        return self.label
        
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
        
    # Implement performGateLogic in subclass -  a specific gate is
    # needed to determine its logic


class BinaryGate(LogicGate):
    def __init__(self, n):
        super(BinaryGate, self).__init__(n)
        
        self.pinA = None
        self.pinB = None
    
    # Can properly choose the proper input line for a connection
    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")
    
            
    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + " --> "))
        else:
            return self.pinA.getFrom().getOutput()
    
        
    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + " --> "))
        else:
            return self.pinB.getFrom().getOutput()
        

class UnaryGate(LogicGate):
    def __init__(self, n):
        super(UnaryGate, self).__init__(n)
        
        self.pin = None
        
    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate " + self.getLabel() + " --> "))
        else:
            return self.pin.getFrom().getOutput()
    
    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


class AndGate(BinaryGate):
    def __init__(self, n):
        super(AndGate, self).__init__(n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return a and b
        # return 1 if a and b else 0


class OrGate(BinaryGate):
    def __init__(self, n):
        super(OrGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        return a or b
        # return 1 if a or b else 0


class NotGate(UnaryGate):
    def __init__(self, n):
        super(NotGate, self).__init__(n)

    def performGateLogic(self):
        pin = self.getPin()
        # return not pin
        return 0 if pin else 1

        
class NorGate(OrGate):
    
    def performGateLogic(self):
        return not super(NorGate, self).performGateLogic()
    

class NandGate(AndGate):
        
    def performGateLogic(self):
        return not super(NandGate, self).performGateLogic()

class Connector:
    def __init__(self, fromGate, toGate):
        self.fromGate = fromGate
        self.toGate = toGate
        
        toGate.setNextPin(self)
        
    def getFrom(self):
        return self.fromGate
        
    def getTo(self):
        return self.toGate

def main():

    # Gates tests
    # g1 = AndGate("G1")
    # outputG1 = g1.getOutput()
    # print("%s output: %i" %(g1.getLabel(), outputG1))
    # 
    # g2 = OrGate("G2")
    # outputG2 = g2.getOutput()
    # print("%s output: %i" %(g2.getLabel(), outputG2))
    # 
    # g3 = NotGate("G3")
    # outputG3 = g3.getOutput()
    # print("%s output: %i" %(g3.getLabel(), outputG3))
    
    # nor1 = NorGate("NOR1")
    # outputNor1 = nor1.getOutput()
    # print("%s output: %i" %(nor1.getLabel(), outputNor1))
    
    nand1 = NandGate("NAND1")
    outputNand1 = nand1.getOutput()
    print("%s output: %i" %(nand1.getLabel(), outputNand1))
    
    # Connector tests
    # and1 = AndGate("AND1")
    # and2 = AndGate("AND2")
    # or1 = OrGate("OR1")
    # not1 = NotGate("NOT1")
    # 
    # # Output from AND gates g1 and g2 is connected to OR gate g3, and that
    # # output is connected to the NOT gate g4. The output of the g4 is the final
    # # output of the circuit. 
    # c1 = Connector(and1, or1)
    # c2 = Connector(and2, or1)
    # c3 = Connector(or1, not1)
    # 
    # print(not1.getOutput())
    
if __name__ == '__main__':
    main()