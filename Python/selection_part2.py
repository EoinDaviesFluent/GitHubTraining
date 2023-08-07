num_1=float(input('Please enter a number: '))
num_2=float(input('Please enter another number: '))
print ()
print('1. Add (+)\n2. Subtract (-)\n3. Multiply (*)\n4. Divide (/)\n5. Square (s)')
choice=input('Please pick an option using either the number or () symbol: ')
if choice in ('1','+'):
    print (num_1,'+',num_2,'=',num_1+num_2)
elif choice in ('2','-'):
    print (num_1,'-',num_2,'=',num_1-num_2)
elif choice in ('3','*'):
    print (num_1,'*',num_2,'=',num_1*num_2)
elif choice in ('4','/'):
    print (num_1,'/',num_2,'=',num_1/num_2)
else:
    print (num_1,'SQUARED =',num_1*num_1)
    print (num_2,'SQUARED =',num_2*num_2)