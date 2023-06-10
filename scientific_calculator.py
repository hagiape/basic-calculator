from basic_calculator import BasicCalculator

class ScientificCalculator(BasicCalculator):
    def exponentiate(self, first_number, second_number):
        self.answer = float(first_number ** second_number)
        self.integer_conversion()
        return self.answer
    def root(self, first_number, second_number):
        self.answer = float(first_number ** 1/second_number)
        self.integer_conversion()
        return self.answer
    def notation(self, first_number, second_number):
        self.answer = float(first_number * 10 ** second_number)
        self.integer_conversion()
        return self.answer
    def show_info(self):
        if self.brand == 'Brand X':
            self.border('This is a generic brand of a scientific calculator.')
        else:
            self.border('This is a ' + self.brand + ' scientific calculator.')