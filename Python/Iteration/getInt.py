

min_num=1
max_num=100
user_input=-1
incorrect_attempts=0
while not(min_num<=user_input<=max_num):
    incorrect_attempts+=1
    print ('Please input a number between',min_num,'and',max_num)
    user_input=int(input(': '))
    if incorrect_attempts>=3:
        user_input=None
        break
print (user_input)

    
