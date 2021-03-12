import matplotlib.pyplot as plt
import numpy as np
import sys

name = ""
if len(sys.argv) != 2:
	print("python3 plotCSV.py [file]")
name = sys.argv[1]

x, y = np.loadtxt(name+".csv", delimiter=",", unpack=True)
plt.plot(x,y, label="Loaded from " + name)

plt.xlabel("x")
plt.ylabel("y")
plt.title(name)
plt.legend()
plt.savefig(name + ".png")
