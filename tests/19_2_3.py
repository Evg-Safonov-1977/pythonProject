import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_mulyiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division_calculation_correctly(self):
        assert self.calc.division(self, 10, 5) == 2

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 20, 10) == 10

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 15, 15) == 30