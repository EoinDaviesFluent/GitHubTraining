from AppMain import count
from AppMain import factorial
from AppMain import list_of_squares
from AppMain import vowels
import pytest

def test_count_zeros():
	assert count.count([0,0,0],0)==3

def test_count_string():
	assert count.count(["a","a","a"],"a")==3

def test_count_minus():
	assert count.count([-1,-3,-5,-4], -1)==1

def test_count_normalNum():
	assert count.count([1,2,3,4,5,6,6,5,4,3,2,1], 1)==2

def test_factorial_5():
	assert factorial.fact(5) == 120

def test_factorial_10():
	assert factorial.fact(10) == 3628800

def test_factorial_7():
	assert factorial.fact(7) == 5040

def test_sqaure_minus():
	assert list_of_squares.list_of_squares(3) == {1: 1, 2: 4, 3: 9}

def test_sqaure_positive():
	assert list_of_squares.list_of_squares(3) == {1: 1, 2: 4, 3: 9}

def test_vowels_word():
	assert vowels.vowels('hello') == 2

def test_vowels_number_string():
	assert vowels.vowels('28') == 0