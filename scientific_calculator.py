from basic_calculator import BasicCalculator

class ScientificCalculator(BasicCalculator):
    def integer_conversion(self):
        if ScientificCalculator.answer.is_integer:
            ScientificCalculator.answer = int(ScientificCalculator.answer)
    def exponentiate(self, first_number, second_number):
        ScientificCalculator.answer = float(first_number ** second_number)
        ScientificCalculator.integer_conversion(self)
        return ScientificCalculator.answer
    def root(self, first_number, second_number):
        ScientificCalculator.answer = float(first_number ** 1/second_number)
        ScientificCalculator.integer_conversion(self)
        return ScientificCalculator.answer
    def notation(self, first_number, second_number):
        ScientificCalculator.answer = float(first_number * 10 ** second_number)
        ScientificCalculator.integer_conversion(self)
        return ScientificCalculator.answer
    def show_info(self):
        if self.brand == 'Brand X':
            ScientificCalculator.border('This is a generic brand of a scientific calculator.')
        else:
            ScientificCalculator.border('This is a ' + self.brand + ' scientific calculator.')