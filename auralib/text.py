def lowercase(string: str | list[str] | tuple[str] | set[str] | dict[str, str]) -> str:
	"""
	Converts the specified string to lowercase.

	Args:
		string (str | list[str] | tuple[str] | set[str] | dict[str, str]): The string to convert to lowercase.

	Returns:
		str: The lowercase version of the specified string.
	"""
	try:
		if type(string) == str:
			return string.lower()
		elif type(string) in (list, set):
			for item in string:
				item.lower()
			return string
		elif type(string) == tuple:
			string = list(string)
			for item in string:
				item.lower()
			return tuple(string)
		elif type(string) == dict:
			for item in string:
				string[item.lower()] = string.pop(item)
		else:
			raise Exception(f"ERROR: Failed to convert string to lowercase: Unsupported type: {type(string)}")
	except Exception as e:
		print(f"ERROR: Error while trying to convert string to lowercase: {e}")

def read_from_file(file_path: str, encoding: str = "utf-8") -> str:
	"""
	Reads text from a text file.

	Args:
		file_path (str): The file path to read from.
		encoding (str, optional): The encoding of the target file. Defaults to "utf-8".

	Returns:
		str: The text from the file.
	"""
	try:
		with open(file_path, "r", encoding=encoding) as file:
			return file.read()
	except Exception as e:
		print(f"ERROR: Error while trying to read text from file '{file_path}': {e}")

def write_to_file(file_path: str, text: str = "", encoding: str = "utf-8") -> None:
	"""
	Creates a text file.

	Args:
		file_path (str): The file path to create.
		text (str, optional): The text to write to the file. Defaults to an empty string.
		encoding (str, optional): The encoding to use. Defaults to "utf-8".
	"""
	try:
		with open(file_path, "w", encoding=encoding) as file:
			file.write(text)
	except Exception as e:
		print(f"ERROR: Error while trying to create text file '{file_path}': {e}")

def test() -> None:
	raise NotImplementedError

if __name__ == "__main__":
	test()
