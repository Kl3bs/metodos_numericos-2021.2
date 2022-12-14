import numpy as np

def f(x):
    y = x**2+7*x+10
    return y

def d(x):
    h = 0000000.1
    return ((f(x + h) - (f(x)))/h)




            

def bisection(a, b, error):
    #Iterations
    n = (np.log(b-a) - np.log(error)/np.log(2))
    n = np.ceil(n)
    index = 0
     
    while index < n:
        if f(a)*f(b) > 0:
            print("Is not possible to confirm if there is any root in this interval")
        else:
            m = round((a+b)/2)
            if f(a) * f(m) < 0:
                b = m
            else:
                a = m
                
        print(f'x{index+1} = {m}')
        index+=1
        
def newton(x0, tol,iterations):
    x = 0
    i = 0
    sequence = []
    while abs(f(x0)) > tol:
        x = x0 - f(x0)/d(x0)
        x0 = x
        i = i  + 1
        print(x0)
        sequence.append(x0)
        
        if (f(x0) == 0): 
            break

        if (i >= iterations):
            print("Could not find any root")
            break
    if i < iterations:
        print("\n\nRoot: %f\nIterations: %d\nf(%lf) = %g \n\n" %(x0,i,x0,f(x0)))
        return  sequence
  
# newton(5,  -0.5,100)
print(bisection(0,1,1))
 