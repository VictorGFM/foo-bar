#Decimal part of sqrt(2)
factor = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727

def calculateSumSequence(n):
    if n == 0:
        return 0

    nPrime = (factor * n)//(10**100)
    p = n * nPrime
    q = (n * (n + 1)) // 2
    r = (nPrime * (nPrime + 1)) // 2

    return p + q - r - calculateSumSequence(nPrime)

def solution(n):
    return str(calculateSumSequence(int(n)))

n=10**100

print(solution(n))