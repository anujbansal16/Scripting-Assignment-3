import setting
import setting
class Operations(object):
	"""docstring for Operations"""
	Guest="1. Register\n2. View Products\n3. Go to Home"	
	Customer="1. View Products\n2. Buy Products\n3. Search Product(by name)\n4. Logout"	
	CustomerSub="1. Add to Cart\n2. Delete from Cart\n3. Make Payment\n4. Go Back"	
	Admin="1. View Products\n2. Add Products\n3. Delete Products\n4. Modify Products\n5. Make Shipment\n6. Confirm Delivery\n7. Logout"	
		

class Admin(object):
	"""docstring for Admin"""
	def __init__(self,id,name):
		self.id=id
		self.name=name
	def addProduct(self,product):
		if product.id in setting.productsList:
			print("Cannot add product: "+str(product.id)+" already exist")
		else:
			setting.productsList[product.id]=product
			print("Product with id "+str(product.id)+" added successfully")		
	def viewAllCustomers(self):
		for key in setting.customersList:
			setting.customersList[key].printCustomer()
	def viewProducts(self):
		for key in setting.productsList:
			setting.productsList[key].printProduct()
	def deleteProducts(self,pids):
		for key in pids:
			if setting.productsList.pop(key, None):
				print("Product with ID: "+str(key)+" deleted Successfully")
			else:
				print("Product not found with ID: "+str(key))
	def modifyProduct(self,product,previousId):
			setting.productsList.pop(previousId, None)
			setting.productsList[product.id]=product
			# print(setting.productsList)
			# print(setting.productsList[product.id])

class Product(object):
	"""docstring for Product"""
	def __init__(self, id,name,group,subgroup,price):
		self.id=id
		self.name=name
		self.group=group
		self.subgroup=subgroup
		self.price=price
	def printProduct(self):
		print("%d\t%s\t%s\t%s\t%f"%(self.id,self.name,self.group,self.subgroup,self.price))

class Customer(object):
	"""docstring for Customer"""
	def __init__(self,id,name,address,phNo):
		self.id = id
		self.name = name
		self.address = address
		self.phNo = phNo

	def printCustomer(self):
		print("%s\t%s\t%s\t%s"%(self.id,self.name,self.address,self.phNo))

	def viewProducts(self):
		for key in setting.productsList:
			setting.productsList[key].printProduct()

	def searchProducts(self,name):
		searchedProList=list()
		for key in setting.productsList:
			if name in setting.productsList[key].name:
				searchedProList.append(setting.productsList[key])
		return searchedProList
		

class Guest(object):
	"""docstring for Guest"""
	gNo=0
	def __init__(self):
		Guest.gNo+=1
	def viewProducts():
		pass
	def getRegistered(self,customer):

		if customer.id in setting.customersList:
			print("Cannot Register: This userID already taken")
			isSuccess=False
		else:
			setting.customersList[customer.id]=customer
			print("Successfully Registered as a Customer. Please Login")		
			isSuccess=True
		return isSuccess

	def viewProducts(self):
		for key in setting.productsList:
			setting.productsList[key].printProduct()
		
class Payment(object):
	"""docstring for Payment"""
	def __init__(self,customerId,name,cardType,cardNo):		
		self.customerId=customerId
		self.name=name
		self.cardType=cardType
		self.cardNo=cardNo
	def pay():
		print("Please Wait...")
		print("%s\t%s\t%s\t%s"%(self.customerId,self.name,self.cardType,self.cardNo))
		print("Payment Done Successfully")		
		
		