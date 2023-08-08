print ('''Pythagoras' Calculator:
1. Find the length of A given B and C
2. Find the length of B given A and C
3. Find the length of C given A and B''')

choice=input('Please input 1,2 or 3: ')
if choice=='1':
    side_b=float(input('Please input the length of side B: '))
    side_c=float(input('Please input the length of side C: '))
    if side_c<=side_b:
        print ('Length of Side C must be longer than the length of Side B')
    else:
        squared_b=side_b**2
        squared_c=side_c**2
        side_a=(squared_c-squared_b)**0.5
        print ('Length of A:',side_a)
elif choice=='2':
    side_a=float(input('Please input the length of side A: '))
    side_c=float(input('Please input the length of side C: '))
    if side_c<=side_a:
        print ('Length of Side C must be longer than the length of Side A')
    else:
        squared_a=side_a**2
        squared_c=side_c**2
        #print (squared_a,squared_c,squared_c-squared_a)
        side_b=(squared_c-squared_a)**0.5
        print ('Length of B:',side_b)
else:
    side_a=float(input('Please input the length of side A: '))
    side_b=float(input('Please input the length of side B: '))
    squared_a=side_a**2
    squared_b=side_b**2
    squared_c=squared_a+squared_b
    side_c=(squared_c)**0.5
    print ('Length of C:',side_c)