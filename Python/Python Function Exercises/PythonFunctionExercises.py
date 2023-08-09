### 1 ###

def find_max(number_1,number_2,number_3):
    return (max(number_1,number_2,number_3))
print ('1)',find_max(18,9,73))

### 2 ###

def sum_of_list(list_input):
    return sum(list_input)
print ('2)',sum_of_list([1,2,3,4]))

### 3 ###

def multiply_list(list_input):
    output=list_input[0]
    for i in range(1,len(list_input)):
        output=output*list_input[i]
    return output
print ('3)',multiply_list([8,2,3,-1,7]))

### 4 ###

def reverse_word(input_word):
    letter_count=len(input_word)-1
    output_word=''
    for i in range(letter_count,-1,-1):
        output_word+=input_word[i]
    return output_word
print ('4)',reverse_word('1234abcd'))

### 5 ###

def factorial(number):
    output_number=number
    number-=1
    while number>0:
        output_number=output_number*number
        number-=1
    return output_number
print ('5)',factorial(5))