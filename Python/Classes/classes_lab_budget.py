total_budget=100
class Budget:
	def __init__(self,category_budget=0):
		global total_budget
		
		self.budget=category_budget
		total_budget-=self.budget
	def withdraw(self,num_value):
		global total_budget
		total_budget+=num_value
		self.budget-=num_value
		return self.budget
	def deposit(self,num_value):
		global total_budget
		total_budget-=num_value
		self.budget+=num_value
		return self.budget
	def transfer(self,num_value,transfer_to_cat):
		transfer_to_cat.budget+=num_value
		self.budget-=num_value
print ('1) Total budget',total_budget)
clothing=Budget(30) # gives clothing a pre-budget of 30
entertainment=Budget() # no budget defaults to 0
food=Budget()
print()
print ('2) Total budget now',total_budget)
print ('Clothing Budget:',clothing.budget)
print ('Entertainment Budget:',entertainment.budget)
print ('Food Budget:',food.budget)
print()
clothing.withdraw(20)
print ('Clothing budget is now',clothing.budget)
print ('3) Total budget',total_budget)
print()
entertainment.deposit(5)
print ('Entertainment  budget is now',entertainment.budget)
print ('4) Total budget',total_budget)
print ()
entertainment.transfer(5,food)
print ('Transferred 5 from entertainment to food')
print ('Entertainment  budget is now',entertainment.budget)
print ('Food  budget is now',food.budget)