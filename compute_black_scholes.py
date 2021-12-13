import math 

def compute(S_0, X, r, T, sig):
    C_0 = S*math.normal(D1(S_0, X, r, T, sig)) - X*math.topower(math.e, -rT)*math.normal(D2(S_0, X, r, T, sig))
    return C_0 
    
    
def D1(S, X, r, T, sig):
    result = (math.ln(S/X) + (r + math.square(sig)/2)*T)/sig*math.sqrt(T)
    return  result
def D2(S, X, r, T, sig):
    result = (math.ln(S/X) + (r - math.square(sig)/2)*T)/sig*math.sqrt(T)
    return result
    