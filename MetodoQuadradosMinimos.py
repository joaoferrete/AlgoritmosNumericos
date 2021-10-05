"""
    Implementação do método dos quadrados minimos
    Para ajuste de reta, utilizando equação para achar os coeficientes da reta.
"""

import sympy
import matplotlib.pyplot as plt

x = sympy.Symbol('X')

def quadradosMin(n, vetx, vety, m=x):
    """ Implementação do método dos quadrados mínimos """

    somax=0
    somay=0
    somaxq=0
    somaxy=0
    for i in range(0,n):
        somax=somax+vetx[i]
        somay=somay+vety[i]
        somaxq=somaxq+(vetx[i]**2)
        somaxy=somaxy+(vetx[i]*vety[i])
    b=((somax*somay)-n*somaxy)/((somax**2)-n*somaxq)
    a=(somay-b*somax)/n
    result=b*m+a
    return result, b, a

def imprimegraf(n, vetx, vety):     
    """ Função que imprime os gráficos """

    plt.title("Pontos inseridos")
    plt.plot(vetx, vety, "o", color='red')
    plt.show()
    result, b, a = quadradosMin(n, vetx, vety)
    print("\n\nA equação da reta a partir do método é: ", result, "\n\n")
    x=abs((vetx[0]-vetx[n-1]))
    for i in range(1, n-1):
        if abs((vetx[i]-vetx[i+1]))<x: x=abs(vetx[i]-vetx[i+1])
    maior=abs(vetx[0])
    menor=abs(vetx[0])
    for i in range(0, n):
        if abs(vetx[i])<menor: menor=abs(vetx[i])
        if abs(vetx[i])>maior: maior=abs(vetx[i])
    x=x/10
    vet1x=[0.0]*2
    vet1y=[0.0]*2
    vet1x[0]=menor
    vet1y[0]=b*vet1x[0]+a
    vet1x[1]=maior
    vet1y[1]=b*vet1x[1]+a
    plt.title("Gráfico da Reta")
    plt.plot(vetx, vety, "o", color='blue')
    plt.plot(vet1x, vet1y, color='green')
    plt.show()
    return

def calculaD(n, vetx, vety ): 
    """ Função que calcula o desvio """

    x, b, a=quadradosMin(n, vetx, vety)
    soma=0
    for i in range(0, n):
        soma=soma+(vety[i]-(b*vetx[i]+a))**2
    return soma

def qualidade(n, vetx, vety): 
    """ Função que calcula a qualidade do ajuste """

    x, b, a=quadradosMin(n, vetx, vety)
    s1=0
    s2=0
    s3=0
    for i in range(0, n):
        s1=s1+(vety[i]-a-b*vetx[i])**2
        s2=s2+vety[i]**2
        s3=s3+vety[i]
    s3=s3**2
    r2=1-(s1/(s2-(1/n)*s3))
    return r2

def main():

    #INSIRA AQUI OS PONTOS
    vetx=[0.3, 2.7, 4.5, 5.9, 7.8]              #Vetor dos valores de X
    vety=[1.8, 1.9, 3.1, 3.9, 3.3]              #Vetor dos valores de y
    #----------------------------------------------------------------------

    imprimegraf(len(vetx), vetx, vety)
    print("\nDeseja avaliar a reta em um ponto específico? ")
    print("1 - Sim")
    print("2 - Não")
    op=int(input())
    while(op!=1 and op!=2): op=int(input())
    if op==2: op=4
    while True:
        while(op==1):
            x=float(input("Qual o valor de x que deseja verificar? "))
            a, b, c=quadradosMin(len(vetx), vetx, vety, x)
            print("O valor da função (y) no ponto ", x, "é: ", a)
            print("\nDeseja avaliar a reta em um outro ponto? ")
            print("1 - Sim")
            print("2 - Não")
            op=int(input())
            while(op!=1 and op!=2): op=int(input())
            if op==2: op=15
        if (op==2):  print("\nO Desvio é: ", calculaD(len(vetx), vetx, vety))
        elif (op == 3): 
            qj=qualidade(len(vetx), vetx, vety)
            print("\nA qualidade do ajuste é:",qj, " Ou ", qj*100, "%" )
        elif op==0: return
        print("\n1 - Avaliar a reta em um ponto")
        print("2 - Calcular o desvio")
        print("3 - Qualidade do Ajuste")
        print("0 - Sair")
        op=int(input())
        while(op<-1 or op>4): op=int(input())
    return

main()