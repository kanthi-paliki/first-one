import pandas as pd
import math
def forward_newton(x,y,xp):
    n = len(y)
    h = x[1]-x[0]
    
    df = pd.DataFrame({"x":x,"y":y})
    for j in range(1,n):
        colname = f"D^{j}y"
        df[colname] = df.iloc[:,j].diff().shift(-1)

        firstrow = df.iloc[0,1:].dropna().tolist()
        
        u = (xp-x[0])/h
        res = firstrow[0]
        term = 1
        for j in range(1,len(firstrow)):
            term*=(u-(j-1))
            res += (term/math.factorial(j))*firstrow[j]
    return res,df
x = [40,44,48,52,56,60]
y = [20.8,20.6,20.2,19.7,18.9,17.9]
xp = 42
value,table = forward_newton(x,y,xp)
print("Table:\n",table)
print(f'Interpolated value at {xp} = {value}')