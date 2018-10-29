import os
import re
#for printing formatted output without newline
import sys
from string import maketrans  

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

def translateStr(intab, outtab, str):
	trantab = maketrans(intab, outtab)
	return str.translate(trantab)

def findTabs(tabs):
	reg=tabs[0]
	res=tabs[1]
	#########################################
	if reg=="[:lower:]":
		reg=""
		for i in range(26):
			reg=reg+chr(97+i)
	elif reg=="[:upper:]":
		reg=""
		for i in range(26):
			reg=reg+chr(65+i)
	elif reg=="[:digit:]":
		reg=""
		for i in range(10):
			reg=reg+chr(ord('0')+i)
	elif reg[0]=="[" and reg[len(reg)-1]=="]":
		before=""
		after=""
		beforeIndex=0
		afterIndex=len(reg)-1
		if "-" in reg:
			if reg.find("-")-1>=1:
				#before is a character
				before=reg[reg.find("-")-1]
				beforeIndex=reg.find("-")-1
			if reg.find("-")+1<len(reg)-1:
				after=reg[reg.find("-")+1];
				afterIndex=reg.find("-")+1
			if len(before)==0 or len(after)==0:
				reg=reg[1:len(reg)-1]
				# beforeIndex=0;
				# afterIndex=len(reg)-1;
			else:
				#[a-e]=>abcde
				regtemp=""
				while ord(before)!=ord(after):
					regtemp=regtemp+before;
					before=chr(ord(before)+1)
				regtemp=regtemp+after
				if beforeIndex!=0 and afterIndex!=len(reg)-1:
					regtemp=reg[1:beforeIndex]+regtemp
					regtemp=regtemp+reg[afterIndex+1:len(reg)-1]
				reg=regtemp
		else:
			#if not having - [ae]=>ae
			reg=reg[1:len(reg)-1]
	##################################
	if res=="[:lower:]":
		res=""
		for i in range(26):
			res=res+chr(97+i)
	elif res=="[:upper:]":
		res=""
		for i in range(26):
			res=res+chr(65+i)
	elif res=="[:digit:]":
		res=""
		for i in range(10):
			res=res+chr(ord('0')+i)
	elif res[0]=="[" and res[len(res)-1]=="]":
		before=""
		after=""
		beforeIndex=0
		afterIndex=len(res)-1
		if "-" in res:
			if res.find("-")-1>=1:
				#before is a character
				before=res[res.find("-")-1]
				beforeIndex=res.find("-")-1
			if res.find("-")+1<len(res)-1:
				after=res[res.find("-")+1];
				afterIndex=res.find("-")+1
			if len(before)==0 or len(after)==0:
				res=res[1:len(res)-1]
				# beforeIndex=0;
				# afterIndex=len(res)-1;
			else:
				#[a-e]=>abcde
				restemp=""
				while ord(before)!=ord(after):
					restemp=restemp+before;
					before=chr(ord(before)+1)
				restemp=restemp+after
				if beforeIndex!=0 and afterIndex!=len(res)-1:
					restemp=res[1:beforeIndex]+restemp
					restemp=restemp+res[afterIndex+1:len(res)-1]
				res=restemp
		else:
			#if not having - [ae]=>ae
			res=res[1:len(res)-1]
	
	print(reg)
	print(res)
	return [reg,res]
	
def trF(keywords, length):
	f=open(keywords[length-1], "r")
	options=keywords[1]
	if options=="-d":
		reg=keywords[2]
		reg=re.compile(reg)
		for line in f:
			sys.stdout.write(reg.sub('',line))
		return True
	else:
		reg=options
		res=keywords[2]
		tabs=[reg,res]
		tabs=findTabs(tabs)
		if len(tabs[0])!=len(tabs[1]):
			return False;
		else:
			for line in f:
				sys.stdout.write(translateStr(tabs[0],tabs[1],line))
		return True


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

def grepF(keywords, length):
	if(length==3):
		f = open(keywords[2], "r")
		searchWord=keywords[1]
		option=None
	elif keywords[1]=="-i":
		f = open(keywords[3], "r")
		option=keywords[1]
		searchWord=(keywords[2])
	else:
		return 1
	if option is not None:
		pattern=re.compile(searchWord,re.IGNORECASE)
	else:
		pattern=re.compile(searchWord)
	for line in f:
		if pattern.search(line):
			sys.stdout.write(line)


def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)]
    if len(where)<n:
    	return string
    where=where[n-1]
    before = string[:where]
    after = string[where:]
    after = re.sub(sub, wanted,after,1)
    newString = before + after
    return newString

def sedF(keywords,length):
	f = open(keywords[length-1], "r")
	sedCmd=keywords[length-2]
	sedCmd=sedCmd.split("/")
	if len(sedCmd)==4:
		if sedCmd[0]=="s":
			patt=sedCmd[1]
			res=sedCmd[2]
			options=sedCmd[3]
			reg=re.compile(patt)
			if len(options)>0:
				if "i" in options:
					reg=re.compile(patt, re.IGNORECASE)
			for line in f:
				replaced=line
				if len(options)>0:
					if "g" in options:
						replaced=reg.sub(res, line)
					else:
						if options[0].isdigit():
							replaced=replacenth(line,patt,res,int(options[0]))
						else:
							replaced=reg.sub(res,line,1)		
				else:
					replaced=reg.sub(res,line,1)
				sys.stdout.write(replaced)
		else:
			print("Erro: Not valid command")
	else:
		print("Error: Invalid Command")



def execCommand(keywords):
	if(len(keywords)>1 and keywords[0]=="touch"):
		# print("Toucin a file")
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

	elif((len(keywords)==3 or len(keywords)==4)  and keywords[0]=="grep"):
		try:
		 	grepF(keywords,len(keywords))
		except Exception as e:
			print(e)
		return 1	

	elif((len(keywords)==4)  and keywords[0]=="tr"):
		try:
		 	isSuccess=trF(keywords,len(keywords))
		 	if not(isSuccess):
		 		print("Error: Problem in arguments")
		except Exception as e:
			print(e)
		return 1	

	elif((len(keywords)==3)  and keywords[0]=="sed"):
		try:
		 	sedF(keywords,len(keywords))
		except Exception as e:
			raise e
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
		break;