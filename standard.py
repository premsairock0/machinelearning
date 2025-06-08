import statistics

# Sample data
data = [4, 7, 1, 2, 7, 5, 7, 9, 3]

# Calculations
mean = statistics.mean(data)
median = statistics.median(data)
std_dev = statistics.stdev(data)

# Output
print("Data:", data)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
