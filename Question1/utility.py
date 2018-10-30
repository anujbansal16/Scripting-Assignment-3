import pickle
import os
import setting
import setting
from classes import Product
from classes import Customer
from classes import Guest
from classes import Operations
from classes import Admin
from classes import Payment

#test by removing clear

F_ADMIN="admins.txt"
F_CUSTOMER="customers.txt"
F_PRODUCT="products.txt"
F_PAYMENT="payment.txt"
F_CART="cart.txt"
F_MYORDER="myorders.txt"

def clear():
	os.system("clear")

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

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

def getPaymentDetails(cid):
	paymentFile=open(F_PAYMENT,"rb")
	while True:
		try:
			payment=pickle.load(paymentFile)
		except EOFError:
			break
		else:
			if(payment.customerId==cid):
				return payment
	paymentFile.close()
	return None
	pass

def makePayment(customer):
	clear()
	payment=getPaymentDetails(customer.id)
	cart=customer.getCart()
	if cart:
		if payment:
			customer.makePayment(payment)
		else:
			print("-------Provide your card details------")
			print("Enter your card number")
			cno=raw_input()
			print("Enter your name (as appeared on card)")
			name=raw_input()
			print("Enter card type")
			cardType=raw_input()
			if not(cno and name and cardType):
				print("please enter valid information (all are mandatory )")
			else:
				payment=Payment(customer.id, name,cardType,cno)
				paymentFile=open(F_PAYMENT,"ab")
				pickle.dump(payment,paymentFile)
				paymentFile.close()
				customer.makePayment(payment)
	else:
		print("Please add products: Cart Empty")	
	printdash()

def authCustomer(id):
	return setting.customersList.get(id,None)

def loadProducts():
	productFile=open(F_PRODUCT,"ab")
	productFile.close()
	productFile=open(F_PRODUCT,"rb")
	while True:
		try:
			setting.productsList=pickle.load(productFile)
			print(setting.productsList)
		except EOFError:
			break
	productFile.close()

def loadCustomers():
	customerFile=open(F_CUSTOMER,"ab")
	customerFile.close()
	customerFile=open(F_CUSTOMER,"rb")
	while True:
		try:
			setting.customersList=pickle.load(customerFile)
			print(setting.customersList)
		except EOFError:
			break
	customerFile.close()

def loadCarts():
	cartFile=open(F_MYORDER,"ab")
	cartFile.close()
	cartFile=open(F_CART,"rb")
	while True:
		try:
			setting.cartsList=pickle.load(cartFile)
			print(setting.cartsList)
		except EOFError:
			break
	cartFile.close()

def loadMyOrders():
	myOrderFile=open(F_MYORDER,"ab")
	myOrderFile.close()
	myOrderFile=open(F_MYORDER,"rb")
	while True:
		try:
			setting.myOrdersList=pickle.load(myOrderFile)
			print(setting.myOrdersList)
		except EOFError:
			break
	myOrderFile.close()



def printdash():
	print("------------------------------")

def viewProducts(person):
	#polymorphism
	clear()
	print("--------------------------------ALL PRODUCTS--------------------------------")
	print("%-10s%-20s%-20s%-20s%-15s"%('ID','NAME','GROUP','SUBGROUP','PRICE'))
	person.viewProducts()
	printdash()

def searchProducts(customer):
	clear()
	print("Search Products(by name): "),
	search=raw_input()
	search=(search.strip()).lower()
	if not(search):
		print("Please enter some keywords")
		return False
	products=customer.searchProducts(search)
	if not(products):
		print("No products found with: "+search)
	else:
		print("---------------------------SEARCHED RESULTS for %s---------------------------"%search)
		print("%-10s%-20s%-20s%-20s%-15s"%('ID','NAME','GROUP','SUBGROUP','PRICE'))
		for prod in products:
			prod.printProduct()
	printdash()

