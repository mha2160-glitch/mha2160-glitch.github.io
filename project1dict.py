# Open data
import csv

data = []
with open("your_dataset.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        # pick one numeric column, for example column 2 (index 1)
        value = float(row[1])
        data.append(value)

# Calculate mean
mean_value = sum(data) / len(data)

# Calculate median
data.sort()
n = len(data)
if n % 2 == 0:
    median_value = (data[n // 2 - 1] + data[n // 2 + 1]) / 2
else:
    median_value = data[n // 2]

# Calculate mode
counts = {}
for num in data:
    counts[num] = counts.get(num, 0) + 1

# find the number(s) with the highest count
max_count = max(counts.values())
modes = [k for k, v in counts.items() if v == max_count]

print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", modes)
