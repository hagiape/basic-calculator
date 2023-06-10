class BasicCalculator:
    answer = 0
    # this code was modified, originally from Stack Overflow:
    # https://stackoverflow.com/a/20757225
    # function that creates text border
    @classmethod
    def border(self, string):
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
        if self.answer.is_integer:
            self.answer = int(self.answer)

    def add(self, first_number, second_number):
        self.answer = float(first_number + second_number)
        self.integer_conversion()
        return self.answer
    
    def subtract(self, first_number, second_number):
        self.answer = float(first_number - second_number)
        self.integer_conversion()
        return self.answer
    
    def multiply(self, first_number, second_number):
        self.answer = float(first_number * second_number)
        self.integer_conversion()
        return self.answer
    
    def divide(self, first_number, second_number):
        self.answer = float(first_number / second_number)
        self.integer_conversion()
        return self.answer
    
    # this method shows information about the calculator object
    def show_info(self):
        if self.brand == 'Brand X':
            self.border('This is a generic brand of a basic calculator.')
        else:
            self.border('This is a ' + self.brand + ' basic calculator.')

    # this is similar to the "Ans" button in some calculators
    # which will print the answer of the last operation performed 
    def last_answer(self):
        return self.answer