import unittest
import subprocess

import compiler.bf_compile as bf_compile
from test.expectedexecutions import ExpectedExecutions


class TestCompiler(unittest.TestCase, ExpectedExecutions):

	TEST_PROGRAM_DIR = 'test/programs/'

	def run_bf_program(self, program_filename, test_input=b''):
		program_path = self.TEST_PROGRAM_DIR + program_filename
		exe_path = bf_compile.compile_assemble_link(
			program_path, quiet_linker=True)
		proc = subprocess.run(
			[exe_path], input=test_input, stdout=subprocess.PIPE)

		return proc.stdout
