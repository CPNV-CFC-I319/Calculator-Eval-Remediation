import unittest

from src.MathFun import MathFun, FunOperatorNotSupportedException, EqualityException
from src.MathRequest import MathRequest


class TestMatFun(unittest.TestCase):

    def setUp(self):
        pass

    def test_execute_max_get_max(self):
        # given
        math_request = MathRequest(3, 'max', 4)

        # when and then
        self.assertEqual(4, MathFun.execute(math_request))

    def test_execute_max_equality_throw_exception(self):
        # given
        math_request = MathRequest(4, 'max', 4)

        # when and then
        self.assertRaises(EqualityException, MathFun.execute, math_request)

    def test_execute_is_sum_even_true(self):
        # given
        math_request = MathRequest(2, 'is_sum_even', 4)

        # when and then
        self.assertEqual(True, MathFun.execute(math_request))

    def test_execute_is_sum_even_false(self):
        # given
        math_request = MathRequest(3, 'is_sum_even', 4)

        # when and then
        self.assertEqual(False, MathFun.execute(math_request))

    def test_execute_not_supported_fun_operator_throw_exception(self):
        # given
        math_request = MathRequest(3, 'not_supported_fun_operator', 4)

        # when and then
        self.assertRaises(FunOperatorNotSupportedException, MathFun.execute, math_request)

    def test_execute_sum_abs_positive_sum_get_result(self):
        # given
        math_request = MathRequest(3, 'sum_abs', 4)

        # when and then
        self.assertEqual(7, MathFun.execute(math_request))

    def test_execute_sum_abs_negative_sum_get_result(self):
        # given
        math_request = MathRequest(3, 'sum_abs', -4)

        # when and then
        self.assertEqual(1, MathFun.execute(math_request))

    def test_execute_sum_abs_zero_sum_get_result(self):
        # given
        math_request = MathRequest(3, 'sum_abs', -3)

        # when and then
        self.assertEqual(0, MathFun.execute(math_request))

    def test_execute_reverse_max_positive_max_get_result(self):
        # given
        math_request = MathRequest(4, 'reverse_max', 5)

        # when and then
        self.assertEqual(-5, MathFun.execute(math_request))

    def test_execute_reverse_max_negative_max_get_result(self):
        # given
        math_request = MathRequest(4, 'reverse_max', -5)

        # when and then
        self.assertEqual(-4, MathFun.execute(math_request))

    def test_execute_reverse_max_equality_throw_exception(self):
        # given
        math_request = MathRequest(-5, 'reverse_max', -5)

        # when and then
        self.assertRaises(EqualityException, MathFun.execute, math_request)


if __name__ == '__main__':
    unittest.main()