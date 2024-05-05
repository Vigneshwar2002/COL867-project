import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('features.csv')

# Compute throughput
df['throughput'] = (df['upstream_volume'] + df['downstream_volume']) / df['flow_duration']

# Filter data for 'Cellular' and 'Wired' labels
cellular_data = df[df['label'] == 'Cellular']
wired_data = df[df['label'] == 'Wired']

# Plot throughput for Cellular
plt.figure(figsize=(10, 6))
plt.plot(cellular_data.index, cellular_data['throughput'], marker='o', linestyle='-', label='Cellular')
plt.xlabel('Data Point Index')
plt.ylabel('Throughput')
plt.title('Throughput for Cellular')
plt.legend()
plt.show()

# Plot throughput for Wired
plt.figure(figsize=(10, 6))
plt.plot(wired_data.index, wired_data['throughput'], marker='o', linestyle='-', label='Wired')
plt.xlabel('Data Point Index')
plt.ylabel('Throughput')
plt.title('Throughput for Wired')
plt.legend()
plt.show()

# Plot distribution for Cellular and Wired
plt.figure(figsize=(10, 6))
plt.hist(cellular_data['throughput'], bins=20, alpha=0.5, label='Cellular')
plt.hist(wired_data['throughput'], bins=20, alpha=0.5, label='Wired')
plt.xlabel('Throughput')
plt.ylabel('Frequency')
plt.title('Distribution of Throughput for Cellular and Wired')
plt.legend()
plt.show()
