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

calculator_one = BasicCalculator()
BasicCalculator.border("The answer is: " + str(calculator_one.add(first_number, second_number)))
calculator_one.last_answer()
calculator_one.show_info()

# calculator2 = BasicCalculator(5, '^', 2, True, 'Casio')
# calculator2.calculate()
# calculator2.last_answer()
# calculator2.show_info()

# calculator2 = BasicCalculator(25,'root', 2, True, 'Casio')
# calculator2.calculate()
# calculator2 = BasicCalculator(2.525, 'notation', 3, True, 'Casio')
# calculator2.calculate()