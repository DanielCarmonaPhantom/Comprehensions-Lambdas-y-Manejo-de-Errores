from ast import Try


def divisors(num: int):
    try:
        if num <0:
            raise ValueError("No se puede ingresar números negativos")
        divisors = []
        for i in range(1, num):
            # breakpoint()
            if num % i ==0:
                divisors.append(i)
        return divisors

    except ValueError as ve:
        print(ve)
    
    

def run():
    try:
        numero = int(input("Dame un numero"))        
        print(divisors(numero))
        print("Termino mi programa")
    except ValueError:
        print("Debes ingresar un Número")

if __name__ == '__main__':
    run()