import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get high temperatures from file
filename = 'sitka_weather_07-2017.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

# Format plot.
plt.title("Daily high temperatures, July 2017", fontsize=24)
plt.xlabel('', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
