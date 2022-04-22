def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {
        'firtname': "Daniel",
        'lastname': "Carmona"
    }

    super_list = [
        {
            'firtname': "Daniel",
            'lastname': "Carmona"
        },
        {
            'firtname': "Juan",
            'lastname': "Modelo"
        },
        {
            'firtname': "Susan",
            'lastname': "Hernandez"
        }
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1, -2, 0 , 1 , 2],
        "floating_nums": [1.1, 4,4, 6,78]
    }

    for key, value in super_dict.items():
        print(key, " - ", value)
    
    for person in super_list:
        print(person)

if __name__ == '__main__':
    run()