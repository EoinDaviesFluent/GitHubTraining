car_sales_file=open('Python/Files IO/carSale.csv','r')
lines=car_sales_file.readlines()
car_sales_file.close()
#print (lines)
title=lines[0].strip()
title=title.split(',')
#print (title)
company_values=[]
company_name=[]
for i in range(1,len(lines)):
    manu_value=lines[i].strip()
    manu_value=manu_value.split(',')
    company_name.append(manu_value[0])
    manu_value.pop(0)
    manu_value=list(map(int, manu_value))
    company_values.append(manu_value)

#print (company_name)
#print (company_values)
print (company_values[0][0])
print (company_values[1][0])
print (company_values[0][1])
list_of_all=[]
for i in range(0,len(company_values[0])):
    list_of_month_values=[]
    for a in range(0,len(company_values)):
        #print (i,a)
        list_of_month_values.append(company_values[a][i])
    #print (list_of_month_values)
    list_of_all.append(sum(list_of_month_values))
    print ('For',title[i+1],'the number of cars sold was',sum(list_of_month_values))
print ('Grand Total:',sum(list_of_all))