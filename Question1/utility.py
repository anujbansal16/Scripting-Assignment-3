import pickle
import os
import setting
import setting
from classes import Product
from classes import Customer
from classes import Guest
from classes import Operations
from classes import Admin

F_ADMIN="admins.txt"
F_CUSTOMER="customers.txt"
F_PRODUCT="products.txt"

def clear():
	os.system("clear")

def createAdmin(id,name):
	admin=Admin(id,name)
	adminFile=open(F_ADMIN,"wb")
	pickle.dump(admin,adminFile)
	adminFile.close()

def authAdmin(id):
	adminFile=open(F_ADMIN,"rb")
	while True:
		try:
			admin=pickle.load(adminFile)
		except EOFError:
			break
		else:
			if(admin.id==id):
				return admin

	adminFile.close()
	return None

def authCustomer(id):
	customerFile=open(F_CUSTOMER,"rb")
	while True:
		try:
			customer=pickle.load(customerFile)
		except EOFError:
			break
		else:
			if(customer.id==id):
				return customer
	customerFile.close()
	return None

def loadProducts():
	productFile=open(F_PRODUCT,"rb")
	while True:
		try:
			setting.productsList=pickle.load(productFile)
			print(setting.productsList)
		except EOFError:
			break
	productFile.close()

def loadCustomers():
	customerFile=open(F_CUSTOMER,"rb")
	while True:
		try:
			setting.customersList=pickle.load(customerFile)
			print(setting.customersList)
		except EOFError:
			break
	customerFile.close()


def adminOperations(admin):
	choice=10
	while choice!=7:
		print(Operations.Admin)
		choice=input()
		try:
			if choice==2:
				clear()
				print("---------ADD PRODUCT---------")
				print("Enter Product Id")
				id=raw_input()
				print("Enter Product Name")
				name=raw_input()
				print("Enter Product Group")
				grp=raw_input()
				print("Enter Product SubGroup")
				sub=raw_input()
				if not(id.isdigit() and name and grp and sub):
					print("please enter all information (id should be integer)")
					continue
				product=Product(id,name,grp,sub)
				admin.addProduct(product)
		except Exception as e:
			print(e)

def guestOperations(guest):
	choice=10
	while choice!=3:
		print(Operations.Guest)
		choice=input()
		try:
			if choice==1:
				clear()
				print("------REGISTER-------")
				print("Enter userId")
				id=raw_input()
				print("Enter your Name")
				name=raw_input()
				print("Enter your Address")
				add=raw_input()
				print("Enter your phoneno")
				phNo=raw_input()
				if not(id and name and add and phNo):
					print("please enter all information")
					continue
				asCustomer=Customer(id,name,add,phNo)
				if(guest.getRegistered(asCustomer)):
					#succesfully register now login
					break;
		except Exception as e:
			print(e)


def persistCustomers():
	customerFile=open(F_CUSTOMER,"wb")
	try:
		pickle.dump(setting.customersList,customerFile)
	except Exception as e:
		print(e)
	customerFile.close()	

def persistProducts():
	productFile=open(F_PRODUCT,"wb")
	try:
		pickle.dump(setting.productsList,productFile)
	except Exception as e:
		print(e)
	productFile.close()	

def persist():
	print(setting.productsList)
	print(setting.customersList)
	if setting.productsList:
		persistProducts()
	if setting.customersList:
		persistCustomers()
