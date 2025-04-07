""
State
	long id primary
	string name
	float state_tax
	float income_tax
	float average_gas_price

Company
	long id primary
	string name
	int total_employee
	float state_tax
	float income_tax

Employee
	long id primary
	string name
	float rent
	long state
	long employed_with
	fk state => State.id
	fk employed_with => Company.id
""
class Company:
	def __init__(self, total_employee, state_tax, income_tax, id = -1):
		self.total_employee = total_employee
		self.state_tax = state_tax
		self.income_tax = income_tax
		self.id = -1
#GET
	def getTE(self):
		return self.total_employee
	def getST(self):
		return self.state_tax
	def getIT(self):
		return self.income_tax
	def getID(self):
		return self.id
#SET
	def setTE(self, TE):
		self.total_employee = TE
	def setST(self, ST):
		self.state_tax = ST
	def setIT(self, IT):
		self.income_tax = IT
	def setID(self, ID):
		self.id = ID
		
#COMPARE
	def is_equal(self, other_company):
	        if not isinstance(other_company, Company):
	            return False
	        return (self.total_employee == other_company.getTE() and
	                self.state_tax == other_company.getST() and
	                self.income_tax == other_company.getIT() and
	                self.id == other_company.getID())
		
		


