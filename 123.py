import os

def create_dict_from_file( file_name):

    file_path = os.path.abspath(os.path.join(file_name))
    cook_dict = {}
    with open(file_path, encoding='utf8') as file_work:
        for line in file_work:
            dish_name = line.strip()
            counter = int(file_work.readline())
            list_of_ingridient = []
            for i in range(counter):
                temp_dict = {}
                ingridient = file_work.readline().lower()
                ingridient = ingridient.strip().split('|')
                temp_dict['ingridient_name'] = ingridient[0].strip()
                temp_dict['quantity'] = int(ingridient[1])
                temp_dict['measure'] = ingridient[2].strip()
                list_of_ingridient.append(temp_dict)
            cook_dict[dish_name] = list_of_ingridient
            file_work.readline()
    return cook_dict

print(create_dict_from_file('recipes.txt'))


def get_shop_list_by_dishes (dish_list,person_count):

    shop_dict = {}
    for dish in dish_list:
        for ingridients in create_dict_from_file('recipes.txt')[dish]:
            temp_dict = {}
            temp_dict['measure'] = ingridients['measure']
            temp_dict['quantity'] = int(ingridients['quantity'])* int(person_count)
            shop_dict.setdefault(ingridients['ingridient_name'],temp_dict)

    return shop_dict

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


def amount_str(file_name):
    file_path = os.path.abspath(os.path.join(file_name))
    with open(file_path, encoding='utf8') as file_work:
        return len(file_work.readlines())


def read_file(file_name):
    file_path = os.path.abspath(os.path.join(file_name))
    with open(file_path, encoding='utf8') as file_work:
        return file_work.read()


file_list = []

dict = {}
elements_sorted = {}
file_list.append(elements_sorted.keys())
file_name = ['1.txt', '2.txt', '3.txt']
for file in file_name:
    dict.setdefault(file, amount_str(file))
elements_sorted = {k: dict[k] for k in sorted(dict, key=dict.get, reverse=False)}
file_for_write = []
file_for_write.extend(elements_sorted.keys())
print(elements_sorted)
for file in file_for_write:
    text = read_file(file)
    text_2 = amount_str(file)
    with open('15.txt', 'a') as f:
        f.write(f'{file}' '\n' f'{text_2}' '\n' f'{text}' '\n')