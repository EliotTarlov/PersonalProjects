from numba import jit

@jit
def find_base_name(x: int) -> list[int]:
    if 0 <= x <= 12:
        print(x)
        return [x]
    candidate: int = -1
    i: int
    for i in range(2, x//2):
        if x % i == 0:
            if abs(i - (x // i)) < abs(candidate - (x // candidate)):
                candidate = i
    return find_base_name(candidate)+find_base_name(x // candidate)

print(find_base_name(17*10**17))
