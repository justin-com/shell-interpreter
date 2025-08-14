import unittest
from main import (
    custom_map, custom_filter, custom_reduce,
    apply_until_false, map_with_index, conditional_pipeline
)


class TestHOFs(unittest.TestCase):
    def test_custom_map(self):
        self.assertEqual(custom_map(lambda x: x**2, [1,2,3]), [1,4,9])

    def test_custom_filter(self):
        self.assertEqual(custom_filter(lambda x: x % 2 == 0, [1,2,3,4]), [2,4])

    def test_custom_reduce(self):
        self.assertEqual(custom_reduce(lambda a,b: a+b, [1,2,3]), 6)
        self.assertEqual(custom_reduce(lambda a,b: a*b, [1,2,3], 2), 12)

    def test_apply_until_false(self):
        func = lambda x: x + 1
        cond = lambda x: x < 5
        self.assertEqual(apply_until_false(func, cond, [1,2,3,7,8]), [2,3,4,7,8])

    def test_map_with_index(self):
        func = lambda i, x: i * x
        self.assertEqual(map_with_index(func, [10,20,30]), [0,20,60])

    def test_conditional_pipeline(self):
        funcs = [lambda x: x + 1, lambda x: x * 2, lambda x: x - 3]
        cond  = lambda v: v % 2 == 0
        pipeline = conditional_pipeline(funcs, cond)
        self.assertEqual(pipeline([1,2,3,4]), [1,3,3,7])


if __name__ == "__main__":
    unittest.main()