
import unittest
import main
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout


class TestStudentTaskManager(unittest.TestCase):

    def setUp(self):
        main.tasks.clear()
        main.next_id = 1

    def test_add_task(self):
        with patch("builtins.input", return_value="Study Python"):
            main.add_task()

        self.assertEqual(len(main.tasks), 1)
        self.assertEqual(main.tasks[0]["title"], "Study Python")

    def test_complete_task(self):
        main.tasks.append({
            "id": 1,
            "title": "Study Python",
            "completed": False
        })

        with patch("builtins.input", return_value="1"):
            with redirect_stdout(StringIO()):
                main.complete_task()

        self.assertTrue(main.tasks[0]["completed"])

    def test_delete_task(self):
        main.tasks.append({
            "id": 1,
            "title": "Study Python",
            "completed": False
        })

        with patch("builtins.input", return_value="1"):
            with redirect_stdout(StringIO()):
                main.delete_task()

        self.assertEqual(len(main.tasks), 0)


if __name__ == "__main__":
    unittest.main()
