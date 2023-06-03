from basic_calculator import BasicCalculator

class ScientificCalculator(BasicCalculator):
    def exponentiate(self, first_number, second_number):
        ScientificCalculator.answer = first_number ** second_number
        ScientificCalculator.integer_conversion()
        return ScientificCalculator.answer
    def root(self, first_number, second_number):
        ScientificCalculator.answer = first_number ** (1/second_number)
        ScientificCalculator.integer_conversion()
        return ScientificCalculator.answer
    def notation(self, first_number, second_number):
        ScientificCalculator.answer = first_number * (10 ** second_number)
        ScientificCalculator.integer_conversion()
        return ScientificCalculator.answer