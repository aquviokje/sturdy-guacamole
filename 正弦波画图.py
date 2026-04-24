import numpy as np
import matplotlib.pyplot as plt
# ⽣成⼀个简单的正弦波信号
t = np.linspace(0, 10, 1000)
y = np.sin(2 * np.pi * t)
plt.figure(figsize=(8, 4))
plt.plot(t, y)
plt.title("Sine Wave Signal Test")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

