import unittest

from moabb.datasets import Ma2022


class TestMa2022(unittest.TestCase):
    def setUp(self):
        self.ds = Ma2022()

    def test_properties(self):
        self.assertEqual(len(self.ds.subject_list), 25)
        self.assertEqual(self.ds.paradigm, "motor_imagery")
        self.assertEqual(self.ds.interval, [4, 8])
        self.assertEqual(self.ds.event_id, {"left_hand": 1, "right_hand": 2})

    def test_data_path_structure(self):
        # We expect a ValueError for invalid subject
        with self.assertRaises(ValueError):
            self.ds.data_path(100)

        # We expect a list of paths for valid subject
        # Note: This will not check if files exist, just the path usage
        paths = self.ds.data_path(1)
        self.assertTrue(len(paths) == 5)  # 5 sessions


if __name__ == "__main__":
    unittest.main()
