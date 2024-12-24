import numpy as np
import matplotlib.pyplot as plt

# File paths for 1 SUN condition at different temperatures
files_1sun = {
    25: 'LAB_4_DATA_&_CODE/EX3/IV 25C 20mA 1SUN 10AVERAGES.txt',
    40: 'LAB_4_DATA_&_CODE/EX3/IV 40C 20mA 1SUN 10AVERAGES.txt',
    55: 'LAB_4_DATA_&_CODE/EX3/IV 55C 20mA 1SUN 10AVERAGES.txt',
    70: 'LAB_4_DATA_&_CODE/EX3/IV 70C 20mA 1SUN 10AVERAGES.txt'
}

plt.figure(figsize=(10, 8))

# Plot IV curves for each temperature
for temp, file_path in files_1sun.items():
    # Read data
    data = np.loadtxt(file_path)
    voltage = data[:, 0]  # Voltage (V)
    current = data[:, 1]  # Current (mA)
    
    # Plot
    plt.plot(voltage, -(current), 'o-', label=f'{temp}°C', 
             markersize=4, markerfacecolor='white', markeredgewidth=1)

# Customize plot
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('I-V Characteristics at Different Temperatures (1 SUN)')
plt.legend(title='Temperature', loc='best')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Set axis to start from zero


plt.show()