from typing import List
def pals(x:str)-> List[str]:
    if len(x)==1:
        return [x]
    elif len(x)==2:
        if x[0]==x[1]:
            return [x]
        else:
            return []
    else:
        out=[]
        for i in pals(x[:-1]):
            if len(i)==len(x-1): # this should be a dict with keys as the lengths of the palindromes and values as lists of palindromes because of this line
            
               if i[0]==x[-1]:#left side
               out+= i+x[-1]
               elif i[-1]==x[-1] 
                
