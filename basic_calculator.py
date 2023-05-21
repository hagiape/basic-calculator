class BasicCalculator:

    def __init__(self, first_number, operator, second_number, is_scientific = False, brand = 'Brand X'):
        self.first_number = float(first_number)
        self.operator = operator
        self.second_number = float(second_number)
        self.is_scientific = is_scientific
        self.brand = brand
    
    def calculate(self):
        result = 0
        try:
            if self.operator in ['+', '-', '*', '/']:
                result = eval(f"self.first_number {self.operator} self.second_number")
                if result.is_integer():
                    result = int(result)
                print(result)
            else:
                print('This calculator cannot perform that operation.')
        except ValueError:
            print('There is an error. Please initialize the calculator properly.')

    # the methods below are additional methods and only applicable
    # for the scientific calculator objects. 
    # if is_scientific == False, the method wouldn't run
    def exponentiate(self):
        if self.is_scientific:
            try:
                self.result = self.first_number ** self.second_number
                if self.result.is_integer():
                    self.result = int(self.result)
                print(self.result)
            except:
                print('There is an error. Please initialize the object properly.')
        else:
            print('This calculator can only perform simple arithmetic operations!')
            
    def nth_root(self):
        if self.is_scientific:
            try:
                self.result = self.first_number ** (1/self.second_number)
                if self.result.is_integer():
                    self.result = int(self.result)
                print(self.result)
            except:
                print('There is an error. Please initialize the object properly.')
        else:
            print('This calculator can only perform simple arithmetic operations!')

    def notation(self):
        if self.is_scientific:
            try:
                self.result = self.first_number * (10 ** self.second_number)
                if self.result.is_integer():
                    self.result = int(self.result)
                print(self.result)
            except:
                print('There is an error. Please initialize the object properly.')
        else:
            print('This calculator can only perform simple arithmetic operations!')
    # this is similar to the "Ans" button in some calculators
    # which will print the answer of the last operation performed 
    # def last_answer(self):
    #     print(self.result)