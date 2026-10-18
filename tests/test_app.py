import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import app  # noqa: E402


class FakeTable:
    def __init__(self):
        self.n = 0

    def update_item(self, **kwargs):
        self.n += 1
        return {"Attributes": {"hits": self.n}}


class TestApp(unittest.TestCase):
    def test_next_count_increments(self):
        t = FakeTable()
        self.assertEqual(app.next_count(t), 1)
        self.assertEqual(app.next_count(t), 2)


if __name__ == "__main__":
    unittest.main()
