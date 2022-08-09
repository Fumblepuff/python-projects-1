import sys

#This variable will hold the total sum of the GPAs
gpa = 0
#The given gpa dictionary
gpaDictionary = {'A':4.0, 'A-':3.66, 'B+':3.33, 'B':3.0, 'B-':2.66, 'C+':2.33, 'C':2.0, 'C-':1.66, 
'D+':1.33, 'D':1.00, 'D-':.66, 'F':0.00}
for i in sys.argv[1:]:
    #Taking in the argument as a string and casting to upper case
    grade = str(i).upper()
    #Summing the total GPA based on the given dictionary
    gpa += gpaDictionary[grade]

#Printing the average GPA
print("My GPA is " + "{:.2f}".format(gpa/4))