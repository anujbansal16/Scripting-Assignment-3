from classes import Product
from classes import Customer
from classes import Guest
from classes import Operations
import os
import pickle
import utility
def clear():
	os.system("clear")

def login(role):
	print("Please provide your id")
	id=input()
	if role=="admin":
		return utility.authAdmin(id)
	elif role=="customer":
		return authCustomer(id)

def guestLogin():
	print(Operations.Guest)

def customerLogin():
	print("customer login")
	customer=login("customer")
	if customer:
		#success logged in perform operations		
		print(Operations.Customer)
	else:
		print("Invalid Id")

def adminLogin():
	admin=login("admin")
	if admin:
		clear()
		#success logged in perform operations
		print("------------------------------WELCOME Admin----------------------------")
		print(Operations.Admin)
	else:
		print("Invalid Id")

def home():
	choice=10
	clear()
	while choice!=4:
		print("------------------------------WELCOME TO SUPERMARKET----------------------------")
		print("")
		print("Tell us who you are? (Press the number)")
		print("\t1.Guest?")
		print("\t2.Customer?")
		print("\t3.Admin?")
		print("\t4.Exit?")
		choice=input()
		if choice==1:
			guestLogin()
		elif choice==2:
			CustomerLogin()
		elif choice==3:
			adminLogin()
	else:
		print("Thanks for shopping..")

utility.createAdmin(1,"anuj")
home()




# p1=Product(1,"netle","a","a1")
# p1.printProduct()
# c1=Customer(1,"anuj","indore","123")
# c2=Customer(2,"anuj1","bhopal","188")
# f=open("customers.txt","ab")
# pickle.dump(c1,f)
# pickle.dump(c2,f)
# f.close()
# f=open("customers.txt","rb")
# content=pickle.load(f)
# print(content)
# content.printCustomer()
# content=pickle.load(f)
# print(content)	
# content.printCustomer()
# f.close()
