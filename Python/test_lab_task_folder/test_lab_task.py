import pytest
def count(sequence, item): 
    sum = 0
    for n in sequence: 
        if n == item: 
            sum += 1
    return sum
 
animals=['Dog','Cat','Cow','Sheep','Llama','Pig','Horse','Goat','Cat','Llama','Sheep','Horse']
print (count(animals,'Sheep'))
def test_count():
    assert count(animals,'Goat') == 1
    assert count(animals,'Deer') == 0
    assert count(animals,'Sheep') == 2
    