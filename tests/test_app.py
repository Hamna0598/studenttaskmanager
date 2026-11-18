
import unittest
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import app


class TestStudentTaskManager(unittest.TestCase):

    def setUp(self):
        app.tasks.clear()

    @patch("builtins.input", return_value="Python Assignment")
    def test_add_task(self, mock_input):
        app.add_task()

        self.assertEqual(len(app.tasks), 1)
        self.assertEqual(app.tasks[0]["title"], "Python Assignment")
        self.assertFalse(app.tasks[0]["completed"])

    @patch("builtins.input", return_value="1")
    def test_complete_task(self, mock_input):
        app.tasks.append({
            "id": 1,
            "title": "Python Assignment",
            "completed": False
        })

        app.complete_task()

        self.assertTrue(app.tasks[0]["completed"])

    @patch("builtins.input", side_effect=["1", "y"])
    def test_delete_task(self, mock_input):
        app.tasks.append({
            "id": 1,
            "title": "Python Assignment",
            "completed": False
        })

        app.delete_task()

        self.assertEqual(len(app.tasks), 0)


if __name__ == "__main__":
    unittest.main()
