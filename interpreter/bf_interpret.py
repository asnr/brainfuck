import sys
import os

from interpreter.brainfuckinterpreter import BrainfuckInterpreter


def main(program_filename):
	with open(program_filename, 'r') as fp:
		program = fp.read()

	stdin_bytes = os.fdopen(sys.stdin.fileno(), 'rb')
	stdout_bytes = os.fdopen(sys.stdout.fileno(), 'wb')

	intrepreter = BrainfuckInterpreter()
	intrepreter.run(program, stdin_bytes, stdout_bytes)


if __name__ == '__main__':
	main(sys.argv[1])