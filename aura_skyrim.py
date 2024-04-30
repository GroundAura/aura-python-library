#import os
from os import path as os_path

def format_formid(formid: int | str, plugin: str, format: str = "0xformid~plugin") -> str:
	raise NotImplementedError

def is_bethesda_plugin(file_path: str) -> bool:
	return True if os_path.isfile(file_path) and file_path.endswith((".esp", ".esm", ".esl")) else False

def test() -> None:
	raise NotImplementedError

if __name__ == "__main__":
	test()
