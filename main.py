class Calculator: 
    def add(self, a_subtract, b_subtract): 
        return a_subtract + b_subtract 
    def subtract(self, a_subtract, b_subtract): 
        return a_subtract - b_subtract 
    def multiply(self, a_subtract, b_subtract): 
        return a_subtract * b_subtract 
    def divide(self, a_subtract, b_subtract): 
        return a_subtract / b_subtract 
    def modulo(self, a_subtract, b_subtract): 
        return a_subtract % b_subtract 
    def power(self, a_subtract, b_subtract): 
        return a_subtract ** b_subtract 
    
if __name__ == "__main__": 
    calc = Calculator() 
    print("Addition: ", calc.add(10, 5)) 
    print("Subtraction: ", calc.subtract(10, 5)) 
    print("Multiplication: ", calc.multiply(10, 5)) 
    print("Division: ", calc.divide(10, 5)) 
    print("Modulo: ", calc.modulo(10, 5)) 
    print("Power: ", calc.power(10, 5)) 