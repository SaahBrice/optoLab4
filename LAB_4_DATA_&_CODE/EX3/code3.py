import numpy as np
import matplotlib.pyplot as plt

# File paths for all temperatures
file_paths_dict = {
    25: [
        'LAB_4_DATA_&_CODE/EX3/IV 25C 5mA 0.25SUN 10AVERAGES.txt',
        'LAB_4_DATA_&_CODE/EX3/IV 25C 10mA 0.5SUN 10AVERAGES.txt',
        'LAB_4_DATA_&_CODE/EX3/IV 25C 15mA 0.75SUN 10AVERAGES.txt',
        'LAB_4_DATA_&_CODE/EX3/IV 25C 20mA 1SUN 10AVERAGES.txt'
    ],
    40: [
        'LAB_4_DATA_&_CODE/EX3/IV 40C 5mA 0.25SUN 10AVERAGES.txt',
        'LAB_4_DATA_&_CODE/EX3/IV 40C 10mA 0.5SUN 10AVERAGES.txt',
        'LAB_4_DATA_&_CODE/EX3/IV 40C 15mA 0.75SUN 10AVERAGES.txt',
        'LAB_4_DATA_&_CODE/EX3/IV 40C 20mA 1SUN 10AVERAGES.txt'
    ],
    55: [
        'LAB_4_DATA_&_CODE/EX3/IV 55C 5mA 0.25SUN 10AVERAGES.txt',
        'LAB_4_DATA_&_CODE/EX3/IV 55C 10mA 0.5SUN 10AVERAGES.txt',
        'LAB_4_DATA_&_CODE/EX3/IV 55C 15mA 0.75SUN 10AVERAGES.txt',
        'LAB_4_DATA_&_CODE/EX3/IV 55C 20mA 1SUN 10AVERAGES.txt'
    ],
    70: [
        'LAB_4_DATA_&_CODE/EX3/IV 70C 5mA 0.25SUN 10AVERAGES.txt',
        'LAB_4_DATA_&_CODE/EX3/IV 70C 10mA 0.5SUN 10AVERAGES.txt',
        'LAB_4_DATA_&_CODE/EX3/IV 70C 15mA 0.75SUN 10AVERAGES.txt',
        'LAB_4_DATA_&_CODE/EX3/IV 70C 20mA 1SUN 10AVERAGES.txt'
    ]
}

# Illumination levels corresponding to the file paths
illumination_levels = [0.25, 0.50, 0.75, 1.00]  # In Sun units

plt.figure(figsize=(10, 8))

for temp, file_paths in file_paths_dict.items():
    short_circuit_currents = []  # To store Isc values for each temperature

    for file_path in file_paths:
        # Read data
        data = np.loadtxt(file_path)
        voltage = data[:, 0]  # Voltage (V)
        current = data[:, 1]  # Current (mA)

        # Find Isc (current at voltage closest to 0)
        isc_index = np.argmin(np.abs(voltage))
        isc = abs(current[isc_index])
        short_circuit_currents.append(isc)

    # Plot for current temperature
    plt.plot(illumination_levels, short_circuit_currents, 'o-', label=f'{temp}°C', markersize=8, markerfacecolor='white', markeredgewidth=2)

# Customize plot
plt.xlabel('Illumination Level (Sun)')
plt.ylabel('Short Circuit Current (mA)')
plt.title('Short Circuit Current vs Illumination Level for Different Temperatures')
plt.legend(title='Temperature', loc='best')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.xlim(0, max(illumination_levels) +0.1)
plt.ylim(0, max(max(short_circuit_currents) for temp, file_paths in file_paths_dict.items()) * 1.1)
plt.show()
