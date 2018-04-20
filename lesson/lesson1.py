#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
x = []
for i in range(-20, 0):
    x.append(i)

for i in range(1, 10):
    x.append(i)

ax = plt.gca()
ax.spines['left'].set_color('blue')
ax.spines['bottom'].set_color('red')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
plt.xlabel('x')
plt.ylabel('y')
y = np.array(x)
plt.plot(y, 2*y)
plt.show()