def solve(X, Y, solution=[]):
    if not X:
        yield list(solution)
    else:
        c = min(X, key=lambda c: len(X[c]))
        for r in list(X[c]):
            solution.append(r)
            cols = select(X, Y, r)
            for s in solve(X, Y, solution):
                yield s
            deselect(X, Y, r, cols)
            solution.pop()

def select(X, Y, r):
    cols = []
    for j in Y[r]:
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].remove(i)
        cols.append(X.pop(j))
    return cols

def deselect(X, Y, r, cols):
    for j in reversed(Y[r]):
        X[j] = cols.pop()
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].add(i)
def maxProduct(nums):
    Y={}
    X=set()
    for i in nums:
        i="{:b}".format(i)
        tmp=[]
        for j in range(0,len(i)):
            if i[-1-j]=="1":
                tmp+=[str(j)]
                X.add(str(j))
        Y[i]=tmp
    X=list(X)
    X = {j: set() for j in X}
    for i in Y:
        for j in Y[i]:
            X[j].add(i)
    max=0
    for i in solve(X,Y):
        if len(i)==2:
            if int(i[0],2)*int(i[1],2)>max:
                max=int(i[0],2)*int(i[1],2)
    return max
            


print(maxProduct(list(range(0,1001))))
