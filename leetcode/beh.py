from math import factorial
def permutations(n:int,r:int) ->int:
    return factorial(n)/factorial(n-r)
def climbStairs(n: int) -> int:
    out=0
    for number_of_2s in range(n//2):
        out+=permutations(n,(n-number_of_2s))
    return out
print(climbStairs(3))
