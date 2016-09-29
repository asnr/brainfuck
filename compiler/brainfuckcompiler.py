
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

    movq %rsp, %r12    # we will be using %r12 as the data pointer

"""

	_EPILOGUE = """
    addq $30008, %rsp
    popq %r12
    popq %rbp
    subq $8, %rsp      # align the stack pointer

    movq $0, %rdi
    call _exit
"""

	def __init__(self):
		pass


	def compile(self, program):
		assembly = [self._PROLOGUE]

		for instruction in program:
			if instruction == '+':
				assembly.append('    incb (%r12)\n')
			if instruction == '.':
				assembly.append('    movq $0, %rdi\n')
				assembly.append('    movb (%r12), %dil\n')
				assembly.append('    call _putchar\n')

		assembly.append(self._EPILOGUE)
		return ''.join(assembly)
