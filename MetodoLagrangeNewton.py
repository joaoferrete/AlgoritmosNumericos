"""
    Implementação do método de Lagrange e de Newton
    para interpolação de funções a partir de vetores dados
"""

import sympy
x = sympy.Symbol('X')

def lagrange(n, vetx, vety, x, verif=0):        
    """ Função de interpolação a partir do método de LaGrange """

    vet = [0.0]*n
    soma=0
    for i in range(0, n):
        prod=1
        for j in range(0, n):
            if i!=j:
                prod=prod*(x-vetx[j])/(vetx[i]-vetx[j])
        soma=soma+vety[i]*prod
        vet[i] = prod*vety[i]
    if verif == 0: print("O polinômio é: " ,sympy.expand(soma))
    else: print("O resultado da interpolação no ponto", x, "é: ", soma)
    return soma

def opDif(n, vetx, vety):                      
    """ Função de calculo da matriz de operadores de diferença """

    mat = [0]*n
    for i in range(0, n):
        mat[i] = [0]*n
        mat[i][0] = vety[i]
    for i in range(1, n):
        for k in range(0, n-i):
            mat[k][i] = (mat[k+1][i-1] - mat[k][i-1])/(vetx[k+i] - vetx[k])
    return mat

def Newton(n, vetx, vety, ponto, verif=0):   
    """ Função de interpolação a partir do método de Newton """

    soma=0
    if ponto != x: verif =1
    mat=opDif(n, vetx, vety)
    for i in range(0, n):
        prod=1
        for k in range(0, i):
            prod=prod*(ponto-vetx[k])
        prod=prod*mat[0][i]
        soma=soma+prod
    if verif == 0: print("O polinômio é: ", sympy.expand(soma))
    else: print("O resultado da interpolação no ponto ", ponto, " é: ", soma)

    return soma

def erro(n, vetx, vety, ponto, qtd, vetx1, vety1): 
    """ Função de calculo do limitante para o erro """
    
    mat = opDif(qtd, vetx1, vety1)
    prod=1
    maior=0
    for i in range (0, n): 
        prod=prod*(ponto-vetx[i])
    if qtd==n: n=n-1
    for i in range(0, qtd): 
        if maior<abs(mat[i][n]): maior = abs(mat[i][n])
    prod=abs(prod*maior)
    print("O limitante para o erro é: ", prod)
    return prod

def main():         
    vetx = [0.2, 0.34, 0.4, 0.52, 0.6, 0.72]              #Vetor de coordenadas em X
    vety = [0.16, 0.22, 0.27, 0.29, 0.32, 0.37]           #Vetor de coordenadas em Y

    while True:
        g=int(input("Qual o grau do polinômio que deseja determinar?  "))
        if g<len(vetx)-1:
            g=g+1
            vetx1=[0]*g
            vety1=[0]*g
            print("Não é possivel determinar um polinômio com esse grau!")
            print("Escolha ", g,  "pontos para continuar: ")
            k=0
            for i in range(0, len(vetx)):
                print(i+1, " - (", vetx[i], ",", vety[i], ")")
            print("\n")
            while k<g :
                e=int(input())
                vetx1[k] = vetx[e-1]
                vety1[k] = vety[e-1]
                k=k+1
        elif g>len(vetx)-1:
            print("Não é possivel determinar um polinômio com esse grau! ")
        else:
            vetx1=vetx
            vety1=vety
            g=g+1
        print("Deseja interpolar em um ponto específico? ")
        print("1 - Sim")
        print("2 - Não")
        inter = int(input())
        if inter ==1:
            ponto = float(input("Digite o valor do ponto: "))
        while True :
            print("\nQual método deseja utilizar? ")
            print("1 - LaGrange")
            print("2 - Newton")
            if inter==1: print("3 - Calcular apenas o erro")
            print("9 - Interpolar em outro ponto")
            print("0 - Sair")
            op=int(input())
            if op==0: return
            elif op==1:
                print("\n")
                print("Método LaGrange")
                lagrange(g, vetx1, vety1, x)
                if inter==1: lagrange(g, vetx1, vety1, ponto, 1)
            elif op==2:
                print("\n")
                print("Método de Newton")
                Newton(g, vetx1, vety1, x);
                if inter==1: 
                    Newton(g, vetx1, vety1, ponto)
                    erro(g, vetx1, vety1, ponto,len(vetx), vetx, vety)
            elif op ==3:
                print("\n")
                print("Calculo do erro:")
                if inter==1: erro(g, vetx1, vety1, ponto,len(vetx), vetx, vety)
                else: print("Não foi definido um ponto! ")
            elif op==9:
                break

    return
            
main()


#         VETORES TESTADOS
#   vetx = [-1, 0, 2]
#   vety = [4, 1, -1]

#   vetx = [-1, 0, 3, 4, 2]
#   vety = [4, 1, 4, 5, -1]

#   vetx = [-1, 0, 1, 2, 3]               
#   vety = [1, 1, 0, -1, -2]

#   vetx = [0.2, 0.34, 0.4, 0.52, 0.6, 0.72]              
#   vety = [0.16, 0.22, 0.27, 0.29, 0.32, 0.37]

#   vetx = [0.7, 1.2, 1.3, 1.5, 2.0, 2.3, 2.6]                         
#   vety = [0.043, 1.928, 2.497, 3.875, 9, 13.467, 19.176]