# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import date

# Uploading the temperature
Temperature = pd.read_csv("air_temperature_lahti.csv", dayfirst=True, sep=",",
                          header=0, decimal=b".", index_col=0,
                          parse_dates=[[0, 1, 2, 3]], usecols=[0, 1, 2, 3, 5])
Temperature.info()

# plotting year
plt.figure(figsize=(40, 10))
plt.plot(Temperature, color='black', linestyle='-', linewidth=3)
plt.title("Air Temperature at Lahti in 2020", fontsize=40, fontweight="bold")
plt.ylabel("Temperature in [°C]", fontweight='bold', fontsize=22)
plt.grid(True)
plt.show()

# plotting month
plt.figure(figsize=(20, 5))
plt.plot(Temperature.loc['2020-7'], color='black', marker="o",
         markerfacecolor="red", markersize=5, linestyle='-', linewidth=2)
plt.title("Air Temperature at Lahti in July 2020",
          fontsize=20, fontweight="bold")
plt.ylabel("Temperature in [°C]", fontweight='bold')
plt.grid(True)
plt.show()

# plotting week
plt.figure(figsize=(20, 5))
plt.plot(Temperature.loc['2020-3-2':'2020-3-8'], color='black', marker="o",
         markerfacecolor="purple", markersize=5, linestyle='-', linewidth=1)
plt.title("Air Temperature at Lahti in Week 10, 2020",
          fontsize=20, fontweight="bold")
plt.ylabel("Temperature in [°C]", fontweight='bold')
plt.grid(True)
plt.show()

# plotting day
fig, ax = plt.subplots(1, figsize=(20, 5))
plt.plot(Temperature.loc['2020-12-21'], color='black',
         marker="x", markersize=15, linestyle=':', linewidth=1)
plt.title("Air Temperature at Lahti in December 21, 2020",
          fontsize=20, fontweight="bold")
plt.ylabel("Temperature in [°C]", fontweight='bold')
plt.grid(True)
xfmt = mdates.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(xfmt)
plt.show()
