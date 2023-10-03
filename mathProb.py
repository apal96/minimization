import numpy as np
from scipy.optimize import minimize

def absFunction(x):
    z = abs(np.log(0.78) + 300 * x) + abs(np.log(0.37) + 1200 * x) + abs(np.log(0.08) + 3000 * x)
    return z

def sumOfSquares(x):
    z = pow((np.log(0.78) + 300 * x),2) + pow((np.log(0.37) + 1200 * x),2) + pow((np.log(0.08) + 3000 * x),2)
    return z

def minimizeFunc(eqtn):
    start = 0.0
    #minimize function from scipy 
    result = minimize(eqtn, start, bounds=[(0, 1)])

    # The result will contain the minimum value and the corresponding x value
    min_value = result.fun
    min_x = result.x
 
    print("Smallest value of k :", min_x[0])
    print("Minimum value of the function:", min_value)
    return min_x[0], min_value
print("Absolute Value")
absV,ignoreVal = minimizeFunc(absFunction)
print("Sum of Squares")
sumS,ignoreVal2 = minimizeFunc(sumOfSquares)
diff = absV-sumS
print(f'Difference: {diff}')
print(f'% Change: {round(((diff)/sumS)*100,2)}')
