class BasicCalculator:
    # class variables
    result = 0
    # constructor
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number
    # calculator functions
    # add
    def add_numbers(self):
        self.result = self.first_number + self.second_number
        print(self.result)
    # subtract
    def subtract_numbers(self):
        self.result = self.first_number - self.second_number
        print(self.result)
    # multiply
    def multiply_numbers(self):
        self.result = self.first_number * self.second_number
        print(self.result)
    # divide
    def divide_numbers(self):
        self.result = self.first_number / self.second_number
        print(self.result)
    # this is similar to the "Ans" button in some calculators
    # which will print the answer of the last operation performed 
    def last_answer(self):
        print(self.result)