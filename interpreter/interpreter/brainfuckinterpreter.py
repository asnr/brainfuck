from interpreter.bracketmatcher import BracketMatcher

class BrainfuckInterpreter():

	DATA_ARRAY_SIZE = int(3e5)

	INST_INCREMENT_DATA = '+'
	INST_DECREMENT_DATA = '-'
	INST_INCREMENT_PTR = '>'
	INST_DECREMENT_PTR = '<'
	INST_READ = ','
	INST_WRITE = '.'
	INST_OPEN_BRACKET = '['
	INST_CLOSE_BRACKET = ']'

	def __init__(self):
		self._data_array = []
		self._data_ptr = 0
		self._reset()


	def _reset(self):
		self._data_array = [bytes([0])] * self.DATA_ARRAY_SIZE
		self._data_ptr = 0 


	def _get_bytes_at_ptr(self):
		return self._data_array[self._data_ptr]


	def _increment_data(self):
		incremented_value = self._get_bytes_at_ptr()[0] + 1
		self._data_array[self._data_ptr] = bytes([incremented_value])


	def _decrement_data(self):
		decremented_value = self._get_bytes_at_ptr()[0] - 1
		self._data_array[self._data_ptr] = bytes([decremented_value])


	def _increment_ptr(self):
		self._data_ptr += 1


	def _decrement_ptr(self):
		self._data_ptr -= 1


	def _read_next_byte(self, in_stream):
		try:
			bytes_read = bytes(in_stream.read(1))
		except TypeError:
			raise TypeError(
				'Could not convert input stream into bytes, ' +
				' check that it is not a text stream.')

		return bytes_read


	def run(self, program, in_stream, out_stream):
		self._reset()

		bracket_matcher = BracketMatcher(program)

		instruction_idx = 0
		while instruction_idx < len(program):
			instruction = program[instruction_idx]

			if instruction == self.INST_INCREMENT_DATA:
				self._increment_data()
				instruction_idx += 1

			elif instruction == self.INST_DECREMENT_DATA:
				self._decrement_data()
				instruction_idx += 1

			elif instruction == self.INST_INCREMENT_PTR:
				self._increment_ptr()
				instruction_idx += 1

			elif instruction == self.INST_DECREMENT_PTR:
				self._decrement_ptr()
				instruction_idx += 1

			elif instruction == self.INST_READ:
				input_byte = self._read_next_byte(in_stream)
				self._data_array[self._data_ptr] = input_byte
				instruction_idx += 1

			elif instruction == self.INST_WRITE:
				out_stream.write(self._get_bytes_at_ptr())
				instruction_idx += 1

			elif instruction == self.INST_OPEN_BRACKET:
				if self._get_bytes_at_ptr()[0] == 0:
					instruction_idx = \
						bracket_matcher.matching_close(instruction_idx) + 1
				else:
					instruction_idx += 1

			elif instruction == self.INST_CLOSE_BRACKET:
				instruction_idx = \
					bracket_matcher.matching_open(instruction_idx)

			else:
				# skip comments
				instruction_idx += 1
	