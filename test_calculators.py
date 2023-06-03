from basic_calculator import BasicCalculator
from scientific_calculator import ScientificCalculator

# basic operations: "add() for addition, "subtract()" for subtraction
# "multiply()" fo multiplication, "divide()" for division
# for scientific calculator: "exponentiate()" for exponentiation, "root()" for nth root, 
# "notation()" for converting scientific notation to decimal notation

first_number = 1
second_number = 2
third_number = 4

calculator_one = BasicCalculator()
BasicCalculator.border("The answer is: " + str(calculator_one.add(first_number, second_number)))
BasicCalculator.border("The last answer is: " + str(calculator_one.last_answer()))
calculator_one.show_info()

calculator_two = BasicCalculator("Sharp")
BasicCalculator.border("The answer is: " + str(calculator_two.subtract(third_number, first_number)))
BasicCalculator.border("The last answer is: " + str(calculator_two.last_answer()))
calculator_two.show_info()

calculator_three = ScientificCalculator()
ScientificCalculator.border("The answer is: " + str(calculator_three.multiply(third_number, second_number)))
ScientificCalculator.border("The last answer is: " + str(calculator_three.last_answer()))
calculator_three.show_info()

calculator_four = ScientificCalculator("Casio")
ScientificCalculator.border("The answer is: " + str(calculator_four.exponentiate(second_number, third_number)))
ScientificCalculator.border("The last answer is: " + str(calculator_four.last_answer()))
calculator_four.show_info()