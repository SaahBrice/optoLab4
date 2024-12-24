import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the logarithmic function for fitting
def log_fit(x, a, b):
    return a + b * np.log(x)

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
illumination_levels = np.array([0.25, 0.50, 0.75, 1.00])  # In Sun units

plt.figure(figsize=(10, 8))

# Create smooth x points for the fit line
x_smooth = np.linspace(min(illumination_levels), max(illumination_levels), 100)

for temp, file_paths in file_paths_dict.items():
    open_circuit_voltages = []  # To store Voc values for each temperature

    for file_path in file_paths:
        # Read data
        data = np.loadtxt(file_path)
        voltage = data[:, 0]  # Voltage (V)
        current = data[:, 1]  # Current (mA)

        # Find Voc (voltage at current closest to 0)
        voc_index = np.argmin(np.abs(current))
        voc = voltage[voc_index]
        open_circuit_voltages.append(voc)

    # Convert to numpy array for fitting
    open_circuit_voltages = np.array(open_circuit_voltages)
    
    # Fit logarithmic curve
    popt, _ = curve_fit(log_fit, illumination_levels, open_circuit_voltages)
    
    # Plot data points
    plt.plot(illumination_levels, open_circuit_voltages, 'o', label=f'{temp}°C (data)', 
             markersize=8, markerfacecolor='white', markeredgewidth=2)
    
    # Plot fitted curve
    plt.plot(x_smooth, log_fit(x_smooth, *popt), '--')

# Customize plot
plt.xlabel('Illumination Level (Sun)')
plt.ylabel('Open Circuit Voltage (V)')
plt.title('Open Circuit Voltage vs Illumination Level for Different Temperatures\nwith Logarithmic Fits')
plt.legend(title='Temperature', loc='best')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()