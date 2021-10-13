import sys
'''
@Author:Peter
This is a program which can speed up our IR procedures 
by extracting common suspicous file path from MFTScan_C.txt
'''
sus_path = [
	'c:\\Users\\Public\\'.casefold(), 
	'c:\\Temp\\'.casefold(), 
	'c:\\Windows\\Temp\\'.casefold(), 
	'c:\\PefLogs\\'.casefold(), 
	'c:\\ProgramData\\'.casefold()
]

def output_common_suspicious(temp_output):
	with open('Common_suspicious.txt', 'w') as f:
		for path in temp_output:
			f.write("%s\n" % path)
	return 

def extract_and_output(arr_path):
	res = []
	if arr_path[0] == 'all': # Common malicious paths, to be continued...
		with open('MFTScan_C.txt') as MFTScan:
			for line in MFTScan:
				for item in sus_path:
					if item in str(line).casefold():
						res.append(line)
	else:
		print("Find specific path!") # What if running python string_parser.py "certain directory"
		for index in range(0, len(arr_path)):
			for line in Lines:
				if arr_path[index].casefold() in line.casefold():
					res.append(line)
				else:
					pass
	return res

if __name__ == '__main__':
	print("Starting to read file path from MFTScan_C.txt....")
	arr_path = []
	if len(sys.argv) < 2: # Extract each common suspicious path from MFTScan_C.txt by default.
		arr_path.append('all') # Customerize flag
	elif len(sys.argv) == 2: # Extract specific file path from MFTScan_C.txt
		arr_path.append(sys.argv[1])
	else: # Extract multiple file paths from MFTScan_C.txt
		for index in range(0,len(sys.argv)):
			arr_path.append(sys.argv[index])
	temp_output = extract_and_output(arr_path)
	if not temp_output:
		print("MFTScan_C.txt might be empty or still in progress!\nTry again later.")
		temp_output.append('None') # Default setting 'None'
	else:
		print("Generating common suspicious file path...")
	output_common_suspicious(temp_output) # Generate Common_malicious.txt
	print("Finish !\nPress any key to end the program.")
	input()	