import csv
import numpy as np
import matplotlib.pyplot as plt

# Read the data from the csv file
data = []
with open('data8.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        data.append(float(row[0]))

# Calculate the average weight of newborns
W = np.mean(data)
print(W)

"""Calculate the weight value X such that 33% of 
newborns from the distribution are born with a weight below X
"""
X = np.percentile(data, 33)
print(X)


# Plot a histogram of the newborn weights with both values W and X on the graph
plt.figure(figsize=(10, 5))
weights, bins, _ = plt.hist(data, bins=50, edgecolor = "white",
                            alpha=0.8, facecolor = "gray",
                            label='Distribution of \n newborn weights')
plt.axvline(x=W, color='b', linestyle='--',
            label='Average weight = \n {:.2f} kg'.format(W))
plt.axvline(x=X, color='k', linestyle='-.',
            label='33% of newborns \n weigh below {:.2f} kg'.format(X))

# Add labels and titles to the plot
plt.xlabel('[Weight (kg)]', fontsize=25, color = "red")
plt.xlim(2.3, 5)
plt.ylim(0, 30)
plt.yticks(np.arange(0, 40, 5), fontsize="18")
plt.xticks(np.arange(2.3, 5.1, 0.3), fontsize="18")
plt.ylabel('No. of Newborns \n near by the weight', 
           fontsize=22, color = "green")
plt.title('(Newborns weight Distribution)', fontsize=50, color="m")
plt.legend(prop = {"size":15})

# Print the values of W and X on the graph
plt.text(x=W+0.01, color='b', y=np.max(weights)/9, fontsize=20,
         s='W = {:.2f} kg'.format(W))
plt.text(x=X-0.58, color='k', y=np.max(weights)/1.5, fontsize=20,
         s='X = {:.2f} kg'.format(X))

#Save the picture 
plt.savefig("22003118.png")

# Display the plot
plt.show()
