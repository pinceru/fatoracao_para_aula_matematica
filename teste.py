def calculo_equacao():
    print("***********************")
    print("Resolução de polinômios")
    print("***********************")


    x = int(input("X = "))
    y = int(input("Y = ")) 

    s = x + y
    p = x * y

    ###PEGAR O RESTO DA FÓRMULA QUANDO CHEGAR EM CASA, PARA TERMINAR O ALGORITIMO



def fatorar_um_numero(numero, a, b, c):
    indice = 0
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 69, 61, 67, 71, 73, 79, 83, 89, 97]
    while numero > 1:
        var = numero % primos[indice]
        if var == 0:
            numero = numero / primos[indice]
            print(numero)
        else:
            indice += 1
            
            

if __name__ == "__main__":
    fatorar_um_numero(30)





