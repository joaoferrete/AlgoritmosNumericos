"""
    Implementação do método de substituição sucessiva
    para resolver sistemas de equações lineares
"""

def matriz (n):
    """ Função que faz a criação da Matriz """
    x=[0]*n
    for i in range (0, n):
        x[i] = [0]*n
    for i in range(0, n):
        for j in range (0, n):
            x[i][j] = 0.0
    return x

def vetor (n):
    """ Função que cria um vetor de tamanho N """
    x=[0]*n
    for i in range(0, n):
        x[i]=0.0
    return x

def substituicaosuc (n, matriz, c):
    """ Implementação do Método """
    x=vetor(n)
    x[0] = c[0]/matriz[0][0]
    for i in range(1, n):
        soma=0
        for j in range(0, i):
            soma=soma+matriz[i][j] * x[j]
        x[i] = ((c[i] - soma)/matriz[i][i])
    return x

def main():
    n= int(input("Numero de termos: "))
    mat = matriz(n)
    c = vetor(n)
    print("Insira os termos da matriz:")
    for i in range (0, n):
        for j in range (0, n):
            mat[i][j] = float(input())
    print("Insira os termos do vetor independente:")
    for i in range (0, n):
        c[i] = float(input())
    x = substituicaosuc(n, mat, c)
    print("[", end=" ")
    for i in range (0, n):
        print(x[i], end="  ")
    print("]")
    return

main()


#    MATRIZ UTILIZADA PARA TESTE:
#    |  1 0 0 | |X1|    | 11 |
#    | -2 1 0 | |X2| =  |-15 |
#    |  4 3 1 | |X3|    | 29 |
#    Resultado Esperado: [11, 7, -36]