class LetterCheck:
	def __init__(self,letter_var):
		self.letter=letter_var
	def is_vowel(self):
		vowels=('a','e','i','o','u')
		if (self.letter).lower() in vowels:
			return True
		else:
			return False

	def is_enclosed(self):
		enclosed_letters=('a','d','o','p','q','r','b')
		if (self.letter).lower() in enclosed_letters:
			return True
		else:
			return False

	def has_dot_in_lower_case(self):
		lower_case_letters_with_dot=('i','j')
		if (self.letter).lower() in lower_case_letters_with_dot:
			return True
		else:
			return False

letter_1=LetterCheck('A')
letter_2=LetterCheck('M')
letter_3=LetterCheck('I')

print ('Is',letter_1.letter,'a vowel:',letter_1.is_vowel())
print ('Is',letter_2.letter,'a vowel:',letter_2.is_vowel())
print ('Is',letter_3.letter,'a vowel:',letter_3.is_vowel())

print ('Is',letter_1.letter,'an enclosed letter:',letter_1.is_enclosed())
print ('Is',letter_2.letter,'an enclosed letter:',letter_2.is_enclosed())
print ('Is',letter_3.letter,'an enclosed letter:',letter_3.is_enclosed())

print ('Does',letter_1.letter,'(as a lower case) have a dot:',letter_1.has_dot_in_lower_case())
print ('Does',letter_2.letter,'(as a lower case) have a dot:',letter_2.has_dot_in_lower_case())
print ('Does',letter_3.letter,'(as a lower case) have a dot:',letter_3.has_dot_in_lower_case())