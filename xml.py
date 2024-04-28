#import os
#import xml

def escape_xml_string(string: str, fomod: bool = False) -> str:
	if fomod:
		escape_mapping: dict[str, str] = {
			"&": "&amp;",
			"<": "&lt;",
			">": "&gt;",
			"\"": "&quot;",
			"'": "&apos;"
		}
	else:
		escape_mapping: dict[str, str] = {
			"&": "&amp;",
			"<": "&lt;",
			">": "&gt;",
			"\"": "&quot;",
			"'": "&apos;"
		}
	formatted_string: str = ""
	for char in string:
		formatted_string += escape_mapping.get(char, char)
	return formatted_string

def test() -> None:
	raise NotImplementedError

if __name__ == "__main__":
	test()
