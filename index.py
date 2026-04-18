import numpy as np 
import matplotlib.pyplot as plt 

# Linalg solve dimana sebuah Solusi dari Suatu matriks dimana X digambarkan sebagai coeficient matriks

# a = np.array([[1, 2], [3, 5]])
# b = np.array([1, 2])
# x = np.linalg.solve(a, b)

# print(x)

class Solution: 

    def __init__(self, a, b, c=None):
        self.a = np.array(a) 
        self.b = np.array(b) 

    def SistemPersamaanLinear2(self):
        hasil = np.linalg.solve(self.a, self.b)
        return hasil

H1 = Solution([[2, 1], [1, 2]], [3, 7])

x, y = H1.SistemPersamaanLinear2()
plt.plot(x, y)
plt.show()