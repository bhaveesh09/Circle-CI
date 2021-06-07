"""
tests for calc app
"""
import calculator


class testCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3,2)

    def test_sub(self):
        assert 5 == calculator.subtract(10,5)

    def test_multiply(self):
        assert 4 == calculator.multiply(2,2)