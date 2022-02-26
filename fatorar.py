def fatorar_um_numero(numero):
    indice = 0
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 69, 61, 67, 71, 73, 79, 83, 89, 97,
              101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
              211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
              307, 311, 313]
    while numero > 1:
        var = numero % primos[indice]
        if var == 0:
            print(numero, " | ", primos[indice])
            numero = numero / primos[indice]
        else:
            indice += 1
    print("1.0 | 1")
    print("0.0")
            
def iniciar():
    print("*****************")
    print("Fatorar um número")
    print("*****************")

    num = float(input("Informe um número inteiro para fatorar: "))
    fatorar_um_numero(num)

if __name__ == "__main__":
    iniciar()



