import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)
y = x**2 - 4*x + 4

plt.plot(x, y, label='$f(x) = x^2 - 4x + 4$', color='blue')
plt.title('Kvadratik funksiya grafigi')
plt.xlabel('x o\'qi')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

x = np.linspace(0, 2 * np.pi, 100)

plt.plot(x, np.sin(x), 'r--', marker='o', markevery=10, label='Sin(x)')
plt.plot(x, np.cos(x), 'g-.', marker='s', markevery=10, label='Cos(x)')
plt.title('Sinus va Kosinus funksiyalari')
plt.legend()
plt.show()


x = np.linspace(0.1, 5, 100)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, x**3, 'r')
axs[0, 0].set_title('$x^3$')

axs[0, 1].plot(x, np.sin(x), 'g')
axs[0, 1].set_title('sin(x)')

axs[1, 0].plot(x, np.exp(x), 'b')
axs[1, 0].set_title('$e^x$')

axs[1, 1].plot(x, np.log(x + 1), 'm')
axs[1, 1].set_title('log(x+1)')

plt.tight_layout()
plt.show()


x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.scatter(x, y, c='purple', marker='*', alpha=0.6)
plt.title('Tasodifiy nuqtalar (Scatter Plot)')
plt.xlabel('X qiymatlari')
plt.ylabel('Y qiymatlari')
plt.grid(True)
plt.show()


data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Normal taqsimot gistogrammasi')
plt.xlabel('Qiymat')
plt.ylabel('Chastota')
plt.show()


from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)

surf = ax.plot_surface(X, Y, Z, cmap='viridis')
fig.colorbar(surf)
ax.set_title('$f(x, y) = \cos(x^2 + y^2)$')
plt.show()


products = ['A', 'B', 'C', 'D', 'E']
sales = [200, 150, 250, 175, 225]

plt.bar(products, sales, color=['red', 'blue', 'green', 'yellow', 'orange'])
plt.title('Mahsulotlar savdosi')
plt.ylabel('Savdo hajmi')
plt.show()


labels = ['T1', 'T2', 'T3', 'T4']
cat_a = [10, 15, 12, 18]
cat_b = [12, 10, 15, 13]
cat_c = [8, 12, 10, 15]

plt.bar(labels, cat_a, label='Category A')
plt.bar(labels, cat_b, bottom=cat_a, label='Category B')
plt.bar(labels, cat_c, bottom=np.array(cat_a)+np.array(cat_b), label='Category C')

plt.title('Vaqt bo\'yicha kategoriyalar hissasi')
plt.legend()
plt.show()
