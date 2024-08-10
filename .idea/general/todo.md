# TODO

## Incomplete

- [ ] add support for specifying file names for multiple files in `move_files()`
- [ ] add support for nested strings to `escape_json_string()` and `escape_xml_string()`
- [ ] implement `format_formid()`
- [ ] check fomod escapes for `escape_xml_string()`
- [ ] add example config `example.ini` for `read_config()`
- [ ] fix lists, tuples, and sets in `read_config()`
- [ ] fix dictionaries in `read_config()`
- [ ] add support for case insensitive strings for options in `read_config()`
- [ ] add suppport for multiple values for `root_dir_value` in `read_config()`
- [ ] implement `replace_text()`
- [ ] implement `unique()`, `unique_sorted()`, `unique_sorted_tuple()`, (_lower)
- [ ] add ability to check recursive types for list/tuple/set/dict in `get_type()`

## Complete

- [x] change module names to not conflict with existing modules
- [x] implement `run_command()`
- [x] implement `move_folders()`
- [x] implement `rename_file()`
- [x] implement `rename_folder()`
- [x] fix root directory in `read_config()`
- [x] implement `str_to_dict()`
- [x] implement `str_to_tuple()`
- [x] implement `str_to_list()`
- [x] implement `str_to_set()`
