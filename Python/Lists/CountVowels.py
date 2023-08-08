vowels=('a','e','i','o','u')
vowel_count=0
word=input('Input a word: ')
for i in range(0,len(word)):
    if word[i] in vowels:
        vowel_count+=1
print ('There are',vowel_count,'vowels in',word)