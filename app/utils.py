import requests
import json

def get_data():
    pk_list= []
    for i in [10, 15, 22, 34, 36, 44, 56, 76]:
        r = requests.get('https://pokeapi.co/api/v2/pokemon/{id}'.format(id=str(i)))
        pk = json.loads(r.text)
        pk_tmp = {
            'name': pk['name'],
            'height': pk['height'],
            'weight': pk['weight'],
            "image": pk['sprites']['front_default']
        }
        pk_list.append(pk_tmp)

    return pk_list
