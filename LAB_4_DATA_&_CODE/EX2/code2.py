
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

# Plot current vs voltage
plt.figure(figsize=(10, 8))

for file_path, label in zip(file_paths, labels):
    # Read data
    data = np.loadtxt(file_path)
    voltage = data[:, 0]  # Voltage (V)
    current = data[:, 1]  # Convert current from mA to A

    # Plot
    plt.plot(voltage, current, label=label)

    # Find Voc (voltage at current closest to 0)
    voc_index = np.argmin(np.abs(current))
    voc = voltage[voc_index]

    # Find Isc (current at voltage closest to 0)
    isc_index = np.argmin(np.abs(voltage))
    isc = current[isc_index]

    print(f"File: {file_path}")
    print(f"Open-Circuit Voltage (Voc): {voc:.3f} V")
    print(f"Short-Circuit Current (Isc): {isc:.3e} mA\n")




# Customize plot
plt.xlim(left=0)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('Current vs Voltage for Different Illumination Levels (FORTH QUADRANT)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.xlim([0, max(voltage)])
plt.ylim([min(current), 0])
# Show plot
plt.show()
