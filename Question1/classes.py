import setting
import setting
class Operations(object):
	"""docstring for Operations"""
	Guest="1. Register\n2. View Products\n3. Go to Home"	
	Customer="1. Buy Products\n2. View Products\n3. Make Payment\n4. Add to Cart\n5. Delete from Cart\n6. Logout"	
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

class Product(object):
	"""docstring for Product"""
	def __init__(self, id,name,group,subgroup):
		self.id=id
		self.name=name
		self.group=group
		self.subgroup=subgroup
	def printProduct(self):
		print("%s\t%s"%(self.id,self.name))

class Customer(object):
	"""docstring for Customer"""
	def __init__(self,id,name,address,phNo):
		self.id = id
		self.name = name
		self.address = address
		self.phNo = phNo

	def printCustomer(self):
		print("%s\t%s\t%s\t%s"%(self.id,self.name,self.address,self.phNo))

	def viewProducts():
		pass

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
		
		
		