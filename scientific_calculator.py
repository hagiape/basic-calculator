from basic_calculator import BasicCalculator

class ScientificCalculator(BasicCalculator):
    def exponentiate(self, first_number, second_number):
        ScientificCalculator.answer = first_number ** second_number
        return ScientificCalculator.answer