import statistics

# Sample data
data = [4, 7, 1, 2, 7, 5, 7, 9, 3]

# Calculate Mean
mean = statistics.mean(data)

# Calculate Mode
mode = statistics.mode(data)

# Calculate Variance
variance = statistics.variance(data)

# Display results
print("Data:", data)
print("Mean:", mean)
print("Mode:", mode)
print("Variance:", variance)
