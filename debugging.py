def divisors(num: int):
    divisors = []
    for i in range(1, num):
        # breakpoint()
        if num % i ==0:
            divisors.append(i)
    return divisors


def run():
    numero = int(input("Dame un numero"))
    print(divisors(numero))
    print("Termino mi programa")

if __name__ == '__main__':
    run()