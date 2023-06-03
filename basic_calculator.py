class BasicCalculator:
    answer = 0
    # this code was modified, originally from Stack Overflow:
    # https://stackoverflow.com/a/20757225
    # function that creates text border
    def border(string):
        text = string.splitlines()
        max_length = max(len(s) for s in text)
        column_width = max_length + 2
        print('+' + ('-' * column_width) + '+')
        for s in text:
            print('| %-*.*s |' % (max_length, max_length, s))
        print('+' + ('-' * column_width) + '+')

    def __init__(self, brand = 'Brand X'):
        self.brand = brand
    
    def integer_conversion(self):
        if BasicCalculator.answer.is_integer:
            BasicCalculator.answer = int(BasicCalculator.answer)

    def add(self, first_number, second_number):
        BasicCalculator.answer = float(first_number + second_number)
        BasicCalculator.integer_conversion(self)
        return BasicCalculator.answer
    
    def subtract(self, first_number, second_number):
        BasicCalculator.answer = float(first_number + second_number)
        BasicCalculator.integer_conversion(self)
        return BasicCalculator.answer
    
    def multiply(self, first_number, second_number):
        BasicCalculator.answer = float(first_number * second_number)
        BasicCalculator.integer_conversion(self)
        return BasicCalculator.answer
    
    def divide(self, first_number, second_number):
        BasicCalculator.answer = float(first_number / second_number)
        BasicCalculator.integer_conversion(self)
        return BasicCalculator.answer
    
    # this method shows information about the calculator object
    def show_info(self):
        if self.brand == 'Brand X':
            BasicCalculator.border('This is a generic brand of a basic calculator.')
        else:
            BasicCalculator.border('This is a ' + self.brand + ' basic calculator.')

    # this is similar to the "Ans" button in some calculators
    # which will print the answer of the last operation performed 
    def last_answer(self):
        return BasicCalculator.answer