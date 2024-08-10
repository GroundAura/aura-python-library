#import os
#import subprocess
from subprocess import run
from subprocess import CalledProcessError

def run_command(command: str | list[str], print_output: bool = False, use_shell: bool = False) -> None:
	try:
		if not print_output and not use_shell:
			run(command, check=True)
		elif not print_output and use_shell:
			run(command, check=True, shell=True)
		elif print_output and not use_shell:
			output = run(command, check=True, capture_output=True, text=True)
			print(f"INFO: Command output:\n\"\"\"\n{output.stdout}\"\"\"")
		elif print_output and use_shell:
			output = run(command, check=True, shell=True, capture_output=True, text=True)
			print(f"INFO: Command output:\n\"\"\"\n{output.stdout}\"\"\"")
		print(f"INFO: Finished running command: '{command}'")
	except CalledProcessError as e:
		print(f"ERROR: Error running command:\n\"\"\"\n{e}\n\"\"\"")
	except Exception as e:
		print(f"ERROR: Error running command '{command}':\"\n{e}\n\"")
	#finally:
	#	print(f"INFO: Finished running command: '{command}'")

def test() -> None:
	command = ["echo", "Hello World!"]
	run_command(command, print_output=True, use_shell=True)

if __name__ == "__main__":
	test()
