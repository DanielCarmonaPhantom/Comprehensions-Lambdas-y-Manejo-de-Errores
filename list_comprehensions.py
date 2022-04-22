def run():
    # squares = []
    # for i in range(1,20):
    #     if i % 3 !=0:
    #         squares.append(i**2)

    # print(squares)

    squares_comprenhension = [i**2 for i in range(1,101) if i % 3 != 0]
    print(squares_comprenhension)



if __name__ == '__main__':
    run()