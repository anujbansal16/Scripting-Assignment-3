import os
#for printing formatted output without newline
import sys

def pwd():
	return os.getcwd()

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)   
    return listOfFile

def printList(mylist):
	for it in mylist:		
		print("\t"+it)

def headF(keywords,length):
	#default read 10 lines
	numLineORChar=10
	# count=0
	f=0
	if(length==2):
		f=open(keywords[1], "r")		
	else:
		option=keywords[1]
		numLineORChar=int(keywords[2])
		if option=="-n":
			f=open(keywords[3], "r")
		elif option=="-c":
			f=open(keywords[3], "r")
			print(f.read(numLineORChar))
			return 1
		else:
			return 1
	for x in range(numLineORChar):
		sys.stdout.write(f.readline())
	return 1

def tailF(keywords,length):
	#default read 10 lines
	numLineORChar=10
	f=0
	if(length==2):
		f=open(keywords[1], "r")
	else:
		option=keywords[1]
		numLineORChar=int(keywords[2])
		if option=="-n":
			f=open(keywords[3], "r")
		elif option=="-c":
			print("hell")
			f=open(keywords[3], "rb")		
			f.seek(-numLineORChar,2);
			print(f.read(numLineORChar))	
			return 1
		else:
			return 1
	lines=f.readlines();
	totalLines=len(lines);
	count=0
	for x in lines:
		if count<totalLines-numLineORChar:
			count+=1;
			continue
		sys.stdout.write(x)
		count+=1;
	return 1

def execCommand(keywords):
	if(len(keywords)>1 and keywords[0]=="touch"):
		print("Toucin a file")
		try:
			f= open(keywords[1],"w+")
			f.close();
		except Exception as e:
			raise e
		return 1;
	elif(keywords[0]=="ls"):
		try:
			if(len(keywords)==1):
				printList(getListOfFiles(os.getcwd()));
			else:
				printList(getListOfFiles(keywords[1]))
		except Exception as e:
			print("Error: No such directory exists : "+"'"+keywords[1]+"'")
		return 1
	elif(keywords[0]=="pwd"):
		try:
			print(pwd())
		except Exception as e:
			print(e)
		return 1
	elif(len(keywords)>1 and keywords[0]=="cd"):
		try:
		 	os.chdir(keywords[1])
		except Exception as e:
			print("Error: No such directory exists : "+"'"+keywords[1]+"'")
		return 1	
	
	elif(	(len(keywords)==2 or len(keywords)==4)  and keywords[0]=="head"):
		try:
		 	headF(keywords,len(keywords))
		except Exception as e:
			print(e)
		return 1	

	elif(	(len(keywords)==2 or len(keywords)==4)  and keywords[0]=="tail"):
		try:
		 	tailF(keywords,len(keywords))
		except Exception as e:
			print(e)
		return 1	
	
	elif(keywords[0]=="exit"):
		return 0
	else:
		print("Invalid command / arguments mismatched")
		return 1

def main():
	inp=raw_input()
	inp=inp.strip();
	keywords=inp.split(" ")
	return execCommand(keywords)

os.system('clear')
while 1==1:
	print("Pyshell: "+pwd())
	if(not(main())):
		break