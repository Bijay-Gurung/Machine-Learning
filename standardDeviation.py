"""
During a survey 6 students were asked how many hours per day they study on an average? Their answer were as follows:
2,6,5,3,2,3. Evaluate the standard deviation.
"""
import numpy as np
import matplotlib.pyplot as plt

n = np.array([2, 6, 5, 3, 2, 3])
mean_value = np.mean(n)
std_deviation = np.std(n)

plt.title("Data with Standard Deviation")
plt.plot(n, marker='o', label="Data", color="blue")
plt.axhline(y=mean_value, color='red', linestyle='--', label="Mean")
plt.axhline(y=mean_value + std_deviation, color='green', linestyle='--', label="Mean + 1 Std Dev")
plt.axhline(y=mean_value - std_deviation, color='green', linestyle='--', label="Mean - 1 Std Dev")
plt.legend()
plt.show()

