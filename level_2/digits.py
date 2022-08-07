import sys

for i in sys.argv[1:]:
    #Taking in the argument as a string
    input = str(i)
    #Removing any decimal points from the string
    input = input.replace(".", "")
    #printing the number of digits in the string
    print(str(len(input)))