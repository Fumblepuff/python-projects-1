import sys

#Iterate through the list of arguments, skipping the first argument (the name of the script)
for i in sys.argv[1:]:
    #Taking in the argument as a float
    celcius = float(i)
    #Converting the temperature to Fahrenheit
    fer = (celcius * 9/5) + 32
    #Printing the temperature in Fahrenheit
    print("The temperature is "  + str(fer)  + " degrees Fahrenheit")





