#IMPORT MODULES
import json
import matplotlib.pyplot as plt 
import timeit
import numpy as np 

#OPENING THE FILE 
with open(r'C:\Users\mannu\338 labs\large-file.json', "r", encoding= "utf-8") as file:
    jsonData = json.load(file) # loads the file onto program 

    
def sizeadjust(n):
    for record in jsonData[:n]:
        record['size'] = 42 # changes field size to 42

record_size = 1000
repeat_times = timeit.repeat(lambda:sizeadjust(record_size),repeat=1000, number=1) 
#measures execuriton time using timeit.repeat


# Measure execution time using timeit.repeat
repeat_times = timeit.repeat(lambda: sizeadjust(record_size), repeat=1000, number=1)

# Convert list to NumPy array for processing
time_data = np.array(repeat_times)

# Plot histogram
plt.hist(time_data, bins=30, color='blue', edgecolor='black', alpha=0.7)
plt.xlabel("Processing Time (seconds)")
plt.ylabel("Frequency")
plt.title("Distribution of Processing Time for 1000 Records (1000 Repetitions)")
plt.savefig("output.3.3.png")  # Save histogram plot to file
plt.show()

# Save modified JSON to a new file
with open('output_modified.json', 'w', encoding="utf-8") as file:
    json.dump(jsonData, file)  # Creates new file with modified content
