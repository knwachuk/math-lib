from math_lib.mult import mult

class TestMult:
    def test_zero_property(self):
        assert mult(0, 0) == 0
        assert mult(0, 1) == 0
        assert mult(1, 0) == 0

    def test_one_property(self):
        assert mult(1, 1) == 1
        assert mult(1, 10) == 10
        assert mult(10, 1) == 10

    def test_positive_multiplication(self):
        assert mult(2, 3) == 6

    def test_negative_multiplication(self):
        assert mult(-2, 3) == -6
        assert mult(2, -3) == -6
