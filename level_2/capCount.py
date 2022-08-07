import sys

for i in sys.argv[1:]:
    #Taking in the argument as a string
    input = str(i)
    
    #This variable will hold the count of capital letters
    count = 0
    
    #This list will hold the indices of the capital letters
    indices = []
    
    #This variable will hold the sum of the indices
    sum = 0
    
    #Iterating through the string
    for j in input:
        #If the character is upercase, increment the count
        if j.isupper():
            count += 1
            #Appending the index of the character to the list
            indices.append(input.index(j))
    
    
    #Iterating through the list of indices
    for k in indices:
        #Adding the index to the sum
        sum += k
    
    
    #Printing the count of capital letters
    print(count)
    #Printing the added indices of the capital letters
    print(sum)
