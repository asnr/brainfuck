from compiler.looplabeler import LoopLabeler


class BrainFuckCompiler():

	_PROLOGUE = """
.text
.globl _main
_main:
    pushq %rbp
    movq %rsp, %rbp
    pushq %r12         # store callee saved register
    subq $30008, %rsp  # allocate 30,008 B on stack, and realign

    leaq (%rsp), %rdi  # address of beginning of tape
    movl $0, %esi      # fill with 0's
    movq $30000, %rdx  # length 30,000 B
    call _memset       # memset

    movq %rsp, %r12    # we will be using %r12 as the tape pointer

"""

	_EPILOGUE = """
    addq $30008, %rsp
    popq %r12
    popq %rbp
    subq $8, %rsp      # align the stack pointer

    movq $0, %rdi
    call _exit
"""

	INDENT = '    '

	TAPE_PTR = '%r12'

	def __init__(self):
		self._assembly_list = None


	def _add_instr(self, instruction):
		self._assembly_list.append(self.INDENT + instruction + '\n')


	def _add_label(self, label):
		self._assembly_list.append(label + ':\n')


	def _add_increment_data_instr(self):
		instr = 'incb ({reg})'.format(reg=self.TAPE_PTR)
		self._add_instr(instr)


	def _add_decrement_data_instr(self):
		instr = 'decb ({reg})'.format(reg=self.TAPE_PTR)
		self._add_instr(instr)


	def _add_increment_ptr_instr(self):
		instr = 'incq {reg}'.format(reg=self.TAPE_PTR)
		self._add_instr(instr)


	def _add_decrement_ptr_instr(self):
		instr = 'decq {reg}'.format(reg=self.TAPE_PTR)
		self._add_instr(instr)


	def _add_putchar_instrs(self):
		# wipe the %rdi register
		self._add_instr('movq $0, %rdi')
		# %dil is the lowest byte of the %rdi register
		self._add_instr('movb (' + self.TAPE_PTR + '), %dil\n')
		self._add_instr('call _putchar')


	def _add_getchar_instrs(self):
		self._add_instr('call _getchar')
		self._add_instr('movb %al, (' + self.TAPE_PTR + ')')


	def _add_open_loop_instrs(self, open_label, close_label):
		self._add_label(open_label)
		self._add_instr('cmpb $0, (' + self.TAPE_PTR + ')')
		self._add_instr('je  ' + close_label)


	def _add_close_loop_instrs(self, open_label, close_label):
		self._add_instr('jmp ' + open_label)
		self._add_label(close_label)


	def compile(self, program):
		self._assembly_list = [self._PROLOGUE]

		loop_labeler = LoopLabeler()

		for instruction in program:
			if instruction == '+':
				self._add_increment_data_instr()
			elif instruction == '-':
				self._add_decrement_data_instr()
			elif instruction == '>':
				self._add_increment_ptr_instr()
			elif instruction == '<':
				self._add_decrement_ptr_instr()
			elif instruction == '.':
				self._add_putchar_instrs()
			elif instruction == ',':
				self._add_getchar_instrs()
			elif instruction == '[':
				loop_label = loop_labeler.open_loop()
				self._add_open_loop_instrs(loop_label.open, loop_label.close)
			elif instruction == ']':
				loop_label = loop_labeler.close_loop()
				self._add_close_loop_instrs(loop_label.open, loop_label.close)
			else:
				# ignore comments
				pass

		self._assembly_list.append(self._EPILOGUE)

		assembly = ''.join(self._assembly_list)

		self._assembly_list = None  # reset field

		return assembly
