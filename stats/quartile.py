import math

enterData = True

data = []
while enterData:
    val = int(input("Enter a number: "))
    if val == -1:
        enterData = False
    else:
        freq = int(input("Enter the frequency of the number: "))
        for i in range(int(freq)):
            data.append(int(val))
    
    

data.sort()
#print mean
mean = sum(data)/len(data)
print("The mean is: " + str(mean))

#print median
if len(data) % 2 == 0:
    median = (data[len(data)//2] + data[len(data)//2 - 1])/2
else:
    median = data[len(data)//2]
print("The median is: " + str(median))

#print mode
mode = data[0]
modeCount = 1
for i in range(1, len(data)):
    if data[i] == mode:
        modeCount += 1
    elif data[i] != mode and modeCount < i:
        mode = data[i]
        modeCount = 1
print("The mode is: " + str(mode))

#print range
range = max(data) - min(data)
print("The range is: " + str(range))


#print all data
print("The data is: " + str(data))