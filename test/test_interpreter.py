import unittest
import subprocess

from test.expectedexecutions import ExpectedExecutions

class TestInterpreter(unittest.TestCase, ExpectedExecutions):

	def run_bf_program(self, program_filename, test_input=b''):
		program_path = self.program_path_from_filename(program_filename)
		proc = subprocess.run(
			['python', 'interpreter/bf_interpret.py', program_path],
			input=test_input, stdout=subprocess.PIPE)

		return proc.stdout
		