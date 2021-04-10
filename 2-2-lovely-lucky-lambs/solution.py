def generous(total_lambs):
    i=0
    total_pay = 0
    while i <= total_lambs:
        total_pay = total_pay + 2**i
        if(total_pay > total_lambs): break
        i = i + 1
    return i

def stingy(total_lambs):
    i=0
    a, b = 1,1
    total_pay = 0
    while i <= total_lambs:
        total_pay = total_pay + a
        if(total_pay > total_lambs): break
        a, b = b, a + b
        i = i + 1
    return i

def solution(total_lambs):
    # Your code here
    return stingy(total_lambs) - generous(total_lambs)
