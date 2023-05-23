# the code was modified, originally from Stack Overflow:
# https://stackoverflow.com/a/20757225
# function that creates text border based on the output
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

class BasicCalculator:
    answer = 0
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
                    BasicCalculator.answer = self.first_number ** self.second_number
                elif self.operator == 'root':
                    BasicCalculator.answer = self.first_number ** (1/self.second_number)
                elif self.operator == 'notation':
                    BasicCalculator.answer = self.first_number * (10 ** self.second_number)
                elif self.operator in ['+', '-', '*', '/']:
                    BasicCalculator.answer = eval(f"self.first_number {self.operator} self.second_number")

                if BasicCalculator.answer.is_integer():
                    BasicCalculator.answer = int(BasicCalculator.answer)
                border('The answer is: ' + str(BasicCalculator.answer))
            else:
                if self.operator in ['+', '-', '*', '/']:
                    BasicCalculator.answer = eval(f"self.first_number {self.operator} self.second_number")
                    if BasicCalculator.answer.is_integer():
                        BasicCalculator.answer = int(BasicCalculator.answer)
                    border('The answer is: ' + str(BasicCalculator.answer))
                else:
                    border('This calculator cannot perform that operation.')
        except:
            border('There is an error. Please initialize the calculator properly.')
    
    def show_info(self):
        if self.brand == 'Brand X':
            print('This is a generic brand of calculator.')
        else:
            print('This is a ' + self.brand + 'calculator.')

        if self.is_scientific:
            print('This is a scientific calculator.')
        else:
            print('This is a regular calculator.')

    # this is similar to the "Ans" button in some calculators
    # which will print the answer of the last operation performed 
    def last_answer(self):
        border('The last answer is: ' + str(BasicCalculator.answer))