from itertools import combinations

def solution(num_buns, num_required):
    # Your code here
    bunnyKeys = [[] for num in range(num_buns)]
    copiesPerKey = num_buns - num_required + 1
    for key, bunnies in enumerate(combinations(range(num_buns), copiesPerKey)):
        for bunny in bunnies:
            bunnyKeys[bunny].append(key)
    return bunnyKeys

print(solution(5, 3))