from sympy import * 

ng = []
ks = []

for n in range(4, 10000000, 2):
    for k in range(int(n/4)): 
        if isprime(int((n/2)-k)) and isprime(int((n/2)+k)): 
            #print(int((n/2)-k), " ", int((n/2)+k), " = ", int((n/2)-k) + int((n/2)+k), ",   k = ", k)
            ng.append( int((n/2)-k) + int((n/2)+k) )
            ks.append(k)
            break


#print(ks)

for x in range(100): 
    print(ks.count(x), end=" ") 