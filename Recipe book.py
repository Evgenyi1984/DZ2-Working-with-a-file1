from pprint import pprint

def read_recipes(filename):
    cook_book = {}
    with open(filename, 'r') as f:
        while True:
            recipe_name = f.readline().strip()
            if not recipe_name:
                break
            ingredient_count = int(f.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_line = f.readline().strip()
                ingredient_info = ingredient_line.split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_info[0],
                    'quantity': int(ingredient_info[1]),
                    'measure': ingredient_info[2]
                }
                ingredients.append(ingredient)
            cook_book[recipe_name] = ingredients
            f.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        ingredients = cook_book.get(dish)
        if ingredients:
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
    shop_list = dict(sorted(shop_list.items(), key=lambda x: x[0]))
    return shop_list


# Задание 1
print('Задание 1:')
filename = 'recipes.txt'
cook_book = read_recipes(filename)
pprint(cook_book)
# Задание 2.py
print('Задание 2.py:')
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count)
pprint(shop_list)
