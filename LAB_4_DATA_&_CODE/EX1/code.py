import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import e, k
import scipy.stats as stats

# Read data from file
file_path = 'LAB_4_DATA_&_CODE/EX1/25C DARK.txt'
data = np.loadtxt(file_path)

# Separate voltage and current data
voltage = data[:, 0]  # First column
current = data[:, 1]  # Second column (in mA)

# Convert current to A from mA
current = current * 1e-3

# Temperature in Kelvin (room temperature)
T = 273.15 + 25  # 25°C to Kelvin

# Thermal voltage
VT = k * T / e  # k is Boltzmann constant, e is elementary charge

# Select linear region in semi-log plot (adjust these values based on your data)
mask = (current > 1e-3) & (current < 1e-0)  # Select middle region
voltage_fit = voltage[mask]
current_fit = current[mask]

# Take natural log of current
ln_current = np.log(current_fit)

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(voltage_fit, ln_current)

# Calculate ideality factor and saturation current
n = 1 / (slope * VT)  # Ideality factor
I0 = np.exp(intercept)  # Saturation current in A

# Generate fit line
fit_line = np.exp(slope * voltage + intercept)

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Linear scale plot
ax1.plot(voltage, current*1e3, 'o', color='#1f77b4', markerfacecolor='white', markersize=8, markeredgewidth=3)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xlabel('Voltage (V)')
ax1.set_ylabel('Current (mA)')
ax1.set_title('Dark I-V Characteristics (Linear Scale)')
ax1.margins(x=0.02)

# Log scale plot with fit
ax2.semilogy(voltage, current*1e3, 'o', color='#1f77b4', markerfacecolor='white', markersize=8, markeredgewidth=3, label='Data')
ax2.semilogy(voltage, fit_line*1e3, 'r-', linewidth=2, label='Fit')
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_xlabel('Voltage (V)')
ax2.set_ylabel('Current (mA)')
ax2.set_title('Dark I-V Characteristics (Log Scale)')
ax2.margins(x=0.02)
ax2.legend()

# Add text box with parameters
textstr = f'Ideality Factor (n) = {n:.2f}\nSaturation Current (I₀) = {I0:.2e} A\nR² = {r_value**2:.4f}'
ax2.text(0.05, 0.95, textstr, transform=ax2.transAxes,
         bbox=dict(facecolor='white', alpha=0.8),
         verticalalignment='top')

plt.tight_layout()
plt.show()

# Print the extracted parameters
print(f"\nExtracted Parameters:")
print(f"Ideality Factor (n) = {n:.2f}")
print(f"Saturation Current (I₀) = {I0:.2e} A")
print(f"R² value = {r_value**2:.4f}")