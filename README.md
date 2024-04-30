# aura.py | Aura's Python Function Library

aura.py is mostly a way for me to reuse some functions I use a lot in my projects, and a learning exercise. Feel free to use these for your own projects if you want though (see license).

## Modules & Functions

<!-- ### `aura_cmd.py`

```py
run_command(
  command: str
) -> None
``` -->

### aura_config.py

`read_config()` reads a configuration file in INI format and returns it as a dictionary, with data types formatted according to the first character of keys (`b`: boolean, `i`: integer, `f`: float, `s`: string). It allows you to use a variable value to start file paths at the current working directory; option keys must begin or end with specified strings. It also has options to preserve/ignore the case of keys, enable debug logging, and specify custom valid values for boolean and current working directory variables.

```py
read_config(
  file_path: str,
  preserve_keys_case: bool = False,
  debug: bool = False,
  root_dir_key: tuple[str] | str = ("PATH", "Path", "path", "sPATH", "sPath", "spath"),
  root_dir_value: str = "[ROOT]",
  true_values: tuple[str] | str = ("TRUE", "True", "true", "T", "t", "1"),
  false_values: tuple[str] | str = ("FALSE", "False", "false", "F", "f", "0")
) -> dict[str, dict[str]]
```

### aura_files.py

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

`move_files()` moves a file or a list/tuple of files to a specified folder. If moving a single file you can specify a file name, allowing renaming, however this is not supported with multiple files.

```py
move_files(
  source_path: str | list[str] | tuple[str],
  destination_path: str,
  force_overwrite: bool = False
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

`is_bethesda_plugin()` checks if a path points to a file that ends in `.esp`, `.esm`, or `.esl`.

```py
is_bethesda_plugin(
  file_path: str
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