def viewCart(customer):
	clear()
	cart=customer.getCart()
	if cart:
		cart.printCart()
		return True
	else:
		print("Your cart is empty")
		return False

def deleteFromCart(customer):
	clear()
	if not(viewCart(customer)):
		return False
	printdash()
	print("Enter the product ID of product you wanna delete")
	id=raw_input()
	if id.isdigit():
		product=customer.getProduct(int(id))
		if product:
			customer.deleteFromCart(product)
		else:
			print("No product found with id: "+id)
	else:
		print("Product id should be a number")

def addToCart(customer):
	clear()
	viewProducts(customer)
	print("Enter the product ID of product you wanna add to cart")
	id=raw_input()
	if id.isdigit():
		product=customer.getProduct(int(id))
		if product:
			customer.addToCart(product)
			print("Added to Cart Succesfully")
		else:
			print("No product found with id: "+id)
	else:
		print("Product id should be a number")
	printdash()

def myOrders(customer):
	clear()
	customer.myOrders()
	printdash()

def buyProducts(customer):
	clear()
	choice=10
	while choice!='5':
		clear()
		print("---------WElCOME "+(customer.name).upper()+"----------")
		print("---------BUYING PANEL----------")
		print(Operations.CustomerSub)
		printdash()
		print("Make a choice: "),
		choice=raw_input()
		try:
			if choice=='1':
				#ADD TO CART
				addToCart(customer)
				print("Press Enter to go back")
				raw_input()
			if choice=='2':
				#DELETE FROM CART
				deleteFromCart(customer)
				printdash()
				print("Press Enter to go back")
				raw_input()
			if choice=='3':
				#VIEW CART
				viewCart(customer)
				printdash()
				print("Press Enter to go back")
				raw_input()
			if choice=='4':
				#MAKE PAYMENT
				makePayment(customer)
				print("Press Enter to go back")
				raw_input()

		except Exception as e:
			print(e)
	pass
	

def addProduct(admin):
	clear()
	print("---------ADD PRODUCT---------")
	# viewProducts(admin)
	print("Enter Product Id")
	id=raw_input()
	print("Enter Product Name")
	name=raw_input()
	print("Enter Product Group")
	grp=raw_input()
	print("Enter Product SubGroup")
	sub=raw_input()
	print("Enter Product Price")
	price=raw_input()
	if not(id.isdigit() and isfloat(price) and name and grp and sub):
		print("please enter valid information (all are mandatory and id should be integer)")
		return None
	return Product(int(id),name,grp,sub,float(price))

def modifyProduct(admin):
	clear()
	print("--------------MODIFYING PRODUCT--------------")
	viewProducts(admin)
	print("Enter Product Id to be modified")
	previousid=raw_input()
	try:
		previousid=int(previousid)
	except Exception as e:
		print("Not valid product id")
		return None
	else:
		prod=setting.productsList.get(previousid,None)
		if not(prod):
			print("No product found with ID: "+str(previousid))
			return None
	
	print("Want to modify id? (Enter new value or press enter)")
	id=raw_input()
	try:
		if id:
			id=int(id)
		else:
			id=previousid			
	except Exception as e:
		print("Not valid product id")
		return None

	print("Want to modify product name? (Enter new value or press enter)")
	name=raw_input()
	name=name if name else prod.name

	print("Want to modify product Group? (Enter new value or press enter)")
	grp=raw_input()
	grp=grp if grp else prod.group

	print("Want to modify product SubGroup? (Enter new value or press enter)")
	sub=raw_input()
	sub=sub if sub else prod.subgroup

	print("Want to modify product Price? (Enter new value or press enter)")
	price=raw_input()
	if price:
		if isfloat(price):
			price=float(price)
		else:
			print("Not valid price value")
			return None
	else:
		price=prod.price
	return [Product(id,name,grp,sub,price),previousid]

