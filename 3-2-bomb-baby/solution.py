def solution(x, y):
    # Your code here
    x = int(x)
    y = int(y)

    #Euclidean Algorithm (Find GCD)
    steps = -1
    while y:
        x, (q, y) = y, divmod(x, y)
        steps += q #Steps based on Stern-Brocot tree

    if x > 1:
        return "impossible"
    else:
        return str(steps)

print(solution('4', '7'))
