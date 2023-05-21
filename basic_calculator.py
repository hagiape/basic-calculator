class BasicCalculator:
    result = 0

    def __init__(self, first_number, second_number, is_scientific = False, brand = 'Brand X'):
        # this is to prevent unnecessary conversion of input to float
        # when performing basic artithmetic operations. the result will 
        # always be an integer except when performing simple division
        if '.' in first_number or second_number:
            self.first_number = float(first_number)
            self.second_number = float(second_number)
        else:
            self.first_number = int(first_number)
            self.second_number = int(second_number)
        self.is_scientific = is_scientific
        self.brand = brand

    def add_numbers(self):
        try:
            self.result = self.first_number + self.second_number
            print(self.result)
        except:
            print('There is an error. Please initialize the object properly.')

    def subtract_numbers(self):
        try:
            self.result = self.first_number - self.second_number
            print(self.result)
        except:
            print('There is an error. Please initialize the object properly.')

    def multiply_numbers(self):
        try:
            self.result = self.first_number * self.second_number
            print(self.result)
        except:
            print('There is an error. Please initialize the object properly.')

    def divide_numbers(self):
        try:
            self.result = self.first_number / self.second_number
            print(self.result)
        except:
            print('There is an error. Please initialize the object properly.')
    # the methods below are additional methods and only applicable
    # for the scientific calculator objects. 
    # if is_scientific == False, the method wouldn't run
    def exponentiate(self):
        if self.is_scientific == True:
            try:
                self.result = self.first_number ** self.second_number
                print(self.result)
            except:
                print('There is an error. Please initialize the object properly.')
        else:
            print('This calculator can only perform simple arithmetic operations!')
    # this is similar to the "Ans" button in some calculators
    # which will print the answer of the last operation performed 
    def last_answer(self):
        print(self.result)