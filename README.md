# aurapy - Aura's Python Function Library

This is mostly for me as a way to reuse some functions I use a lot in my projects to reduce manual workload, and as a learning exercise, but feel free to use these for your own projects.

## Modules and Functions

### `commandline`

```py
run_command(
  command: str
) -> None
```

### `config`

```py
read_config(
  file_path: str,
  preserve_keys_case: bool = False,
  debug: bool = False,
  true_values: tuple[str] | str = ("TRUE", "True", "true", "T", "t"),
  false_values: tuple[str] | str = ("FALSE", "False", "false", "F", "f"),
  root_dir_value: str = "[ROOT]"
) -> dict[str, dict[str]]
```

### `filemanager`

```py
get_root_path() -> str
```

### `json`

```py
escape_json_string(
  string: str
) -> str
```

### `skyrim`

```py
is_bethesda_plugin(
  file_path: str
) -> bool
```

### `xml`

```py
escape_xml_string(
  string: str, fomod: bool = False
) -> str
```
