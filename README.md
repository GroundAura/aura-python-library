# Aura's Python Function Library | aurapy

This is mostly for me as a way to reuse some functions I use a lot in my projects to reduce manual workload, and as a learning exercise, but feel free to use these for your own projects.

## Modules & Functions

<!-- ### `commandline`

```py
run_command(
  command: str
) -> None
``` -->

### `config.py`

`read_config()` reads a configuration file in INI format and returns it as a dictionary, with data types formatted according to the first character of keys (`b`: boolean, `i`: integer, `f`: float, `s`: string, `l`: list, `t`: tuple, `d`: dictionary, `o`: set). It allows you to use a variable value to start file paths at the current working directory. It also has options to preserve/ignore the case of keys, enable debug logging, and specify custom valid values for boolean and current working directory variables.

```py
read_config(
  file_path: str,
  preserve_keys_case: bool = False,
  debug: bool = False,
  true_values: tuple[str] | str = ("TRUE", "True", "true", "T", "t", "1"),
  false_values: tuple[str] | str = ("FALSE", "False", "false", "F", "f", "0"),
  root_dir_value: str = "[ROOT]"
) -> dict[str, dict[str]]
```

### `filemanager.py`

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

### `json.py`

`escape_json_string()` replaces common dangerous characters in a string with their json-escaped equivalents, allowing them to be used in json files.

```py
escape_json_string(
  string: str
) -> str
```

### `skyrim.py`

`is_bethesda_plugin()` checks if a path points to a file that ends in `.esp`, `.esm`, or `.esl`.

```py
is_bethesda_plugin(
  file_path: str
) -> bool
```

### `xml.py`

`escape_xml_string()` replaces common dangerous characters in a string with their xml-escaped equivalents, allowing them to be used in xml files.

```py
escape_xml_string(
  string: str, fomod: bool = False
) -> str
```

## License

[Clear BSD](https://github.com/GroundAura/aurapy/blob/main/LICENSE.txt)
