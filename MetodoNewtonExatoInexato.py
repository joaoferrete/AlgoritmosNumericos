"""

    Implementação dos métodos de Newton Exato e Inexato
    para resolução de equações diferenciais

"""

import numpy as np

#Definição das funções a serem utilizadas
def f1(x): return x[0]**2 + x[1]**2 + x[2]**2 -1
def f2(x): return 2*x[0]**2 + x[1]**2 - 4*x[2] 
def f3(x): return 3*x[0]**2 - 4*x[1] + x[2]

def calculaJacobiano(x):
    return [[2*x[0], 2*x[1], 2*x[2]],
            [4*x[0], 2*x[1], -4],
            [6*x[0], -4, 1]]

def prodInterno(x, j):
    return np.dot(x, j)

def calculaInversa(mat):
    return np.linalg.inv(mat)

def calculaFX(x):
    return np.array([f1(x), f2(x), f3(x)])

def calculaErro(x, xk):
    return max(abs(xk - x))

def verifErro(epsilon, x):
    err = calculaFX(x)
    return abs(err[0]) < epsilon and abs(err[1]) < epsilon and abs(err[2]) < epsilon

def NExato():
    """
        Implementação do método de Newton Exato
    """
    x = [0.5, 0.5, 0.5] #Vetor de aproximação inicial
    epsilon = 0.0001    #Erro máximo
    k = 0
    
    while(not verifErro(epsilon, x)):
        j = calculaJacobiano(x)
        x = x - prodInterno(calculaInversa(j), calculaFX(x))
        k += 1
        print(f"X{k} = {x}")


    print(f"\n\nErro: {calculaFX(x)}")
    print("Melhor Solução: ", x)

def NInexato():
    """
        Implementação do método de Newton Inexato
    """
    x = [0.5, 0.5, 0.5] #Vetor de aproximação inicial
    x0 = calculaJacobiano(x)
    epsilon1 = 0.0001 #Erro máximo
    epsilon2 = epsilon1 #Erro máximo
    k=0
    error=True

    while not verifErro(epsilon1, x):
        xk = x
        fx = calculaFX(x)
        s = np.linalg.solve(x0, -fx)
        x = x + s
        k=k+1
        print(f"X{k} = {x}")

        if calculaErro(x, xk) < epsilon2:
            print("\n\nErro:", calculaErro(xk, x))
            error = False
            break
    
    if error: print("\n\nErro:", calculaFX(x))
    print(f"Melhor Solução = {x}")

print("-----Metodo de Newton Exato-----\n")
NExato()
input("\nAperte ENTER para o próximo Método\n")
print("-----Metodo de Newton Inexato-----\n")
NInexato()