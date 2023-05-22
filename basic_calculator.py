class BasicCalculator:
    result = 0
    def __init__(self, first_number, operator, second_number, is_scientific = False, brand = 'Brand X'):
        self.first_number = float(first_number)
        self.operator = operator
        self.second_number = float(second_number)
        self.is_scientific = is_scientific
        self.brand = brand
    
    def calculate(self):
        try:
            # the conditionals below are additional methods and only applicable
            # for the scientific calculator objects. 
            # if is_scientific == False, the method wouldn't run
            if self.is_scientific:
                if self.operator == '^':
                    BasicCalculator.result = self.first_number ** self.second_number
                elif self.operator == 'root':
                    BasicCalculator.result = self.first_number ** (1/self.second_number)
                elif self.operator == 'notation':
                    BasicCalculator.result = self.first_number * (10 ** self.second_number)
                elif self.operator in ['+', '-', '*', '/']:
                    BasicCalculator.result = eval(f"self.first_number {self.operator} self.second_number")

                if BasicCalculator.result.is_integer():
                    BasicCalculator.result = int(BasicCalculator.result)
                print(BasicCalculator.result)
            else:
                if self.operator in ['+', '-', '*', '/']:
                    BasicCalculator.result = eval(f"self.first_number {self.operator} self.second_number")
                    if BasicCalculator.result.is_integer():
                        BasicCalculator.result = int(BasicCalculator.result)
                    print(BasicCalculator.result)
                else:
                    print('This calculator cannot perform that operation.')
        except ValueError:
            print('There is an error. Please initialize the calculator properly.')

    # this is similar to the "Ans" button in some calculators
    # which will print the answer of the last operation performed 
    def last_answer(self):
        print(BasicCalculator.result)