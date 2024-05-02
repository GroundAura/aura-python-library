
import os
#import pathlib
#import pathlib2
import shutil
#from os import getcwd as os_getcwd
#from os import path as os_path
#from os import remove as os_remove
#from os import removedirs as os_removedirs
#from pathlib import Path
#from pathlib2 import Path
#from shutil import move as shutil_move

#def copy_file(source_path: str | tuple[str], destination_path: str) -> None:
#	raise NotImplementedError

#def copy_folder(source_path: str | tuple[str], destination_path: str) -> None:
#	raise NotImplementedError

def delete_file(file_path: str | tuple[str]) -> None:
	try:
		os.remove(file_path)
	except Exception as e:
		print(f"ERROR: Error while trying to delete file '{file_path}': {e}")

def delete_folder(file_path: str | tuple[str]) -> None:
	try:
		os.removedirs(file_path)
	except Exception as e:
		print(f"ERROR: Error while trying to delete folder '{file_path}: {e}")

def get_base_path(file_path: str) -> str:
	try:
		return os.path.dirname(file_path)
	except Exception as e:
		print(f"ERROR: Error while trying to get base path of '{file_path}': {e}")

def get_file_name(file_path: str, include_extension: bool = True) -> str:
	try:
		if include_extension:
			return os.path.basename(file_path)
		else:
			return os.path.splitext(os.path.basename(file_path))[0]
	except Exception as e:
		print(f"ERROR: Error while trying to get file name of '{file_path}': {e}")

def get_file_extension(file_path: str, include_dot: bool = True) -> str:
	try:
		if include_dot:
			return os.path.splitext(file_path)[1]
		else:
			return os.path.splitext(os.path.basename(file_path))[1]
	except Exception as e:
		print(f"ERROR: Error while trying to get file extension of '{file_path}': {e}")

def get_root_path() -> str:
	try:
		return os.getcwd()
	except Exception as e:
		print(f"ERROR: Error while trying to get current working directory: {e}")

def move_files(source_path: str | list[str] | tuple[str], destination_path: str, force_overwrite: bool = False) -> None:
	try:
		#output_to_dir: bool = True if os.path.isdir(destination_path) else False
		if type(source_path) in (tuple, list):
			#destination = os.path.join(os.path.dirname(source_path), destination_path) if destination_path == os.path.basename(destination_path) else destination_path
			#if os.path.isfile(destination) and not force_overwrite:
				#raise FileExistsError
			for source in source_path:
				if os.path.isdir(source):
					raise IsADirectoryError(f"ERROR: 'move_files()' does not support moving directories. '{source}' is a directory.")
				if os.path.isfile(destination_path):
					raise NotADirectoryError(f"ERROR: If source_path is a list or tuple, then destination_path must be a directory path. '{destination_path}' is a file.")
				file_name = get_file_name(source)
				try:
					os.makedirs(destination_path, exist_ok=True)
					shutil.move(source, destination_path)
					print(f"INFO: '{file_name}' moved to '{destination_path}'")
				except shutil.Error as Error:
					if force_overwrite:
						print(f"WARNING: '{file_name}' already exists at '{destination_path}'. Deleting file and trying again.")
						delete_file(destination_path)
						shutil.move(source, destination_path)
						print(f"INFO: Moved file:'{file_name}' changed to '{destination_path}'")
					else:
						raise Error(f"WARNING: '{file_name}' already exists at '{destination_path}'. Skipped moving file. Set the argument 'force_overwrite' to 'True' to force overwrite.")
		else:
			if os.path.isdir(source_path):
				raise IsADirectoryError(f"ERROR: 'move_files()' does not support moving directories. '{source_path}' is a directory.")
			file_name = get_file_name(source_path)
			try:
				shutil.move(source_path, destination_path)
				print(f"INFO: '{file_name}' moved to '{destination_path}'")
			except shutil.Error as Error:
				if force_overwrite:
					print(f"WARNING: '{file_name}' already exists at '{destination_path}'. Deleting file and trying again.")
					delete_file(destination_path)
					shutil.move(source_path, destination_path)
					print(f"INFO: '{file_name}' moved to '{destination_path}'")
				else:
					raise Error(f"WARNING: '{file_name}' already exists at '{destination_path}'. Skipped moving file. Set the argument 'force_overwrite' to 'True' to force overwrite.")
	except Exception as e:
		print(f"ERROR: Error while trying to move file '{source_path}' to '{destination_path}': {e}")

