class BasicCalculator:
    # class variables
    result = 0
    # constructor
    def __init__(self, first_number, second_number, is_scientific = False, brand = 'Brand X'):
        self.first_number = first_number
        self.second_number = second_number
        self.is_scientific = is_scientific
        self.brand = brand
    # calculator functions
    # add
    def add_numbers(self):
        try:
            self.result = self.first_number + self.second_number
            print(self.result)
        except:
            print('There is an error. Please initialize the object properly.')
    # subtract
    def subtract_numbers(self):
        try:
            self.result = self.first_number - self.second_number
            print(self.result)
        except:
            print('There is an error. Please initialize the object properly.')
    # multiply
    def multiply_numbers(self):
        try:
            self.result = self.first_number * self.second_number
            print(self.result)
        except:
            print('There is an error. Please initialize the object properly.')
    # divide
    def divide_numbers(self):
        try:
            self.result = self.first_number / self.second_number
            print(self.result)
        except:
            print('There is an error. Please initialize the object properly.')
    # this is similar to the "Ans" button in some calculators
    # which will print the answer of the last operation performed 
    def last_answer(self):
        print(self.result)