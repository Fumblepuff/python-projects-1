import sys
import math

#Iterate through the list of arguments, skipping the first argument (the name of the script)
for i in sys.argv[1:]:
    #Taking in the argument as a float
    celcius = float(i)
    #Converting the temperature to Fahrenheit
    fer = (celcius * 9/5) + 32
    #Printing the temperature in Fahrenheit
    #  "{:.2f}".format(fer)  formats the result to 2 decimal places
    print("The temperature is "  + "{:.2f}".format(fer)  + " degrees Fahrenheit")





