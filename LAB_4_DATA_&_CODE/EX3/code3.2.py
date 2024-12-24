import numpy as np
import matplotlib.pyplot as plt

def calculate_fill_factor(voltage, current):
    # Find Voc and Isc
    voc_index = np.argmin(np.abs(current))
    isc_index = np.argmin(np.abs(voltage))
    voc = voltage[voc_index]
    isc = (current[isc_index])
    
    # Find maximum power point
    power = np.abs(voltage * current)
    max_power_index = np.argmax(power)
    max_power = power[max_power_index]
    
    # Calculate fill factor
    ff = max_power / (voc * isc)
    
    return ff

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

# Illumination levels
illumination_levels = [0.25, 0.50, 0.75, 1.00]

# Create figure
plt.figure(figsize=(10, 8))

# Dictionary to store fill factors for each illumination level
fill_factors_by_illumination = {ill: [] for ill in illumination_levels}
temperatures = []

# Calculate fill factors for each temperature and illumination level
for temp, file_paths in file_paths_dict.items():
    temperatures.append(temp)
    for i, file_path in enumerate(file_paths):
        # Read data
        data = np.loadtxt(file_path)
        voltage = data[:, 0]
        current = data[:, 1]
        
        # Calculate fill factor
        ff = calculate_fill_factor(voltage, current)
        fill_factors_by_illumination[illumination_levels[i]].append(ff)

# Plot fill factor vs temperature for each illumination level
for illumination, fill_factors in fill_factors_by_illumination.items():
    plt.plot(temperatures, fill_factors, 'o-', 
             label=f'{illumination} Sun', 
             markersize=8, 
             markerfacecolor='white', 
             markeredgewidth=2)

plt.xlabel('Temperature (°C)')
plt.ylabel('Fill Factor')
plt.title('Fill Factor vs Temperature for Different Illumination Levels')
plt.legend(title='Illumination', loc='best')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()