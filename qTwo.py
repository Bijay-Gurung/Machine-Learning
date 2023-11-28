"""
A shopkeeper sells an apple. One day he decide to calculate the profit and loss of apple
 that he sell from the past 7 days.
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([12,24,6,8,13,24,26])
days = np.array(["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])

mean = np.mean(x)
standardDeviation = np.std(x)
day = np.arange(len(days))

plt.title("Record of sells from the past 7 Days")
plt.xlabel("Days")
plt.ylabel("no.of Sells")
plt.xlim(day[0],day[-1])
plt.plot(x,color="blue",marker="o",label="Data")
plt.axhline(y=mean,color="red",linestyle="--",label="Mean")
plt.axhline(y=standardDeviation+mean,color="green",linestyle="--",label="+Standard Deviation")
plt.axhline(y=standardDeviation-mean,color="green",linestyle="--",label="-Standard Deviation")
plt.legend()
plt.show()