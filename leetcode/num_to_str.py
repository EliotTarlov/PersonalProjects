def int_to_str(x:int)->str:
    ONES = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 0: ""}
    TEENS = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",17: "seventeen", 18: "eighteen", 19: "nineteen"}
    TENS = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    SUFFIXES = ("hundred","thousand")+(x+"illion" for x in ["m","b","tr","quadr","quint","hex","sex"])
    out=""

    starting_power=(len(str(x))-1)//3 #highest order of magnitude of x
    leading_digits=(len(str(x)))%(starting_power*3)
    
    
    if x==0:
        return "zero"   
    elif x<0:
        return "negative "+out
    else:
        return out
    
        
    def _i_2_s_helper(x:int) -> str:
        #for values<1000
        if x<0:
            raise ValueError("Input must be >=0")
        elif x<10:
            return ONES[int(x)]
        elif x<20:
            return TEENS[int(x)]
        elif x<100:
            return TENS[x//10]+" "+_i_2_s_helper(x%10)
        elif x<1000:
            out=ONES[int(x//(100))]+" hundred"
            if int(x%100):
                return out+" and "+_i_2_s_helper(x%100)
            return out
        else:
            return _i_2_s_helper + " and " + _i_2_s_helper(x%1000) + SUFFIXES[len()]
            
