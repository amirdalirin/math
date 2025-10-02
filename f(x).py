import numpy as np
import matplotlib.pyplot as plt

# تعریف تابع درجه سه
def cubic(a, b, c, d, x):
    return a*x**3 + b*x**2 + c*x + d

# گرفتن ضرایب از کاربر
a = float(input("ضریب a (x³): "))
b = float(input("ضریب b (x²): "))
c = float(input("ضریب c (x): "))
d = float(input("ضریب d (ثابت): "))

# بازه x
x = np.linspace(-10, 10, 500)
y = cubic(a, b, c, d, x)

# رسم نمودار
plt.plot(x, y, label=f"f(x) = {a}x³ + {b}x² + {c}x + {d}")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend()
plt.grid(True)
plt.title("نمودار تابع درجه سه")
plt.show()
