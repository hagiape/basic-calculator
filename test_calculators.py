from basic_calculator import BasicCalculator
from scientific_calculator import ScientificCalculator

# basic operations: "add() for addition, "subtract()" for subtraction
# "multiply()" fo multiplication, "divide()" for division
# for scientific calculator: "exponentiate()" for exponentiation, "root()" for nth root, 
# "notation()" for converting scientific notation to decimal notation

first_number = 1
second_number = 2
third_number = 3
fourth_number  = 4

calculator1 = BasicCalculator()
calculator1.add()
calculator1.last_answer()
calculator1 = BasicCalculator(2, '*', BasicCalculator.answer, False)
calculator1.calculate()
calculator1.last_answer()
calculator1.show_info()

calculator2 = BasicCalculator(5, '^', 2, True, 'Casio')
calculator2.calculate()
calculator2.last_answer()
calculator2.show_info()

calculator2 = BasicCalculator(25,'root', 2, True, 'Casio')
calculator2.calculate()
calculator2 = BasicCalculator(2.525, 'notation', 3, True, 'Casio')
calculator2.calculate()