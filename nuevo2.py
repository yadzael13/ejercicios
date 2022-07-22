json_existente = {
	'statusPromocion': False,
	'images': {
		'thumbnail': '',
		'product': ''
	},
	'currency': '',
	'id': '',
	'score': 0,
	'stockDisponible': False,
	'imageProductCarousel': '',
	'category': '',
	'promocion_Producto': {},
    "url": "",
    "vendor": {
        "categoriesFood": [
            {
                "id": "111",
                "name": "1111"
            },
            {
                "id": "111111",
                "name": "1111"
            }
        ],
        "code": "11111",
        "name": "11111"
    },
    "warranty": "",
	'descriptionHTML': '',
	'name': '',
	'amount': '',
	'description': ''
}
json_nuevo={
    'statusPromocion': False,
	'images': {
		'thumbnail': 123321,
		#'product': '897'
        "qwe" : 213
	},

     #'descriptionHTML': '',
     #'name': '',
     #'amount': '',
     'description': 'papas',
     "vendor": {
         "categoriesFood": [
             {
                 "id": "222222",
                 "name": "22222",
                 "sadasd": "123"
             },
             {
                 "id": "222222",
                 "name": "222222"
             }
         ],
         "code": "2222222",
         "name": "2222222"
     },

}
def filter_type(param):
    error_array = ["", 0, 0.0,[],{}]
    if (isinstance(param, str) or isinstance(param, bool) or isinstance(param, int) or isinstance(param, float)) and param not in error_array:
        return 1
    elif isinstance(param, dict) and param not in error_array:
        return 2
    elif isinstance(param, list) and param not in error_array:
        return 3
    else:
        return 0 # ya sirve
def dict_return(dict_pass, dict_body):
    for x in dict_pass:
        if x in dict_body:
            if type(dict_pass[x]) == type(dict_body[x]):
                validate = filter_type(dict_pass[x])
                if validate == 1:

                    dict_body[x] = dict_pass[x]
                    continue
                if validate == 2:
                    dict_body[x] = dict_return(dict_pass[x], dict_body[x])
                    continue
                elif validate == 3:
                    dict_body[x] = dict_pass[x]
                    continue
            else:
                print(f"{x} is not the same type of given body -- (dict_return funct)")
        else:
            print(f"{x} is not in given body -- (dict_return funct)")
        return dict_body


def productos_update(nuevo, existente):

    for el in nuevo:
        #valida si existe
        try:
            if el in existente:
                #valida que sea del mismo tipo
                if type(nuevo[el]) == type(existente[el]):
                    validate = filter_type(nuevo[el])
                    #si es asignable, lo asignar
                    if validate == 1:
                        existente[el] = nuevo[el]
                        continue
                    elif validate == 2:
                        breakpoint()
                        existente[el] = dict_return(nuevo[el], existente[el])
                        continue
                    elif validate == 3:

                        for el_2 in nuevo[el]:
                            validate = filter_type(el_2)
                            pos_el2 = nuevo[el].pos(el_2)
                            if validate == 2:
                                existente[el].append( dict_return(nuevo[el],existente[el][0]))
                            else:
                                existente[el][pos_el2] = nuevo[el][pos_el2]
                                continue
                    else:
                        print(f"Not changes for {el}")
                        continue
                else:
                    print(f"{el} is not the same data type in given body")
                    continue
            else:
                print(f"{el} not exists on given body")
        except:
             continue
    return existente

print(productos_update(json_nuevo, json_existente))
