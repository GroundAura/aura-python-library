#import json

def escape_json_string(string: str) -> str:
	escape_mapping: dict[str, str] = {
		"\\": "\\\\",
		"\"": "\\\"",
		"\b": "\\b",
		"\f": "\\f",
		"\n": "\\n",
		"\r": "\\r",
		"\t": "\\t"
	}
	formatted_string: str = ""
	for char in string:
		formatted_string += escape_mapping.get(char, char)
	return formatted_string

def test() -> None:
	raise NotImplementedError

if __name__ == "__main__":
	test()
