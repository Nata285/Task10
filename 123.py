with open('recipes.txt', 'r', encoding = 'utf-8') as file_work:
    cook_book = {}

    for line in file_work:
        dish_name = 0
        counter = 0
        list_of_ingridient =[]

        if line.strip().isdigit() == False and line.strip() != '' and line.strip().__contains__('|') == False:
            dish_name=line.strip()

        elif line.strip().isdigit() == True:
            counter += int(line.strip())+3
        elif line.strip().__contains__('|') == True:
            for i in
            temp_dict = {}
            temp_dict.setdefault('ingredient_name',line.strip())
            list_of_ingridient.append(temp_dict)

        elif line.strip() == '': break
        cook_book.setdefault(dish_name, list_of_ingridient)
        print(cook_book)

