from pprint import pprint


with open('recipes.txt', 'rt', encoding='utf-8') as f:
    ingridients = {}
    for line in f:
        dish_name = line.strip()
        ingridients_count = int(f.readline())
        ingridient = []
        for i in range(ingridients_count):
            ingredient_name, quantity, measure = f.readline().strip().split(' | ')
            ingridient.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        ingridients[dish_name] = ingridient


def get_shop_list_by_dishes(dishes, person_count):
    resultdict = {}
    for dish in dishes:
        if dish in ingridients:
            for ing in ingridients[dish]:
                if ing['ingredient_name'] not in resultdict:
                    value = {'quantity': int(ing['quantity']) * person_count, 'measure': ing['measure']}
                    resultdict[ing['ingredient_name']] = value
                else:
                    resultdict[ing['ingredient_name']]['quantity'] += int(ing['quantity']) * person_count
    return resultdict


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))