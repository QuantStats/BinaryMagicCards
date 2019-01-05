import numpy as np

#construct binary magic cards with n as input

#number of cards to construct as determined by the user
n = int(input('How many binary magic cards do you want to construct?'))

#the maxinum number of value that can be attained with the given n
m = 2**n-1

#the result matrix, initialized with zeros
res = np.zeros((n,1), dtype=int)

#the loop to extend the result matrix
for dg in range(1, m+1):

    #convert the decimal number to binary in string
    bi = np.binary_repr(dg, width=n)
    bi = str(bi)

    #construct the array of 1 or 0 from the binary representation,
    #then tranpose it
    temp = [int(b) for b in bi]
    temp = np.transpose([temp])

    #extend the result matrix with the decimal digit
    res = np.append(res, temp*dg, axis=1)

    #print to see how it looks like if necessary
    #print(temp*dg)

counter = n+1

#removing repeating zeros
for x in res:
    x = np.unique(x)
    x = x[1:]

    #the final output showing the numbers to be printed on each card
    #the length of each card is also provided as additional info
    counter-=1
    print('Card '+str(counter)+ ' prints')
    print(x)
    print('length = '+str(len(x)))

input('Press Enter to continue...')
    


