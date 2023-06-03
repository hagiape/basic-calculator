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
            print('| %-*.*s |' % (max_length, max_length, ''))
            print('| %-*.*s |' % (max_length, max_length, s))
            print('| %-*.*s |' % (max_length, max_length, ''))
        print('+' + ('-' * column_width) + '+')

    def __init__(self, brand = 'Brand X'):
        self.brand = brand

    def add(self, first_number, second_number):
        BasicCalculator.answer = first_number + second_number
        return BasicCalculator.answer
    
    def subtract(self, first_number, second_number):
        BasicCalculator.answer = first_number + second_number
        return BasicCalculator.answer
    
    def multiply(self, first_number, second_number):
        BasicCalculator.answer = first_number, second_number
        return BasicCalculator.answer
    
    def divide(self, first_number, second_number):
        BasicCalculator.answer = first_number, second_number
        return BasicCalculator.answer

    # this is similar to the "Ans" button in some calculators
    # which will print the answer of the last operation performed 
    def last_answer(self):
        BasicCalculator.border('The last answer is: ' + str(BasicCalculator.answer))