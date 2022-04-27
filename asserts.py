from ast import Try


def divisors(num: int):
    assert num < 0, "No puede ser negativo"
    divisors = []
    for i in range(1, num):
            # breakpoint()
        if num % i ==0:
            divisors.append(i)
    return divisors

    

def run():
    numero = input("Dame un numero ") 
    assert numero.isnumeric(), "Ingresa un número" 
    print(divisors(int(numero)))
    print("Termino mi programa")


if __name__ == '__main__':
    run()