
import os
#import pathlib
#import pathlib2
#import shutil
#from os import getcwd as os_getcwd
#from pathlib import Path
#from pathlib2 import Path

def copy_file(source_path: str, destination_path: str) -> None:
	raise NotImplementedError

def copy_files(source_path: str, destination_path: str) -> None:
	raise NotImplementedError

def copy_folder(source_path: str, destination_path: str) -> None:
	raise NotImplementedError

def get_base_path(file_path: str) -> str:
	raise NotImplementedError

def get_file_name(file_path: str) -> str:
	raise NotImplementedError

def get_file_extension(file_path: str) -> str:
	raise NotImplementedError

def get_root_path() -> str:
	return os.getcwd()

def move_file(source: str, destination: str) -> None:
	raise NotImplementedError

def move_folder(source: str, destination: str) -> None:
	raise NotImplementedError

def rename_file(source: str, destination: str) -> None:
	raise NotImplementedError

def rename_folder(source: str, destination: str) -> None:
	raise NotImplementedError

def remove_file(file_path: str) -> None:
	raise NotImplementedError

def test() -> None:
	raise NotImplementedError

if __name__ == "__main__":
	test()