def move_folders(source_path: str | list[str] | tuple[str], destination_path: str) -> None:
	if type(source_path) in (tuple, list):
		for source in source_path:
			try:
				if os.path.isdir(source):
					raise NotADirectoryError(f"ERROR: 'move_folders()' does not support moving files. '{source}' is a file.")
				folder_name = os.path.basename(source)
				shutil.move(source, destination_path)
				print(f"INFO: Moved folder: '{folder_name}' changed to '{os.path.join(destination_path, folder_name)}'")
			except Exception as e:
				print(f"ERROR: Error while trying to move folder '{source}' to '{destination_path}': {e}")
	else:
		try:
			if os.path.isfile(source_path):
				raise NotADirectoryError(f"ERROR: 'move_folders()' does not support moving files. '{source_path}' is a file.")
			folder_name = os.path.basename(source_path)
			shutil.move(source_path, destination_path)
			print(f"INFO: Moved folder: '{folder_name}' changed to '{os.path.join(destination_path, folder_name)}'")
		except Exception as e:
			print(f"ERROR: Error while trying to move folder '{source_path}' to '{destination_path}': {e}")

def rename_file(file_path: str, new_name: str) -> None:
	try:
		if os.path.isdir(file_path):
			raise IsADirectoryError(f"ERROR: 'rename_file()' does not support renaming directories. '{file_path}' is a directory.")
		if new_name == get_file_name(new_name):
			destination_path = os.path.join(get_base_path(file_path), new_name)
		else:
			if os.path.isdir(new_name):
				raise IsADirectoryError(f"ERROR: A new file name much be specified. '{new_name}' is a directory.")
			destination_path = new_name
		shutil.move(file_path, destination_path)
		print(f"INFO: Renamed file: '{file_path}' changed to '{destination_path}'")
		#print(f"INFO: Renamed file: '{file_path}' renamed to '{new_name}'")
		#print(f"INFO: Renamed file: '{get_file_name(file_path)}' renamed to '{new_name}'")
	except Exception as e:
		print(f"ERROR: Error while trying to rename file '{file_path}' to '{new_name}': {e}")

def rename_folder(file_path: str, new_name: str) -> None:
	try:
		if os.path.isfile(file_path):
			raise NotADirectoryError(f"ERROR: 'rename_folder()' does not support renaming files. '{file_path}' is a file.")
		if new_name == os.path.basename(new_name):
			destination_path = os.path.join(get_base_path(file_path), new_name)
		else:
			if os.path.isfile(new_name):
				raise NotADirectoryError(f"ERROR: A new directory name much be specified. '{new_name}' is a file.")
			destination_path = new_name
		shutil.move(file_path, destination_path)
		print(f"INFO: Renamed folder: '{file_path}' changed to '{destination_path}'")
		#print(f"INFO: Renamed folder: '{file_path}' renamed to '{new_name}'")
		#print(f"INFO: Renamed folder: '{os.path.basename(file_path)}' renamed to '{new_name}'")
	except Exception as e:
		print(f"ERROR: Error while trying to rename folder '{file_path}' to '{new_name}': {e}")

def test() -> None:
	file_path = "C:\\Code\\Projects\\My Projects\\aurapy\\filemanager.py"
	#file_path = "filemanager.py"
	base_name = os.path.basename(file_path)
	print(f"{base_name}")
	identical = True if file_path == base_name else False
	print(f"{identical}")

if __name__ == "__main__":
	test()
