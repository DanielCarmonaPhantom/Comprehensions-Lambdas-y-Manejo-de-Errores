from numpy import number


def read():
    numbers = []
    with open('./assets/numbers.txt', "r", encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Daniel", "Miguel", "Pepe", "Saul"]
    with open('./assets/names.txt', "w", encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write("\n")



def run():
    read()
    write()




if __name__ == '__main__':
    run()