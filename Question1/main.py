from classes import Product
from classes import Customer
from classes import Guest
from classes import Operations
from classes import Admin
import pickle
import utility

def init():
	utility.createAdmin(1,"anuj")
	utility.loadProducts()
	utility.loadCustomers()
	utility.loadCarts()	

def login(role):
	print("Please provide your id")
	id=raw_input()
	if role=="admin":
		try:
			id=int(id)
		except Exception as e:
			print("ID should be integer")
		return utility.authAdmin(id)
	elif role=="customer":
		return utility.authCustomer(id)

def guestLogin():
	utility.clear()
	print("------------------------------WELCOME Guest----------------------------")
	guest=Guest()
	utility.guestOperations(guest)

def customerLogin():
	print("customer login")
	customer=login("customer")
	if customer:
		#success logged in perform operations		
		print("------------------------------WELCOME "+ (customer.name).upper() +"----------------------------")
		utility.customerOperations(customer)
	else:
		print("Invalid Id")

def adminLogin():
	admin=login("admin")
	if admin:
		utility.clear()
		print("------------------------------WELCOME ADMIN "+ (admin.name).upper() +"----------------------------")
		utility.adminOperations(admin)
	else:
		print("Invalid Id")

def home():
	choice=10
	utility.clear()
	while choice!='4':
		print("----------------------------WELCOME TO SUPERMARKET--------------------------")
		print("")
		print("Tell us who you are? (Press the number)")
		print("\t1.Guest?")
		print("\t2.Customer?")
		print("\t3.Admin?")
		print("\t4.Exit?")
		choice=raw_input()
		if choice=='1':
			guestLogin()
		elif choice=='2':
			customerLogin()
		elif choice=='3':
			adminLogin()
		# utility.clear()
	else:
		utility.clear()
		utility.persist()
		print("Thanks for shopping..")

init()
home()