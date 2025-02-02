#pip install matplotlib

#IMPORT
import json
import matplotlib.pyplot as plt

# Open and read the JSON file
with open(r'C:\Users\mannu\338 labs\internetdata.json', 'r') as file:
    data = json.load(file)

#print("hi")
#GROUPING
grouping_countries = {
    "countries_below" : [], 
    "countries_above" : []
}
for i in data: 
    income = i.get("incomeperperson")
    if ( (income is None) or (income =="null")) :
        grouping_countries["countries_below"].append(i) 
    elif (income <= 10000):
        grouping_countries["countries_below"].append(i) 
    else :
        grouping_countries["countries_above"].append(i)
#HIST DATA
below_income_values = [item["internetuserate"] for item in grouping_countries["countries_below"] if item.get("internetuserate") is not None]
above_income_values = [item["internetuserate"] for item in grouping_countries["countries_above"] if item.get("internetuserate") is not None]

#CREATING GRAPHS
#HIST1
plt.figure(figsize=(8, 6))
#plt.subplot(1, 2, 1)
plt.title('Histogram 1: Income < 10,000')
plt.hist(below_income_values, bins=15, alpha=0.7, edgecolor='black', color='blue')
plt.xlabel("Internet Usage Rate", fontsize=12)
plt.ylabel("Number of Countries", fontsize=12)
plt.savefig("hist1.png") #saves the file 
#plt.show() #close the figure
#plt.show()

#HIST2
plt.figure(figsize=(8, 6))
#plt.subplot(1, 2, 2)
plt.title('Histogram 2: : Income > 10,000')
plt.hist(above_income_values, bins=15, alpha=0.7, edgecolor='black', color='blue')
plt.xlabel("Internet Usage Rate", fontsize=12)
plt.ylabel("Number of Countries", fontsize=12)
plt.savefig("hist2.png") #saves the graph 
#plt.show() #closes the file
#plt.show()

# Adjust layout
#plt.tight_layout()


# Show histograms
#plt.show()

# Print the data
#print(data)