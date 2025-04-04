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
