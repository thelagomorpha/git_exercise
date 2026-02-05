class Calculator: 
    def add(self, y, z): 
        return y + z 
    def subtract(self, y, z): 
        return y - z 
    def multiply(self, y, z): 
        return y * z 
    def divide(self, y, z): 
        return y / z 
    def modulo(self, y, z): 
        return y % z 
    def power(self, y, z): 
        return y ** z 
    
if __name__ == "__main__": 
    calc = Calculator() 
    print("Addition: ", calc.add(10, 5)) 
    print("Subtraction: ", calc.subtract(10, 5)) 
    print("Multiplication: ", calc.multiply(10, 5)) 
    print("Division: ", calc.divide(10, 5)) 
    print("Modulo: ", calc.modulo(10, 5)) 
    print("Power: ", calc.power(10, 5)) 