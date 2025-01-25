def reverse(x:str)->str:
    if len(x)==1:
        return x
    else:
        return x[-1]+reverse(x[:-1])
