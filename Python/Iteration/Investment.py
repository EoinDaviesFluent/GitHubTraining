initial_investment=float(input('Please input the Initial Investment: '))
target_value=float(input('Please input the Target Value: '))
interest_rate=float(input('Please input the Interest Rate: '))
current_investment=initial_investment
year_count=0
dec_interest_rate=(interest_rate/100)
interest_add=initial_investment*dec_interest_rate
print ('sub',interest_add)
while current_investment<target_value:
    
    #current_investment+=initial_investment
    current_investment+=interest_add
    year_count+=1
    interest_add=current_investment*dec_interest_rate
    print ('Year',year_count,'paid',round(current_investment,2),'out of',round(target_value,2),' - Interest Rate',round(interest_add,2))
    
    #print ('sub',interest_add)
if current_investment>target_value:
    print ('Overpaid',round(current_investment-target_value,2))