"""
    Função que calcula o maior autovalor de uma matriz
"""


import numpy as np

def calculaErro(alpha2, alpha):
    return abs(alpha2 - alpha)/alpha2

#Insira a matriz Aqui
A = [[1, 2, 1],
     [-1, 3, 1],
     [0, 2, 2]]

#Insira a aproximação inicial aqui
y0 = [1, 1, 1]

i = 1
z1 = np.dot(A, y0)
alpha = abs(max(z1, key=abs))
y1 = np.dot(1/alpha, z1)
print("Iteração:", i)
print("Yi =", y1)
print("Alpha:", alpha, "\n")

while(True):
    i+=1
    z2 = np.dot(A, y1)
    alpha2 = abs(max(z2, key=abs))
    y2 = np.dot(1/alpha2, z2)

    print("Iteração:", i)
    print("Yi =", y2)
    print("Alpha:", alpha2 , "\n")

    if(calculaErro(alpha2, alpha) < 0.00001): break
    y1 = y2
    alpha = alpha2
    