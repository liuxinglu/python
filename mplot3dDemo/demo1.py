#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
sinY = np.sin(x)
cosY = np.cos(x*2)
tanY = np.tan(x)

plt.figure(figsize=(8,4))
plt.plot(x,sinY,'r--',label="$sin(x)$",linewidth=2)
plt.plot(x,cosY,label="$cos(x*2)$",color = "blue")
plt.plot(x, tanY,'--', label = "$tan(x)$", color = "green")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-10.2,10.2)
plt.legend()
plt.show()