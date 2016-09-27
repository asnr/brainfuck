import unittest
import io

from interpreter.brainfuckinterpreter import BrainfuckInterpreter

class TestSystem(unittest.TestCase):
	
	def setUp(self):
		self.empty_in_stream = io.BytesIO()
		self.out_stream = io.BytesIO()
		self.interpreter = BrainfuckInterpreter()


	def test_print_A_program(self):
		program = ('+' * 65) + '.'
		
		self.interpreter.run(program, self.empty_in_stream, self.out_stream)

		self.assertEqual(b'A', self.out_stream.getvalue())


	def test_print_B_program(self):
		program = ('+' * 66) + '.'
		
		self.interpreter.run(program, self.empty_in_stream, self.out_stream)

		self.assertEqual(b'B', self.out_stream.getvalue())
	

	def test_print_C_then_A_program(self):
		program = ('+' * 67) + '.--.'	
		
		self.interpreter.run(program, self.empty_in_stream, self.out_stream)

		self.assertEqual(b'CA', self.out_stream.getvalue())


	def test_read_multibyte_character_from_unicode_stream(self):
		program = ','
		in_stream = io.StringIO('龙')

		with self.assertRaises(TypeError):
			self.interpreter.run(program, in_stream, self.out_stream)


	def test_print_character_after_inputted_character(self):
		program = ',+.'
		in_stream = io.BytesIO(b'Q')

		self.interpreter.run(program, in_stream, self.out_stream)

		self.assertEqual(b'R', self.out_stream.getvalue())


	def test_store_then_print_two_input_characters(self):
		program = ',>,<.>.'
		in_stream = io.BytesIO(b'xy')

		self.interpreter.run(program, in_stream, self.out_stream)

		self.assertEqual(b'xy', self.out_stream.getvalue())


	def test_print_A_that_is_created_with_a_loop(self):
		multiply_13_by_5_to_get_65 = ('+' * 13) + '[>' + ('+' * 5) + '<-]'
		print_65 = '>.'
		program = multiply_13_by_5_to_get_65 + print_65

		self.interpreter.run(program, self.empty_in_stream, self.out_stream)

		self.assertEqual(b'A', self.out_stream.getvalue())


	def test_print_B_that_is_created_with_nested_loops(self):
		multiply_11_by_2_by_3_to_get_66 = ('+' * 11) + '[>+++[>++<-]<-]'
		print_66 = '>>.'
		program = multiply_11_by_2_by_3_to_get_66 + print_66

		self.interpreter.run(program, self.empty_in_stream, self.out_stream)

		self.assertEqual(b'B', self.out_stream.getvalue())


	def test_print_input_full_of_comments(self):
		program = 'This is a comment, .20?!#é龙andmorecomments'
		in_stream = io.BytesIO(b'!')

		self.interpreter.run(program, in_stream, self.out_stream)

		self.assertEqual(b'!', self.out_stream.getvalue())
