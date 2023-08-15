""" Linting Task"""
def count(sequence, item):
    """Function to count how many items are in a list"""
    item_count = 0
    for index in sequence:
        if index == item:
            item_count += 1
    return item_count



