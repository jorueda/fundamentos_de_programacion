import numpy as np

a = np.array([1 ,2 ,3 ,4 ,5])
print(a)

mat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(mat)

generar = np.arange(10, 30)
print(generar)

tmat = np.transpose(mat)
print(tmat)

iden = np.identity(5)
print(iden)

cero = np.zeros([4, 6])
print(cero)