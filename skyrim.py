#import os
from os import path as os_path

def format_formid(formid: int | str, plugin: str, format: str = "0xformid~plugin") -> str:
	raise NotImplementedError

def is_bethesda_plugin(file_path: str) -> bool:
	plugin_extensions: tuple[str] = (".esp", ".esm", ".esl")
	if not os_path.isfile(file_path) or not file_path.endswith(plugin_extensions):
		return False
	return True

def test() -> None:
	raise NotImplementedError

if __name__ == "__main__":
	test()
