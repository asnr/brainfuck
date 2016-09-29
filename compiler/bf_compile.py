import sys
import os
import subprocess

from compiler.brainfuckcompiler import BrainFuckCompiler


def compile_assemble_link(program_path, quiet_linker=False):
	with open(program_path, 'r') as fp:
		program = fp.read()

	compiler = BrainFuckCompiler()
	assembly = compiler.compile(program)

	path_no_ext = os.path.splitext(program_path)[0]

	assembly_path = path_no_ext + '.asm'
	with open(assembly_path, 'w') as assembly_fp:
		assembly_fp.write(assembly)

	object_path = path_no_ext + '.o'
	subprocess.run(['as', assembly_path, '-o', object_path])

	exe_path = path_no_ext
	linker_stderr = subprocess.PIPE if quiet_linker else None
	subprocess.run(
		['ld', '-lc', '-macosx_version_min', '10.8.5',
		 object_path, '-o', exe_path],
		stderr=linker_stderr)

	return exe_path


if __name__ == '__main__':
	compile_assemble_link(sys.argv[1])