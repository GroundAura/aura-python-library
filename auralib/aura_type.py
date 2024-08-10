def get_type(data: any) -> str:
	try:
		data_type = type(data)
		if data_type == bool:
			return "bool"
		elif data_type == bytes:
			return "bytes"
		elif data_type == dict:
			return "dict"
		elif data_type == float:
			return "float"
		elif data_type == int:
			return "int"
		elif data_type == list:
			return "list"
		elif data_type == set:
			return "set"
		elif data_type == str:
			return "str"
		elif data_type == tuple:
			return "tuple"
		elif data_type == type(None):
			return "None"
		elif data_type == type(Ellipsis):
			return "Ellipsis"
		elif data_type == type(NotImplemented):
			return "NotImplemented"
		else:
			return "unknown"
	except Exception as e:
		raise Exception(f"Error while trying to get type of data {data}:\n  {e}")

def str_to_bool(string: str, case_sensitive: bool = False, true_values: list[str] | tuple[str] | str = ("TRUE", "True", "true", "T", "t", "1"), false_values: list[str] | tuple[str] | str = ("FALSE", "False", "false", "F", "f", "0")) -> bool:
	try:
		if not case_sensitive:
			string = string.lower()
			true_values: list[str] = sorted(set(value.lower() for value in true_values))
			false_values: list[str] = sorted(set(value.lower() for value in false_values))
		if string in true_values:
			return True
		elif string in false_values:
			return False
		else:
			true_values: list[str] = sorted(set(true_values))
			false_values: list[str] = sorted(set(false_values))
			raise Exception(f"Failed to convert str to bool. Valid values are: {true_values + false_values}. Case sensitive: '{case_sensitive}'.")
	except Exception as e:
		raise Exception(f"Error while trying to convert string '{string}' to a boolean:\n  {e}")

def str_to_dict(string: str) -> dict:
	try:
		if string.startswith("{") and string.endswith("}"):
			string: dict = eval(string)
		else:
			string: dict = eval("{" + string + "}")
		if type(string) == dict:
			return string
		else:
			raise Exception(f"Failed to convert str to dict.")
	except Exception as e:
		print(f"Error while trying to convert string '{string}' to a list:\n  {e}")

def str_to_float(string: str) -> float:
	try:
		string: float = float(string)
		if type(string) == float:
			return string
		else:
			raise Exception(f"Failed to convert str to float.")
	except Exception as e:
		print(f"Error while trying to convert string '{string}' to a float:\n  {e}")

def str_to_int(string: str) -> int:
	try:
		string: int = int(string)
		if type(string) == int:
			return string
		else:
			raise Exception(f"Failed to convert str to int.")
	except Exception as e:
		print(f"Error while trying to convert string '{string}' to an integer:\n  {e}")

def str_to_list(string: str) -> list:
	try:
		string: str = string.lstrip("[").rstrip("]")
		string: list = string.split(", ")
		if type(string) == list:
			return string
		else:
			raise Exception(f"Failed to convert str to list.")
	except Exception as e:
		print(f"Error while trying to convert string '{string}' to a list:\n  {e}")

def str_to_set(string: str) -> set:
	try:
		string: str = string.lstrip("{").rstrip("}")
		string: set = set(string.split(", "))
		if type(string) == set:
			return string
		else:
			raise Exception(f"Failed to convert str to set.")
	except Exception as e:
		print(f"Error while trying to convert string '{string}' to a set:\n  {e}")

def str_to_tuple(string: str) -> tuple:
	try:
		string: str = string.lstrip("(").rstrip(")")
		string: tuple = tuple(string.split(", "))
		if type(string) == tuple:
			return string
		else:
			raise Exception(f"Failed to convert str to tuple.")
	except Exception as e:
		print(f"Error while trying to convert string '{string}' to a tuple:\n  {e}")

def test() -> None:
	try:
	# get_type()
		data = 123
		data_type = get_type(data)
		print(f"get_type():")
		print(f"data = {data}")
		print(f"data_type = {data_type}")
		print()
	# str_to_bool()
		bool_as_str = "TrUe"
		bool_as_bool = str_to_bool(bool_as_str, case_sensitive=True, true_values=("TRUE", "True", "true", "T", "t", "1"), false_values=("FALSE", "False", "false", "F", "f", "0"))
		print(f"str_to_bool():")
		print(f"bool_as_str = {bool_as_str}")
		print(f"bool_as_bool = {bool_as_bool}")
		print(f"data_type = {get_type(bool_as_bool)}")
		print()
	# str_to_dict()
		dict_as_str = "{\"key\": \"value\"}"
		dict_as_dict = str_to_dict(dict_as_str)
		print(f"str_to_dict():")
		print(f"dict_as_str = {dict_as_str}")
		print(f"dict_as_dict = {dict_as_dict}")
		print(f"data_type = {get_type(dict_as_dict)}")
		print()
	# str_to_float()
		float_as_str = "123.456"
		float_as_float = str_to_float(float_as_str)
		print(f"str_to_float():")
		print(f"float_as_str = {float_as_str}")
		print(f"float_as_float = {float_as_float}")
		print(f"data_type = {get_type(float_as_float)}")
		print()
	# str_to_int()
		int_as_str = "123"
		int_as_int = str_to_int(int_as_str)
		print(f"str_to_int():")
		print(f"int_as_str = {int_as_str}")
		print(f"int_as_int = {int_as_int}")
		print(f"data_type = {get_type(int_as_int)}")
		print()
	# str_to_list()
		list_as_str = "[1, 2, 3]"
		list_as_list = str_to_list(list_as_str)
		print(f"str_to_list():")
		print(f"list_as_str = {list_as_str}")
		print(f"list_as_list = {list_as_list}")
		print(f"data_type = {get_type(list_as_list)}")
		print()
	# str_to_set()
		set_as_str = "{1, 2, 3}"
		set_as_set = str_to_set(set_as_str)
		print(f"str_to_set():")
		print(f"set_as_str = {set_as_str}")
		print(f"set_as_set = {set_as_set}")
		print(f"data_type = {get_type(set_as_set)}")
		print()
	# str_to_tuple()
		tuple_as_str = "(1, 2, 3)"
		tuple_as_tuple = str_to_tuple(tuple_as_str)
		print(f"str_to_tuple():")
		print(f"tuple_as_str = {tuple_as_str}")
		print(f"tuple_as_tuple = {tuple_as_tuple}")
		print(f"data_type = {get_type(tuple_as_tuple)}")
		print()
	except Exception as e:
		print(f"ERROR: {e}")
		exit()

if __name__ == "__main__":
	test()
