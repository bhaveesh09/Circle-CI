"""
tests for calc app
"""
import calculator


class testCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3,2)

    def test_add(self):
        assert 5 == calculator.sub(10,5)
