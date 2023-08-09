def getincomeTax(salary):
    if salary<=34500: # 20%
        return salary*0.2
    elif 34501<=salary<=150000: # 40%
        return salary*0.4
    else: # 45%
        return salary*0.45
salary=float(input('Please input the salary: '))
outcome_tax=getincomeTax(salary)
print ('The income tax is:',outcome_tax)
