import pickle
from classes import Admin
F_ADMIN="admins.txt"
F_CUSTOMER="customers.txt"

def createAdmin(id,name):
	admin=Admin(id,name)
	adminFile=open(F_ADMIN,"wb")
	pickle.dump(admin,adminFile)
	adminFile.close()
	pass

def authAdmin(id):
	adminFile=open(F_ADMIN,"rb")
	while True:
		try:
			admin=pickle.load(adminFile)
			if(admin.id==id):
				return admin
		except EOFError:
			break
	adminFile.close()
	return None

def authCustomer(id):
	customerFile=open(F_CUSTOMER,"rb")
	while True:
		try:
			customer=pickle.load(customerFile)
			if(customer.id==id):
				return customer
		except EOFError:
			break
	customerFile.close()
	return None