class Calculator: 
    def add(self, ciki, b): 
        return ciki + b 
    def subtract(self, ciki, b): 
        return ciki - b 
    def multiply(self, ciki, b): 
        return ciki * b 
    def divide(self, ciki, b): 
        return ciki / b 
    def modulo(self, ciki, b): 
        return ciki % b 
    def power(self, ciki, b): 
        return ciki ** b 
    
if __name__ == "__main__": 
    calc = Calculator() 
    print("Addition: ", calc.add(10, 5)) 
    print("Subtraction: ", calc.subtract(10, 5)) 
    print("Multiplication: ", calc.multiply(10, 5)) 
    print("Division: ", calc.divide(10, 5)) 
    print("Modulo: ", calc.modulo(10, 5)) 
    print("Power: ", calc.power(10, 5)) 