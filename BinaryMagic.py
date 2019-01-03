import numpy as np

#construct binary magic cards

#number of cards to construct
n = 6

#the maxinum number of value that can be attained with the given n
max_no = 2**n

#the result matrix, initialized with zeros
res = np.zeros((n,1), dtype=int)

#the loop to extend the result matrix
for dg in range(1, max_no):

    #convert the decimal number to binary in string
    bi = np.binary_repr(dg, width=n)
    bi = str(bi)

    #construct the array of 1 or 0 from the binary representation,
    #then tranpose it
    tflist = [int(b) for b in bi]
    temp = tflist
    temp = np.transpose([temp])

    #extend the result matrix with the decimal digit
    res = np.append(res, temp*dg, axis=1)

    #print to see how it looks like if necessary
    #print(temp*dg)


#removing repeating zeros
for x in res:
    y = np.unique(x)

    #the final output showing the numbers to be printed on each card
    #the length of each card is also provided as additional info
    print(y[1:])
    print('length = '+str(len(y)))

input("Press Enter to continue...")
    


