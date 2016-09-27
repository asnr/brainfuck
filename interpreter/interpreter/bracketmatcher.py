
class BracketMatcher:

	def __init__(self, program):
		find_opening_bracket_map, find_closing_bracket_map = \
			self._parse_program(program)

		self._find_opening_bracket_map = find_opening_bracket_map
		self._find_closing_bracket_map = find_closing_bracket_map


	def _parse_program(self, program):
		find_opening_bracket_map = {}
		find_closing_bracket_map = {}

		unclosed_open_brackets = []
		for idx, instruction in enumerate(program):
			if instruction == '[':
				unclosed_open_brackets.append(idx)
			elif instruction == ']':
				matching_open_bracket_idx = unclosed_open_brackets.pop()
				find_closing_bracket_map[matching_open_bracket_idx] = idx
				find_opening_bracket_map[idx] = matching_open_bracket_idx

		return (find_opening_bracket_map, find_closing_bracket_map)

	
	def matching_open(self, idx_of_close_bracket):
		return self._find_opening_bracket_map[idx_of_close_bracket]


	def matching_close(self, idx_of_open_bracket):
		return self._find_closing_bracket_map[idx_of_open_bracket]
