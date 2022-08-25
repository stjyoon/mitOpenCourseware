def evaluate_poly(poly, x):


    counter = 0
    result = 0
    while counter < len(poly):
        result += x**(counter)*(poly[counter])
        counter += 1

    return result

def compute_deriv(poly):
    counter = len(poly)-1

    while counter >= 0:
        poly[counter] = counter*poly[counter]
        counter -= 1
    poly.pop(0)
    return poly
if __name__ == "__main__":

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
    print('derivative is: ',derivresult)
