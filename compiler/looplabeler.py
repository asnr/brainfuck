from collections import namedtuple


LoopLabel = namedtuple('LoopLabel', ['open', 'close'])


class LoopLabeler:
	
	def __init__(self):
		self._loop_stack = []
		self._next_loop_id = 1

	
	def _next_loop_label(self):
		open_label = 'LOOP_{}_OPEN'.format(self._next_loop_id)
		close_label = 'LOOP_{}_CLOSE'.format(self._next_loop_id)

		self._next_loop_id += 1

		return LoopLabel(open=open_label, close=close_label)
	

	def open_loop(self):
		label = self._next_loop_label()
		self._loop_stack.append(label)
		return label


	def close_loop(self):
		label = self._loop_stack.pop()
		return label