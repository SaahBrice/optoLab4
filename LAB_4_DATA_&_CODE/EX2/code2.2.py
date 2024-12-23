import numpy as np
import matplotlib.pyplot as plt

# File paths
file_paths = [
    'LAB_4_DATA_&_CODE/EX2/IV 25C 5mA 0.25SUN 10AVERAGES.txt',
    'LAB_4_DATA_&_CODE/EX2/IV 25C 10mA 0.5SUN 10AVERAGES.txt',
    'LAB_4_DATA_&_CODE/EX2/IV 25C 15mA 0.75SUN 10AVERAGES.txt',
    'LAB_4_DATA_&_CODE/EX2/IV 25C 20mA 1SUN 10AVERAGES.txt'
]

# Labels for each dataset
labels = [
    '5mA (0.25 SUN)',
    '10mA (0.5 SUN)',
    '15mA (0.75 SUN)',
    '20mA (1 SUN)'
]

# Plot output power as a function of voltage
plt.figure(figsize=(10, 6))

for file_path, label in zip(file_paths, labels):
    # Read data
    data = np.loadtxt(file_path)
    voltage = data[:, 0]  # Voltage (V)
    current = data[:, 1]  # Convert current from mA to A

    # Calculate power
    power = -(voltage * current)
    voc_index = np.argmin(np.abs(current))
    voc = voltage[voc_index]

    # Find Isc (current at voltage closest to 0)
    isc_index = np.argmin(np.abs(voltage))
    isc = current[isc_index]
    max_power = max(power)
    fillF = max_power / -(voc * isc)
    print(f"File: {file_path}")
    print(f"max_power: {max_power:.3f} mW")
    print(f"fill Factor: {fillF:.3f}\n")
    # Plot
    plt.plot(voltage, power, label=label)
    plt.plot(voltage[np.argmax(power)], max(power), 'ro', markersize=6, )

# Customize plot
plt.xlabel('Voltage (V)')
plt.ylabel('Output Power (W)')
plt.title('Output Power vs Operating Voltage')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()


# Show plot
plt.show()
