from basic_calculator import BasicCalculator

calculator1 = BasicCalculator(1,'+',2,False)
calculator1.calculate()
calculator1.last_answer()
calculator1 = BasicCalculator(2,'*',BasicCalculator.answer,False)
calculator1.calculate()
calculator1.last_answer()
calculator1.show_info()

calculator2 = BasicCalculator(5,'^',2,True,'Casio')
calculator2.calculate()
calculator2.last_answer()
calculator2.show_info()

calculator2 = BasicCalculator(25,'root',2,True,'Casio')
calculator2.calculate()
calculator2 = BasicCalculator(2.525,'notation',3,True,'Casio')
calculator2.calculate()