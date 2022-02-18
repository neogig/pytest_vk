import pytest


class TestTuple:
    # simple first case
    def test_sizeof_tuple_smaller(self):
        testing_tuple = (1, 2, 4, 5, 1, 6, 7, 8, 9, 1)
        identical_list = list(testing_tuple)
        assert testing_tuple.__sizeof__() < identical_list.__sizeof__()

    # parametrized case
    @pytest.mark.parametrize("test_input, counting_element, expected", [
        ((), 1, 0),
        ((100, -100, 1000, 0), 100, 1),
        ((-100, 0, 100, 99999), -100, 1),
        ((-9999, 0, -9999, 999999), -9999, 2),
        ((-8888, 8888, 0, 8888), 8888, 2),
    ])
    def test_count(self, test_input, counting_element, expected):
        assert test_input.count(counting_element) == expected

    # negative case
    def test_remove(self):
        testing_tuple = (1, 2, 3, 4, 5, 6)
        try:
            assert testing_tuple.remove(1)
        except AttributeError as e:
            pass


class TestFloat:
    # simple first case
    def test_abs(self):
        num = -12.94098
        assert abs(num) > 0

    # parametrized case
    @pytest.mark.parametrize("test_input, expected", [
        (0.0, 0),
        (-0.0, -0),
        (-100.0, -100),
        (100.0, 100),
        (200.123456789, 200),
        (201.9, 202),
        (303.90, 304),
        (500.5, 500),
        (-500.5, -500),
    ])
    def test_round(self, test_input, expected):
        assert round(test_input) == expected

    # negative case
    def test_summ(self):
        num = 0.1
        for i in range(9):
            num += 0.1
        assert num != 1
