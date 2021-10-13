# String parser
This is a program which can speed up our IR procedures by extracting common suspicious file path from MFTScan_C.txt
# Requirement
Install Python from official website on latest Windows or Linux operating system (e.g Windows 10)
# Usage
Place this code with a text file which contains MFT file path.
`python string_parser.py`
# Flexibility
You can also use this code to parse specific strings, all you have to do is replacing the searching list inside the code to yours.
```python
sus_path = [
	'c:\\Users\\Public\\'.casefold(), 
	'c:\\Temp\\'.casefold(), 
	'c:\\Windows\\Temp\\'.casefold(), 
	'c:\\PefLogs\\'.casefold(), 
	'c:\\ProgramData\\'.casefold()
]
with open('MFTScan_C.txt') as MFTScan:
	for line in MFTScan:
		for item in sus_path:
			if item in str(line).casefold():
				res.append(line)
```