def deleteProducts(admin):
	clear()
	print("--------------DELETING PRODUCT--------------")
	# viewProducts(admin)
	print("Enter Product Ids to delete")
	try:
		pids=[int(x) for x in raw_input().split()]
		if not(pids):
			print("id cannot be blank")
	except Exception as e:
		print("Please provide ids as integer")
		return None
	else:
		return pids

def adminOperations(admin):
	choice=10
	while choice!='7':
		clear()
		print("---------WElCOME "+(admin.name).upper()+"----------")
		print("---------ADMIN PANEL----------")
		print(Operations.Admin)
		printdash()
		print("Make a choice: "),
		choice=raw_input()
		try:
			if choice=='1':
				#VIEW PRODUCTS
				viewProducts(admin)
				print("Press Enter to go back")
				raw_input()
			if choice=='2':
				#ADD PRODUCT
				subChoice=10
				while subChoice!="quit":
					product=addProduct(admin)
					if product:
						admin.addProduct(product)
					print("Want to Add more? Press enter else \'quit\'")
					subChoice=raw_input()
				printdash()
			if choice=='3':
				#DELETE PRODUCT
				pids=deleteProducts(admin)
				if pids:
					admin.deleteProducts(pids)
				print("Press Enter to go back")
				raw_input()
			if choice=='4':
				#MODIFY PRODUCT
				listProd_ID=modifyProduct(admin)
				if listProd_ID:
					admin.modifyProduct(listProd_ID[0],listProd_ID[1])
				print("Press Enter to go back")
				raw_input()
			if choice=='15':
				clear()
				admin.viewAllCustomers()
				print("Press Enter to go back")
				raw_input()

		except Exception as e:
			print(e)
	else:
		print("You have logged out.(press enter to go to home)")

def customerOperations(customer):
	choice=10
	while choice!='5':
		clear()
		print("---------WElCOME "+(customer.name).upper()+"----------")
		print("---------CUSTOMER PANEL----------")
		print(Operations.Customer)
		printdash()
		print("Make a choice: "),
		choice=raw_input()
		try:
			if choice=='1':
				#VIEW PRODUCTS
				viewProducts(customer)
				print("Press Enter to go back")
				raw_input()
			if choice=='2':
				#buy PRODUCT
				buyProducts(customer)
			if choice=='3':
				#search PRODUCT
				searchProducts(customer)
				print("Press Enter to go back")
				raw_input()
			if choice=='4':
				#search PRODUCT
				myOrders(customer)
				print("Press Enter to go back")
				raw_input()

		except Exception as e:
			print(e)
	else:
		print("You have logged out.(press enter to go to home)")


def guestOperations(guest):
	choice=10
	while choice!='3':
		clear()
		print("---------WELCOME GUEST----------")
		print("---------GUEST PANEL----------")
		print(Operations.Guest)
		printdash()
		print("Make a choice: "),
		choice=raw_input()
		try:
			if choice=='1':
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
					printdash()
					print("Press Enter to go back")
					raw_input()
					continue
				asCustomer=Customer(id,name,add,phNo)
				if(guest.getRegistered(asCustomer)):					
					raw_input()
					#succesfully register now login
					break;
				printdash()
				print("Press Enter to go back")
				raw_input()
			if choice=='2':
				viewProducts(guest)
				print("Press Enter to go back")
				raw_input()
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

def persistCarts():
	cartFile=open(F_CART,"wb")
	try:
		pickle.dump(setting.cartsList,cartFile)
	except Exception as e:
		print(e)
	cartFile.close()	

def persistMyOrders():
	myOrderFile=open(F_MYORDER,"wb")
	try:
		pickle.dump(setting.myOrdersList,myOrderFile)
	except Exception as e:
		print(e)
	myOrderFile.close()	
	

def persist():
	# print(setting.productsList)
	# print(setting.customersList)
	# print(setting.cartsList)
	persistProducts()
	persistCustomers()
	persistCarts()
	persistMyOrders()
