
class ExpectedExecutions:

	TEST_PROGRAM_DIR = 'test/programs/'

	def program_path_from_filename(self, program_filename):
		return self.TEST_PROGRAM_DIR + program_filename


	def run_bf_program(self, program_filename, test_input=b''):
		raise Exception()


	def test_print_A_program(self):
		output = self.run_bf_program('1_print_A.bf')
		self.assertEqual(b'A', output)


	def test_print_B_program(self):
		output = self.run_bf_program('2_print_B.bf')
		self.assertEqual(b'B', output)
	

	def test_print_C_then_A_program(self):
		output = self.run_bf_program('3_print_C_then_A.bf')
		self.assertEqual(b'CA', output)


	def test_print_character_after_inputted_character(self):
		output = self.run_bf_program(
			'4_print_char_after_input_char.bf', test_input=b'Q')
		self.assertEqual(b'R', output)


	def test_store_then_print_two_input_characters(self):
		output = self.run_bf_program(
			'store_then_print_two_input_characters.bf', b'xy')
		self.assertEqual(b'xy', output)


	def test_print_A_that_is_created_with_a_loop(self):
		output = self.run_bf_program('print_A_that_is_created_with_a_loop.bf')
		self.assertEqual(b'A', output)


	def test_print_B_that_is_created_with_nested_loops(self):
		output = self.run_bf_program(
			'print_B_that_is_created_with_nested_loops.bf')
		self.assertEqual(b'B', output)


	def test_print_input_full_of_comments(self):
		output = self.run_bf_program(
			'print_input_full_of_comments.bf', test_input=b'!')
		self.assertEqual(b'!', output)

	def test_print_hello_world(self):
		output = self.run_bf_program('hello_world.bf')
		self.assertEqual(b'Hello world', output)

	def test_print_hello_world_wikipedia(self):
		output = self.run_bf_program('hello_world_wikipedia.bf')
		self.assertEqual(b'Hello World!\n', output)
