import configparser
#from os import getcwd as get_root_path
from os import path as os_path

#import sys
#sys.path.append("./")
from aura_files import get_root_path

def read_config(file_path: str, preserve_keys_case: bool = False, debug: bool = False, root_dir_key: tuple[str] | str = ("PATH", "Path", "path", "sPATH", "sPath", "spath"), root_dir_value: str = "[ROOT]", true_values: tuple[str] | str = ("TRUE", "True", "true", "T", "t", "1"), false_values: tuple[str] | str = ("FALSE", "False", "false", "F", "f", "0")) -> dict[str, dict[str]]:
	config = configparser.ConfigParser(
		comment_prefixes=(";", "#", "//"),
		inline_comment_prefixes=(";", "#", "//")
	)
	if preserve_keys_case:
		config.optionxform = lambda option: option
	print(f"INFO: Trying to read config file from: '{file_path}'.")
	if not os_path.exists(file_path):
		raise Exception(f"ERROR: Config file not found: '{file_path}'.")
	try:
		config.read(file_path)
		print(f"INFO: Config file read successfully.")
	except Exception as e:
		print(f"ERROR: Error while trying to read config file: {e}")
		return
	valid_boolean_values = true_values + false_values
	root_path = get_root_path()
	config_dict: dict = {}
	for section in config.sections():
		section_dict: dict = {}
		for option in config.options(section):
			value: bool | dict[str, str] | float | int | list[str] | set | str | tuple[str] = config.get(section, option)
			if option.startswith("b", 0, 1):
				if value in true_values:
					value = True
				elif value in false_values:
					value = False
				else:
					raise Exception(f"ERROR: Unknown boolean value in config: '{file_path}' -> '[{section}]' -> '{option} = {value}'. Valid values are: {valid_boolean_values}.")
			elif option.startswith("i", 0, 1):
				value = int(value)
			elif option.startswith("f", 0, 1):
				value = float(value)
			elif option.startswith("s", 0, 1):
				if option.startswith(root_dir_key) or option.endswith(root_dir_key):
					if value.startswith(root_dir_value):
						value = root_path + value[len(root_dir_value):]
			#elif option.startswith("l", 0, 1):
			#	value = list(value)
			#elif option.startswith("t", 0, 1):
			#	value = tuple(value)
			#elif option.startswith("d", 0, 1):
			#	value = dict(value)
			#elif option.startswith("o", 0, 1):
			#	value = set(value)
			section_dict[option] = value
		config_dict[section] = section_dict
	if debug:
		print(f"Config ({file_path}):\n{config_dict}")
		for section in config_dict:
			print(f"\n'[{section}]'")
			for option in config_dict[section]:
				print(f"'{option}': {type(config_dict[section][option])} = '{config_dict[section][option]}'")
	return config_dict

def test() -> None:
	CONFIG_PATH = os_path.join(get_root_path(), "examples", "example_config.ini")
	try:
		config = read_config(CONFIG_PATH, True, True)
	except Exception as e:
		print(e)
		exit()

if __name__ == "__main__":
	test()
