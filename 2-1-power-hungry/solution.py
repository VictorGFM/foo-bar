from functools import reduce

def maxProductSubset(xs):
    if len(xs) == 1:
        return xs[0]
        
    # Get all negative numbers
    negatives = [i for i in xs if i < 0]
    
    # Check if there are odd numbers of negative values
    if len(negatives) % 2 == 1:
        # Remove least absolute value of negatives 
        xs.remove(max(negatives))
    
    # Remove all zeros
    while 0 in xs:
        xs.remove(0)
    
    # Check if list is empty
    if not xs:
        return 0
    
    # Calculate the max product of the subset
    product = reduce(lambda x, y: x * y, xs)

    return product

def solution(xs):
    # Your code here
    return str(maxProductSubset(xs))
