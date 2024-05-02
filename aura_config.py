import configparser
from os import path as os_path

from aura_files import get_root_path
from aura_type import get_type, str_to_bool, str_to_dict, str_to_float, str_to_int, str_to_list, str_to_set, str_to_tuple

def config_to_dict(
		config: configparser.ConfigParser,
		root_dir_key: tuple[str] | str,
		root_dir_value: str,
		root_path: str | None,
		bool_case_sens: bool,
		bool_true: tuple[str] | str,
		bool_false: tuple[str] | str
		) -> dict[str, dict[str]]:
	config_dict: dict = {}
	root_path = root_path if root_path else get_root_path()
	config_dict: dict = {}
	for section in config.sections():
		section_dict: dict = {}
		for option in config.options(section):
			value: bool | dict[str, str] | float | int | list[str] | set | str | tuple[str] = config.get(section, option)
			if option.startswith("s", 0, 1):
				if option[1:].startswith(root_dir_key) or option.endswith(root_dir_key):
					if value.startswith(root_dir_value):
						value = root_path + value[len(root_dir_value):]
			elif option.startswith("b", 0, 1):
				value = str_to_bool(value, case_sensitive=bool_case_sens, true_values=bool_true, false_values=bool_false)
			elif option.startswith("i", 0, 1):
				value = str_to_int(value)
			elif option.startswith("f", 0, 1):
				value = str_to_float(value)
			elif option.startswith("l", 0, 1):
				value = str_to_list(value)
			elif option.startswith("t", 0, 1):
				value = str_to_tuple(value)
			elif option.startswith("d", 0, 1):
				value = str_to_dict(value)
			elif option.startswith("o", 0, 1):
				value = str_to_set(value)
			section_dict[option] = value
		config_dict[section] = section_dict
	return config_dict

def read_config(
		file_path: str,
		preserve_key_case: bool = False,
		comment_prefixes: tuple[str] = (";", "#", "//"),
		inline_comment_prefixes: tuple[str] = (";", "#", "//"),
		root_dir_key: tuple[str] | str = ("PATH", "Path", "path"),
		root_dir_value: str = "[ROOT]",
		root_path: str | None = None,
		bool_case_sens: bool = False,
		bool_true: tuple[str] | str = ("TRUE", "True", "true", "T", "t", "1"),
		bool_false: tuple[str] | str = ("FALSE", "False", "false", "F", "f", "0")
		) -> dict[str, dict[str]]:
	config = configparser.ConfigParser(comment_prefixes=comment_prefixes, inline_comment_prefixes=inline_comment_prefixes)
	if preserve_key_case:
		config.optionxform = lambda option: option
	print(f"INFO: Trying to read config file from: '{file_path}'.")
	try:
		if not os_path.exists(file_path):
			raise Exception(f"Config file not found: '{file_path}'.")
		config.read(file_path)
		print(f"INFO: Config file read successfully.")
	except Exception as e:
		raise Exception(f"ERROR: Error while trying to read config file: {e}")
	try:
		config_dict: dict[str, dict[str]] = config_to_dict(config, root_dir_key, root_dir_value, root_path, bool_case_sens, bool_true, bool_false)
	except Exception as e:
		raise Exception(f"ERROR: Error while trying to format config file: {e}")
	return config_dict

def test() -> None:
	CONFIG_PATH = os_path.join(get_root_path(), "examples", "example_config.ini")
	try:
		config = read_config(CONFIG_PATH, preserve_key_case=True, bool_case_sens=False)
		print(f"\nConfig ({CONFIG_PATH}):\n{config}")
		for section in config:
			print(f"\n'[{section}]'")
			for option in config[section]:
				print(f"'{option}': {get_type(config[section][option])} = '{config[section][option]}'")
	except Exception as e:
		print(e)
		exit()

if __name__ == "__main__":
	test()
