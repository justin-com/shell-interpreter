import unittest
import io
from contextlib import redirect_stdout
import builtins
from executor import execute_command
from parser import parse_command
from interpreter import run_interpreter


class TestExecute(unittest.TestCase):
    def test_execute_command_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            execute_command("echo", ["hello"])
        output = f.getvalue().strip()
        self.assertEqual(output, "hello")

    def test_execute_command_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            execute_command("cd", ["testing"])
        output = f.getvalue().strip()
        self.assertEqual(output, "cd: no such directory: testing")

    def test_execute_command_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            execute_command("echo", [])
        output = f.getvalue().strip()
        self.assertEqual(output, "echo: missing arg")

    def test_execute_command_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            execute_command("cd", [])
        output = f.getvalue().strip()
        self.assertEqual(output, "cd: missing arg")


    def test_parse_command_1(self):
        self.assertEqual(parse_command("test 123"), ("test", ["123"]))

    def test_parse_command_2(self):
        self.assertEqual(parse_command(""), ("", []))

    def test_parse_command_3(self):
        self.assertEqual(parse_command('echo "hello world"'), ("echo", ["hello world"]))


    def test_run_interpreter(self):
        inputs = [":show", "echo hello", ":exit"]
        def fake_input(prompt):
            return inputs.pop(0)
        
        original_input = builtins.input
        builtins.input = fake_input

        f = io.StringIO()
        with redirect_stdout(f):
            lines = run_interpreter()

        builtins.input = original_input
        output = f.getvalue().strip()

        self.assertIn("Interpreter mode: ':exit' to finish, ':show' to display buffer", output)
        self.assertIn("[]", output)
        self.assertIn("hello", output)
        self.assertEqual(lines, [("echo", ["hello"])])


if __name__ == "__main__":
    unittest.main()