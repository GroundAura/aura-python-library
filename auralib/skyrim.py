#import os
#from os import path as os_path
from .files import has_extension, is_file

#def format_formid(formid: int | str, plugin: str, format: str = "0xformid~plugin") -> str:
#	raise NotImplementedError

def is_bethesda_plugin(file_path: str, check_if_file: bool = True) -> bool:
	if check_if_file and not is_file(file_path):
		return False
	return has_extension(file_path, (".esp", ".esm", ".esl"))

def test() -> None:
	file_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Skyrim Special Edition\\Data\\Skyrim.esm"
	print(f"is_bethesda_plugin('{file_path}') = {is_bethesda_plugin(file_path)}")

if __name__ == "__main__":
	test()
