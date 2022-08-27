def evaluate_poly(poly, x):


    counter = 0
    result = 0
    while counter < len(poly):
        result += (x**(counter))*(poly[counter])
        counter += 1

    return result

def compute_deriv(poly):
    counter = len(poly)-1

    while counter >= 0:
        poly[counter] = counter*poly[counter]
        counter -= 1
    poly.pop(0)
    return poly

def compute_root(poly, x_0, epsilon):
    rootguess = evaluate_poly(poly,x_0)
    counter = 0
    while abs(rootguess) > abs(epsilon):
        rootguess = rootguess - (evaluate_poly(poly, rootguess)/evaluate_poly(compute_deriv(poly), rootguess))
        counter += 1
        print('approximating: ',rootguess)
    return rootguess, counter

if __name__ == "__main__":
    #Compute value of x in polynomial function
    lengthofpoly = int(input('What is the max exponent of your function?:'))
    counter = 0
    poly = []
    while counter <= lengthofpoly:
        print('Enter coefficient of ', counter, 'power')
        poly.append(float(input()))
        counter += 1

    x = float(input('Enter value to solve function for: '))
    evalresult = evaluate_poly(poly, x)
    derivresult = compute_deriv(poly)
    print('polynomial evaluates to ',evalresult,'for x=',x)

    #Compute derivative
    counter = len(derivresult)-1
    result = []
    while counter >= 0:
        result.append(str(derivresult[counter]) + 'x^' + str(counter))
        counter -= 1
    print('derivative is: ',result)


    #Compute root using successive approximation
    print('Enter initial x value: ')
    x_0 = float(input())
    print('Enter epsilon value: ')
    epsilon = float(input())
    rootres = compute_root(poly, x_0, epsilon)
    print('Computed root at ',rootres[0],'in ',rootres[1], 'tries')
