from numba import jit
@jit
class tree():
    def __init__(self,value,left=None,right=None):
        self.value=value    #the bitmask for the position of the bit
        self.left=left      #has a zero at this position
        self.right=right    #has a one at this position, None if terminal (leaf node)
    def find_maximum_without_matching(multiplier):
        if self.value^multiplier==0:
            if self.right==None:
                return self.value
            else:
                if self.right.find_maximum_without_matching(multiplier)!=0:
                    return self.right.find_maximum_without_matching(multiplier) #self.right will always be larger than self.left
                else:
                    return self.left.find_maximum_without_matching(multiplier)
        else:
            return 0
for i in nums:
    if multiplier^value==0:
        return value
return 0
