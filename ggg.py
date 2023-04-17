import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.cos(x*x) + 3*x

def df(x):
    return -2*x*np.sin(x)**2 + 3

x0 = 1

a = -37.7
b = 37.7

max_iterations = 10
eps = 1e-6


x_values = [x0]


for i in range(max_iterations):
    x_new = x_values[-1] - f(x_values[-1])/df(x_values[-1])
    x_values.append(x_new)
    
    if abs(x_new - x_values[-2]) < eps and x_new >= a and x_new <= b:
        break

results = np.array(x_values)
print('Результаты итерации метода Ньютона:')
print(results)

x = np.linspace(a, b, 1000)
plt.plot(x, f(x), label='f(x)')
plt.plot(x_values, f(np.array(x_values)), 'o', label='x - Ньютон')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()







def g(x):
    return np.cos(x*x) + 3*x


x0 = 1
max_iter = 50


x_values = [x0]
errors = []

for i in range(max_iter):
    x_new = g(x_values[-1])
    error = np.abs(x_new - x_values[-1])
    x_values.append(x_new)
    errors.append(error)
    if error < 1e-6:
        break

print(f"Найденный корень: {x_values[-1]}")
print(f"Количество итераций: {len(x_values)-1}")


fig, ax = plt.subplots(figsize=(8, 6))
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.plot(x_values, 'bo-')
ax.set_xlabel("Номер итерации")
ax.set_ylabel("Приближение корня")
ax.set_title("Метод итерации: приближение корня")


fig, ax = plt.subplots(figsize=(8, 6))
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.plot(errors, 'ro-')
ax.set_xlabel("Номер итерации")
ax.set_ylabel("Ошибка")
ax.set_title("Метод итерации: ошибка приближения")

plt.show()

