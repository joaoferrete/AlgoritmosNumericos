"""
    MÉTODO PARA ENCONTRAR AUTOVALORES DE UMA MATRIZ DADA
"""


import math as m
import numpy as np

def maxDiag(m, epsilon):
    """ FUNÇÃO QUE VERIFICA A CONDIÇÃO DE PARADA """
    return abs(m[1][0]) > epsilon or abs(m[2][0]) > epsilon or abs(m[2][1]) > epsilon

def autoValores(m):
    """ Função que cria o vetor com os autovalores """
    return [m[0][0], m[1][1], m[2][2]]

#Insira a Matriz aqui
A = [[1, 2, 1],
     [-1, 3, 1],
     [0, 2, 2]]

B = A

#Insira o limitante para o erro aqui
epsilon = 0.0001

s = c = R = Q = U = 0
 
i = 0

while maxDiag(A, epsilon):
    i+=1

    if abs(A[1][0]) != 0 and maxDiag(A, epsilon):
        s = A[1][0] / m.sqrt(A[1][0]**2 + A[0][0]**2)
        c = A[0][0] / m.sqrt(A[1][0]**2 + A[0][0]**2)
        U = [[c, s, 0],
             [-s, c, 0],
             [0, 0, 1]]
        R = np.dot(U, A)
        Q = np.transpose(U)
        A = np.dot(R, Q)

    if abs(A[2][0]) != 0 and maxDiag(A, epsilon):
        s = A[2][0] / m.sqrt(A[2][0]**2 + A[0][0]**2)
        c = A[0][0] / m.sqrt(A[2][0]**2 + A[0][0]**2)
        U = [[c, 0, s],
             [0, 1, 0],
             [-s, 0, c]]

        R = np.dot(U, A)
        Q = np.transpose(U)
        A = np.dot(R, Q)
             
    if abs(A[2][1]) != 0 and maxDiag(A, epsilon):
        s = A[2][1] / m.sqrt(A[2][1]**2 + A[1][1]**2)
        c = A[1][1] / m.sqrt(A[2][1]**2 + A[1][1]**2)
        U = [[1, 0, 0],
             [0, c, s],
             [0, -s, c]]
        
        R = np.dot(U, A)
        Q = np.transpose(U)
        A = np.dot(R, Q)

        
    print("Iteração: ", i)
    print(A, "\n")



print("AUTOVALORES:", autoValores(A))
print("Resultado Exato:", np.linalg.eigvals(B))
