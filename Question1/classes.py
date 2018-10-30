import setting
import setting
class Operations(object):
	"""docstring for Operations"""
	Guest="1. Register\n2. View Products\n3. Go to Home"	
	Customer="1. View Products\n2. Buy Products\n3. Search Product(by name)\n4. My orders\n5. Logout"	
	CustomerSub="1. Add to Cart\n2. Delete from Cart\n3. View Cart\n4. Make Payment\n5. Go Back"	
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
			print("Product modified successfully")

class Product(object):
	"""docstring for Product"""
	def __init__(self, id,name,group,subgroup,price):
		self.id=id
		self.name=name
		self.group=group
		self.subgroup=subgroup
		self.price=price
	def printProduct(self):
		print("%-10d%-20s%-20s%-20s%-15.2f"%(self.id,self.name,self.group,self.subgroup,self.price))

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

	def makePayment(self,payment):
		payment.pay(self)

	def searchProducts(self,name):
		searchedProList=list()
		for key in setting.productsList:
			if name in setting.productsList[key].name:
				searchedProList.append(setting.productsList[key])
		return searchedProList

	def getProduct(self,pid):
		return setting.productsList.get(pid,None)

	def getCart(self):
		if self.id in setting.cartsList:
			return setting.cartsList[self.id]
		else:
			return None;

	def deleteFromCart(self,product):
		cart=self.getCart()
		flag=False
		if cart:
			products=cart.products
			for prod in products:
				if prod.id==product.id:
					flag=True
					(cart.products).remove(prod)
					cart.noProducts-=1
					cart.total-=prod.price
					setting.cartsList.pop(self.id, None)
					setting.cartsList[self.id]=cart
					break
			if(len(cart.products)==0):
				setting.cartsList.pop(self.id, None)
			if flag:
				print("Product Removed from cart successfully")
			else:
				print("No product in cart with id: "+str(product.id))
		else:
			print("Your cart is empty")
	def addToCart(self,product):
		if self.id in setting.cartsList:
			cart=setting.cartsList[self.id]
			cart.noProducts+=1
			(cart.products).append(product)
			cart.total+=product.price
			setting.cartsList[self.id]=cart
			# print("Cannot add product: "+str(product.id)+" already exist")
		else:
			cart=Cart(self.id,1,[product],product.price)
			setting.cartsList[self.id]=cart
			# print("Product with id "+str(product.id)+" added successfully")
	def myOrders(self):
		myOrders=setting.myOrdersList.get(self.id,None)
		if myOrders:
			print("--------------------------------MY ORDERS------------------------------------")
			# print("ID\t\tNAME\t\tGROUP\t\tSUBGROUP\t\tPRICE")
			print("%-10s%-20s%-20s%-20s%-15s"%('ID','NAME','GROUP','SUBGROUP','PRICE'))
			for prod in myOrders:
				prod.printProduct()
		else:
			print("You haven't bought any product")
		

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
	def pay(self,customer):
		cart=customer.getCart()
		# if cart:
		print("Please Wait...")
		print("Amount paid: "+str(cart.total)+" Rs.")
		print("Card Holder name: "+self.name)		
		print("Card Number: "+self.cardNo)		
		# print("%s\t\t%s\t\t%s\t\t%s"%(self.customerId,self.name,self.cardType,self.cardNo))
		print("Payment Done Successfully")

		#empty cart and populate my orders
		myOrders=setting.myOrdersList.get(customer.id,None)
		if myOrders:
			setting.myOrdersList[customer.id]=setting.myOrdersList[customer.id]+cart.products
		else:
			setting.myOrdersList[customer.id]=cart.products
		setting.cartsList.pop(customer.id, None)

		# else:
			# print("Please add products: Cart Empty")
		
class Cart(object):
	"""docstring for Cart"""
	def __init__(self, id, noProducts, products, total):
		self.id=id
		self.noProducts=noProducts
		self.products=products
		self.total=total
	def printCart(self):
		print("---------Your Cart---------")
		print("ID\t\tNAME\t\tGROUP\t\tSUBGROUP\t\tPRICE")
		for prod in self.products:
			prod.printProduct()
		print("---------------------------")
		print("Total items-"+str(self.noProducts))
		print("Amount to pay-"+str(self.total)+" Rs.")
		print("")

		
		