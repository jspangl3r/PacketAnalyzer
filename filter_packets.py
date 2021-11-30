import sys
# Project 2
# filter_packets.py by Caleb Ghatt and Gang 


def filter(fileName) :
	print('called filter function in filter_packets.py')
	f=open(str(fileName), 'r')
	line=f.readline()
	fileName=fileName[:-4]
	# Opens and wipes previous versions of file
	open(fileName+"_filtered.txt", "w").close()
	while line:
		line=line.strip()
		# Only reads in lines with Echo Requests/Replies in packet header
		if "Echo" in line:
			
			print("No.     Time           Source                Destination           Protocol Length Info", file=open(fileName+"_filtered.txt", "a"))
			
			print(line, file=open(fileName+"_filtered.txt", "a"))
			line=f.readline().strip()

			# checks the next line
			if line=="":
				# While line isnt empty reads HEX code
				while(line!="\n"):
					print(str.rstrip(line), file=open(fileName+"_filtered.txt", "a"))
					line=f.readline()

			line=f.readline()
			# prints blank line between readings
			print("", file=open(fileName+"_filtered.txt", "a"))
		line=f.readline()
	f.close()

# Get User Text File
fileName=str(sys.argv[1])
filter(fileName)

