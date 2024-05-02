# aura.py | Aura's Python Function Library

aura.py is mostly a way for me to reuse some functions I use a lot in my projects, and a learning exercise. Feel free to use these for your own projects if you want though (see license).

## Modules & Functions

### `aura_cmd.py`

`run_command()` runs a command line command. Options to use shell and print output.

```py
run_command(
  command: str | list[str],
  print_output: bool = False,
  use_shell: bool = False
) -> None
```

### aura_config.py

`read_config()` reads a configuration file in INI format and returns it as a dictionary, with data types formatted according to the first character of keys (`b`: boolean, `d`: dictionary, `f`: float, `i`: integer, `l`: list, `o`: set `s`: string, `t`: tuple). It allows you to use a variable value to start file paths at the current working directory; option keys must begin or end with specified strings. It also has options to preserve/ignore the case of keys, enable debug logging, and specify custom values for boolean and current working directory variables.

```py
read_config(
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
) -> dict[str, dict[str]]
```

### aura_files.py

`copy_file()` copies a file from one path to another. You can optionally forcibly copy all possible metadata and overwrite an existing file.

```py
copy_file(
  source_path: str,
  destination_path: str,
  force_metadata: bool = False,
  force_overwrite: bool = False
) -> None
```

`copy_folder()` copies a directory from one path to another. Optionally, you may forcibly copy all possible metadata and overwrite an existing directory.

```py
copy_folder(
  source_path: str,
  destination_path: str,
  force_metadata: bool = True,
  force_overwrite: bool = False
) -> None
```

<!-- `copy_from_path()` copies a file or directory from one path to another. Optionally, you may forcibly copy all possible metadata, overwrite an existing directory, and specify if you're copying a file or directory.

```py
copy_from_path(
  source_path: str,
  destination_path: str,
  force_metadata: bool = True,
  force_overwrite: bool = False,
  type: str | None = None
) -> None
``` -->

`delete_file()` deletes a file.

```py
delete_file(
  file_path: str | tuple[str]
) -> None
```

`delete_folder()` deletes a directory.

```py
delete_folder(
  file_path: str | tuple[str]
) -> None
```

<!-- `delete_from_path()` deletes a file or directory.

```py
delete_from_path(
  file_path: str
) -> None
``` -->

`get_base_path()` gets only the directory elements from a path to a file. Eg: `c:\example\folders`

```py
get_base_path(
  file_path: str
) -> str
```

`get_file_name()` gets only the file element from a path. Includes the extension by default, but you can disable this. Eg: `file.txt`, `file`

```py
get_file_name(
  file_path: str
  include_extension: bool = True
) -> str
```

`get_file_extension()` gets only the file extension from a path to a file. Includes the `.` by default, but you can disable this. Eg: `.txt`, `txt`

```py
get_file_extension(
  file_path: str
  include_dot: bool = True
) -> str
```

`get_root_path()` gets the current working directory path.

```py
get_root_path() -> str
```

`has_extension()` checks if a path or string ends with an extension or one of a list/tuple of extensions.

```py
has_extension(
  file_path: str,
  extensions: str | list[str] | tuple[str]
) -> bool
```

`is_file()` checks if a file exists at a path.

```py
is_file(
  file_path: str
) -> bool
```

`is_file_with_extension()` checks in a file exists at a path and ends with an extension or one of a list/tuple of extensions.

```py
is_file_with_extension(
  file_path: str,
  extensions: str | list[str] | tuple[str]
) -> bool
```

`is_folder()` checks if a folder exists at a path.

```py
is_folder(
  file_path: str
) -> bool
```

`move_files()` moves a single file or a list/tuple of files into a specified folder. If moving a single file you can specify a file name, allowing renaming, however this is not supported with multiple files.

```py
move_files(
  source_path: str | list[str] | tuple[str],
  destination_path: str,
  force_overwrite: bool = False
) -> None
```

`move_folders()` moves a single folder or a list/tuple of folders into a specified folder.

```py
move_folders(
  source_path: str | list[str] | tuple[str],
  destination_path: str
) -> None
```

`rename_file()` renames a single file to a new name, including extension. Optionally, you may specify a full file path to move the file as well.

```py
rename_file(
  file_path: str,
  new_name: str
) -> None
```

`rename_folder()` renames a single folder to a new name. Optionally, you may specify a full file path to move the folder as well.

```py
rename_folder(
  file_path: str,
  new_name: str
) -> None
```

### aura_json.py

`escape_json_string()` replaces common dangerous characters in a string with their json-escaped equivalents, allowing them to be used in json files.

```py
escape_json_string(
  string: str
) -> str
```

### aura_skyrim.py

`is_bethesda_plugin()` checks if a string ends in `.esp`, `.esm`, or `.esl`. By default it also checks if the string is a path to a file.

```py
is_bethesda_plugin(
  file_path: str,
  check_if_file: bool = True
) -> bool
```

### aura_type.py

`get_type()` gets the type of some data and returns it as a string.

```py
get_type(
  data: any
) -> str
```

`str_to_bool()` turns a string into a boolean. Uses a list of values to consider as true/false that you can optionally override.

```py
def str_to_bool(
  string: str,
  case_sensitive: bool = False,
  true_values: list[str] | tuple[str] | str = ("TRUE", "True", "true", "T", "t", "1"),
  false_values: list[str] | tuple[str] | str = ("FALSE", "False", "false", "F", "f", "0")
) -> bool
```

`str_to_dict()` turns a string into a dictionary.

```py
def str_to_dict(
  string: str
) -> bool
```

`str_to_float()` turns a string into a float.

```py
def str_to_float(
  string: str
) -> bool
```

`str_to_int()` turns a string into a integer.

```py
def str_to_int(
  string: str
) -> bool
```

`str_to_list()` turns a string into a list.

```py
def str_to_list(
  string: str
) -> bool
```

`str_to_set()` turns a string into a set.

```py
def str_to_set(
  string: str
) -> bool
```

`str_to_tuple()` turns a string into a tuple.

```py
def str_to_tuple(
  string: str
) -> bool
```

### aura_xml.py

`escape_xml_string()` replaces common dangerous characters in a string with their xml-escaped equivalents, allowing them to be used in xml files.

```py
escape_xml_string(
  string: str, fomod: bool = False
) -> str
```

## License

[Clear BSD](https://github.com/GroundAura/aurapy/blob/main/LICENSE.txt)
