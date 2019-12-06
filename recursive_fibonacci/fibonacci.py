def f(n):
    return n if n <= 1 else f(n-1) + f(n-2)

if __name__ == '__main__':
    for x in range(int(input("Digite um numero para obter o Fibonacci dele: "))):
        print(x, ":", f(x))
    input()