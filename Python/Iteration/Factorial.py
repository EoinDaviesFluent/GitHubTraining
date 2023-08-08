number=int(input('Please enter a number: '))
current_number=number
factorial_result=number
while current_number>1:
    current_number-=1
    factorial_result=factorial_result*current_number

print ('The factorial number of',number,'is',factorial_result)