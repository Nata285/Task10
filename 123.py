with open('recipes.txt', 'r', encoding = 'utf-8') as f:
    lines = f.read().splitlines()
    dict = {}
    for i in enumerate(lines):
        dict.setdefault(i[0], i[1])
    cook_book={}
    dish = 0
    dish_list =[]

    dish_dict = {}


    for index, line in dict.items():
        t = 0
        x = 0
        y = 0
        a = 0
        if index == a:
            dish = line
        if index == a+1:
            t = line
            x = line
            y = line
        dish_dict.setdefault('ingredient_name', t)
        dish_dict.setdefault('quantity', x)
        dish_dict.setdefault('measure', y)
        dish_list.append(dish_dict)
        cook_book.setdefault(dish, dish_list)


    print(dish_dict)
    print(dish)