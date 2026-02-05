class Calculator: 
    def add(self,  attar1,  attar2): 
        return attar1 + attar2
    def subtract(self,  attar1,  attar2): 
        return attar1 - attar2
    def multiply(self,  attar1,  attar2): 
        return attar1 * attar2
    def divide(self,  attar1,  attar2): 
        return attar1 / attar2
    def modulo(self,  attar1,  attar2): 
        return attar1 % attar2
    def power(self,  attar1,  attar2): 
        return attar1 ** attar2
    
if __name__ == "__main__": 
    calc = Calculator() 
    print("Addition: ", calc.add(10, 5)) 
    print("Subtraction: ", calc.subtract(10, 5)) 
    print("Multiplication: ", calc.multiply(10, 5)) 
    print("Division: ", calc.divide(10, 5)) 
    print("Modulo: ", calc.modulo(10, 5)) 
    print("Power: ", calc.power(10, 5)) 