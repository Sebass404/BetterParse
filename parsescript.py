#!/usr/bin/python
# encoding: UTF-8

'''
	BetterParse
	
	Author: Sebastian 'Sebass' Ausitn
	Email: pensec31337@gmail.com
'''
import re
import os
import sys, traceback

def main():
	try:
		if (sys.argv[1] == None):
			filePath = raw_input("Enter the path to Bettercap output log: ")
		else:
			filePath  = sys.argv[1]
			if not (os.path.isfile(filePath)):
				print "File does not exists!"
				sys.exit(0)
			string = open (filePath).read()
			newStr = re.sub('[^a-zA-Z0-9.-[]\n\.]', ' ', string)
			delete_list = ["bettercap", '^', ";" , " _          _   _" , "|" ,"\ " , '`' , "1.5.6"]
			fin = filePath
			fileExists = os.path.isfile("Bettercap Cleaned.txt")
			if (fileExists):
				print "File already exist!"
				print "Outputting to Bettercap Cleaned(1).txt"
				fout = open("Bettercap Cleaned(1).txt", 'w')
				fout.write(newStr)
				for line in fin:
					for word in delete_list:
						line = line.replace(word, "")
					fout.write(line)
				fout.close()
			else: 
				print "Outputting to Bettercap Cleaned..."
				foutO = open("Bettercap Cleaned.txt" , 'w')
				foutO.write(newStr)
				for line in fin:
					for word in delete_list:
						line = line.replace(word, "")
					foutO.write(line)
				foutO.close()
	except KeyboardInterrupt:
			print "Shutdown requested...exiting"
	except Exception:
			print traceback.print_exc(file=sys.stdout)
			sys.exit(0)
if __name__ == "__main__":
	main()
