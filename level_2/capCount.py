import sys

for i in sys.argv[1:]:
    #Taking in the argument as a string
    input = str(i)
    
    #This variable will hold the count of capital letters
    count = 0
    
    #This variable will hold the sum of the indices
    sum = 0
    
    #Iterating through the string
    for j in input:
        #If the character is upercase, increment the count
        if j.isupper():
            count += 1
            #Incrementing the sum by the index of the character
            sum += input.index(j)
    
    
    
    #Printing the count of capital letters
    print(count)
    #Printing the added indices of the capital letters
    print(sum)
