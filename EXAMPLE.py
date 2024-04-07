import unittest

class TestExample(unittest.TestCase):

    def test_correct_use(self):
        self.assertEqual(len(["a", "b", "c"]), 3)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            len(1)

    def test_too_many(self):
        self.assertEqual(len(["a", "b", "c"]), 3)
        self.assertEqual(len(["d", "e", "f"]), 3)
        self.assertEqual(len(["g", "h", "i"]), 3)

    def test_good_variety(self):
        self.assertEqual(len(["a", "b", "c"]), 3)
        self.assertEqual(len((1, 2, 3)), 3)
        self.assertEqual(len("abc"), 3)

if __name__ == "__main__":
    unittest.main()
