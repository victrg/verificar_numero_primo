def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        n = int(input("Digite um número de 1 a 100: "))
        if eh_primo(n):
            print(f"{n} é primo.")
        else:
            print(f"{n} não é primo.")
    except ValueError:
        print("Por favor, digite outro número inteiro.")