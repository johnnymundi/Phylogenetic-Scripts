import matplotlib.pyplot as plt

'''

  This script verifies ranges from different distances between genes
  Type of input - a .txt file containing data such as:
  7678
  4606879
  34190
  42329059
  22008
  4631
  514063
  13853
  14271
'''



# Opens the .txt file
with open('Xborealis_distance.txt') as f:
    distances = [int(line.strip()) for line in f]

# define the range size and the maximum distance
range_size = 1000  # adjust this as needed
max_distance = 500000  # adjust this as needed

# create a list of range boundaries using the range function
ranges = list(range(-range_size // 2, max_distance, range_size))

# count the number of distances that fall within each range using a list comprehension
counts = [len([d for d in distances if r <= d < r+range_size]) for r in ranges]
# This creates a list of counts, where each count represents the number of distances that fall within a particular range

# Finally, plot the histogram using a plotting library such as Matplotlib
plt.bar(ranges, counts, width=range_size, color='black')
plt.xticks([i*20000 for i in range(1, int(max_distance/20000)+1)], ['{}'.format(i*20) for i in range(1, int(max_distance/20000)+1)])
plt.xlabel('Distance (kilobases)')
plt.ylabel('Frequency')
plt.show()
