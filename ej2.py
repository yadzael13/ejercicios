json_fire={
    "classifications": [
        {
            "code": "",
            "features": [
                {
                    "code": "",
                    "comparable": False,
                    "featureUnit": {
                        "name": "Minutos",
                        "symbol": "min",
                        "unitType": "310"
                    },
                    "featureValues": [
                        {
                            "value": "40"
                        }
                    ],
                    "name": "",
                    "range": False
                },
                {
                    "code":"",
                    "comparable": False,
                    "featureUnit": {
                        "name": "Minutos",
                        "symbol": "min",
                        "unitType": "310"
                    },
             "featureValues": [
                        {
                            "value": "30"
                        }
                    ],
                    "name": "",
                    "range": False
                }
            ],
            "name": "Tiempos"
        }
    ],
    "images": [
        {
            "altText": "",
            "format": "product",
            "imageType": "PRIMARY",
            "originalImageCode": "",
            "url": ""
        },


    ]
    }
json_nuevo={

    "classifications": [
        {
            "code": "123",
            "features": [
                {
                    #"code": "",
                    "comparable": 213123,
                    "featureUnit": {
                        "name": "11111",
                        "symbol": "a11111",
                        "unitType": "sadasd"
                    },
                    "featureValues": [
                        {
                            "value": "123123"
                        }
                    ],
                    "name": "12323",
                    "range": True
                },
                {
                    "code":"",
                    "comparable": False,
                    "featureUnit": {
                        "name": "Minutos",
                        "symbol": "min",
                        "unitType": "310"
                    },
             "featureValues": [
                        {
                            "value": "30"
                        }
                    ],
                    "name": "",
                    "range": False
                }
            ],
            "name": "Tie12323mpos"
        }
    ],
    "vendor": {
    "categoriesFood": [
            {
                "id": "111111111",
                "name": "111111111"
            },
            {
                "id": "111111111",
                "name": "111111111"
            }
        ],
        "code": "111111111",
        "name": "111111111"
    },
        "images": [
            {
                "altText": "1111111111",
                #"format": "1111111111",
                "imageType": "1111111111",
                "originalImageCode": "1111111111",
                "url": "1111111111"
            },
                        {
                            "altText": "2",
                            #"format": "1111111111",
                            "imageType": "2",
                            "originalImageCode": "2",
                            "url": "2"
                        }
        ]
}
def update_product(new, exis):

    #en caso de listas ...
    def case_list(list, empty_dict):

        ret_list = []
        if len(list) > 1:
            breakpoint()
            for x in list:
                index = list.index(x)
                a = update_product(list[index], empty_dict)
                ret_list.append(a)
        elif len(list) == 1:

            ret_list = [update_product(list[0], empty_dict)]
        elif len(list) == 0:
            print("empty_body, returning empty dict weird")
        return ret_list
    #filtro para saber el tipo, y si es vacio, 0 o array vacio
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
    for el in new:
        if el in exis:
            if type(new[el]) == type(exis[el]):
                validate = filter_type(new[el])
                if validate == 0:
                    print(f"{el} is empty, not change")
                    continue
                elif validate == 1:
                    exis[el] = new[el]
                elif validate == 2:
                    try:
                        exis[el] = update_product(new[el], exis[el])
                    except:
                        continue
                elif validate == 3:
                    ls = []
                    ls.append(exis[el][0])
                    if len(new[el]) == len(exis[el]):
                        exis[el] = case_list(new[el], ls[0])
                    else:
                        long1 = len(exis[el])
                        exis[el] = case_list(new[el], ls[0])
                        while len(exis[el]) < long1:
                            exis[el].append(ls[0])

            else:
                print(f"{el} is not the same data type of given body")
        else:
            print(f"{el} is not in given body")
    return exis
print(update_product(json_nuevo, json_fire))
