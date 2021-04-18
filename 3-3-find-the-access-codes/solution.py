def solution(l):
    # Your code here
    n = len(l)
    numberOfDivisors = [0] * n
    numberLuckyTriples = 0
    
    for i in range(n):
        for j in range(i):
            if(l[i]%l[j] == 0):
                numberOfDivisors[i] = numberOfDivisors[i] + 1
                numberLuckyTriples = numberLuckyTriples + numberOfDivisors[j]

    return numberLuckyTriples

#l = [1, 1, 1]
l = [1, 2, 3, 4, 5, 6]
#l = [3, 6, 9]
#l = [3, 6, 12]
#l = range(2, 2001)
print(solution(l))