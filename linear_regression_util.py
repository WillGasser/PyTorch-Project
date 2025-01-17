import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 10, 50)  # 50 points between 0 and 10
y = 2 * x + 3 + np.random.normal(0, 2, size=x.shape)  

m = 0  # Initial slope
b = 0  # Initial intercept

# Set learning rate and number of iterations
learning_rate = 0.01
iterations = 100

plt.ion()


