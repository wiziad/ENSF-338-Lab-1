#IMPORT MODULES 
import json
import timeit
import matplotlib.pyplot as plt
import numpy as np

#LISTS
record_sizes =[1000, 2000, 5000, 10000]

average_time =[]

#OPENS THE INPUT/READING FILE  
with open(r'C:\Users\mannu\338 labs\large-file.json', "r", encoding= "utf-8") as file:

    jsonData = json.load(file) # loads the file onto program 

    
#FUNCTIONS
def sizeadjust(n):  #modifies the size field for the first n records
    for record in jsonData[:n]: #processes only the first 'n' records 
        record['size'] = 42 # changes field size to 42


#THE CALLING FUNCTIONS 
for n in record_sizes: 
    modsize_time = timeit.timeit(lambda:sizeadjust(n), number=100) # calculates the time it takes to change field size to 42 (100 times)
    avg_time = modsize_time / 100 # takes average of modsize_time
    average_time.append(avg_time)
    print(f"It takes an average of {avg_time:.4f} seconds to modify the {n} number of records(after being run 100 times).")


#LINEAR REGRESSION FROM THE GITHUB

# Now, compute linear regression to find the slope and intercept of the line
# that most accurately describes the relationship between input length and time.
# Then, plot the data and the line.
slope, intercept = np.polyfit(record_sizes, average_time, 1)  #1 means the linear fit line 
plt.figure(figsize=(8, 6))  # Adjust width and height
plt.xlabel("Number of Records")
plt.ylabel("Average Processing Time (seconds)")
plt.title("Processing Time vs Number of Records") 
plt.scatter(record_sizes, average_time) #makes a scatter plaot with (x,y)

linevalues = [slope * x + intercept for x in record_sizes] #uses the linear equation mx+b
plt.plot(record_sizes, linevalues, 'r') #plots the best fitting line in red
plt.xticks(record_sizes) #sets the x-axis to only the record sizes
plt.savefig("output.3.2.png") #saves the plot to file 

# Finally, print out the linear relationship between input length and time.
print("The linear model is: t = %.2e * n + %.2e" % (slope, intercept)) #displays the linear equation in scientific notation