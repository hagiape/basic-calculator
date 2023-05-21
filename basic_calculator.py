class BasicCalculator:
    result = 0

    def __init__(self, first_number, operator, second_number, is_scientific = False, brand = 'Brand X'):
        self.first_number = float(first_number)
        self.operator = operator
        self.second_number = float(second_number)
        self.is_scientific = is_scientific
        self.brand = brand
    
    def calculate(self, operator):
        try:
            if operator == '+':
                self.result = self.first_number + self.second_number
            if operator == '-':
                self.result = self.first_number - self.second_number
            if operator == '*':
                self.result = self.first_number * self.second_number
            if operator == '/':
                self.result = self.first_number / self.second_number

            if self.result.is_integer():
                self.result = int(self.result)

            print(self.result)
        except ValueError:
            print('There is an error. Please initialize the calculator properly.')

    def add_numbers(self):
        try:
            self.result = self.first_number + self.second_number
            if self.result.is_integer():
                self.result = int(self.result)
            print(self.result)
        except:
            print('There is an error. Please initialize the object properly.')

    def subtract_numbers(self):
        try:
            self.result = self.first_number - self.second_number
            if self.result.is_integer():
                self.result = int(self.result)
            print(self.result)
        except:
            print('There is an error. Please initialize the object properly.')

    def multiply_numbers(self):
        try:
            self.result = self.first_number * self.second_number
            if self.result.is_integer():
                self.result = int(self.result)
            print(self.result)
        except:
            print('There is an error. Please initialize the object properly.')

    def divide_numbers(self):
        try:
            self.result = self.first_number / self.second_number
            if self.result.is_integer():
                self.result = int(self.result)
            print(self.result)
        except:
            print('There is an error. Please initialize the object properly.')
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
    def last_answer(self):
        print(self.result)