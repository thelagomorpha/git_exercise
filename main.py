class Calculator: 
    def add(self, a, b): 
        return a + bagi 
    def subtract(self, a, b): 
        return a - bagi 
    def multiply(self, a, b): 
        return a * bagi 
    def divide(self, a, b): 
        return a / bagi 
    def modulo(self, a, b): 
        return a % bagi 
    def power(self, a, b): 
        return a ** bagi 
    
if __name__ == "__main__": 
    calc = Calculator() 
    print("Addition: ", calc.add(10, 5)) 
    print("Subtraction: ", calc.subtract(10, 5)) 
    print("Multiplication: ", calc.multiply(10, 5)) 
    print("Division: ", calc.divide(10, 5)) 
    print("Modulo: ", calc.modulo(10, 5)) 
    print("Power: ", calc.power(10, 5)) 