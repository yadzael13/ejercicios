product = {
    "availableForPickup": False,
    "averageRating": 0.0,
    "baseOptions": [],
    "categories": [
        {
            "code": "",
            "name": "",
            "url": ""
        },
        {
            "code": "",
            "name": "",
            "url": ""
        }
    ],
    "characteristics": "",
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
    "code": "",
    "configurable": False,
    "description": "",
    "galleryImages": [
        {
            "altText": "",
            "format": "zoom",
            "imageType": "PRIMARY",
            "originalImageCode": "",
            "url": ""
        },
        {
            "altText": "",
            "format": "product",
            "imageType": "PRIMARY",
            "originalImageCode": "",
            "url": ""
        },
        {
            "altText": "",
            "format": "thumbnail",
            "imageType": "PRIMARY",
            "originalImageCode": "",
            "url": ""
        },
        {
            "altText": "",
            "format": "superZoom",
            "galleryIndex": 0,
            "galleryQualifier": "",
            "imageType": "GALLERY",
            "url": ""
        },
    ],
    "images": [
        {
            "altText": "",
            "format": "product",
            "imageType": "PRIMARY",
            "originalImageCode": "",
            "url": ""
        }
    ],
    "manufacturer": "",
    "manufacturerName": "",
    "multimedia": {
        "img": "",
        "video": ""
    },
    "name": "",
    "numberOfReviews": 0,
    "offlineDate": "01/01/2020",
    "onlineDate": "01/01/2020",
    "potentialPromotions": [],
    "price": {
        "currencyIso": "MXN",
        "formattedValue": "$",
        "priceType": "BUY",
        "value": 0.0
    },
    "priceRange": {},
    "productReferences": [],
    "purchasable": False,
    "reviews": [],
    "sku": "",
    "stock": {
        "stockLevel": 0,
        "stockLevelStatus": ""
    },
    "summary": "",
    "url": "",
    "vendor": {
        "categoriesFood": [
            {
                "id": "",
                "name": ""
            },
            {
                "id": "",
                "name": ""
            }
        ],
        "code": "",
        "name": ""
    },
    "warranty": ""
}
my_product = {
    "availableForPickup": False,
    "averageRating": 1.1,
    "baseOptions": [],
    "multimedia": {
        "img": "123123213"
        #"video": ""
    },
    "images": [
            {
                "qwe" : "mdfj",
                #"altText": "qewe",
                "format": "product",
                #"imageType": "PRIMARY",
                "originalImageCode": "099213",
                "url": "lñfgjoijgfdoig"
            },
                {
                    "qwe" : "23",
                    #"altText": "qewe",
                    "format": "thumbail",
                    "imageType": "",
                    "originalImageCode": "987h",
                    "url": "asdads"
                }
        ],
    "vendor" : {
            "categoriesFood": [
                {
                    "id": "1233",
                    #"name": "dassadsad",
                    "asd" : "asd"
                },
                {
                    "id": "1234321",
                    "name": "sadasddas"
                },
                {
                    "id": "wqert",
                    "name": "6776yj"
                }
            ],
            "code": "123krj",
            #"name": "09ijkookj"
        } #ya esta
}
#recibe dos dicts y descarta los inexistentes y añade los nuevos
def filter_dicts(dict_input, dict_body):

    for x in dict_input:
        if x in dict_body:
            dict_body[x] = dict_input[x]
        else:
            print(f"{x} is not in given body, {dict_body},\n")
            continue
    return dict_body

def get_keys(dict):
    return dict.items()
def filter_str_or(param):

    if isinstance(param, str) or isinstance(param, bool) or isinstance(param, int) or isinstance(param, float):
        return 1
    elif isinstance(param, dict):
        return 2
    elif isinstance(param, list):
        return 3
def destructuration(body):

    ret_body = [[],[],[]]
    [elements, dicts, lists] = ret_body
    for el in body:
        if filter_str_or(body[el]) == 1:
            elements.append(el)
        if filter_str_or(body[el]) == 2:
            dicts.append(el)
        if filter_str_or(body[el]) == 3:
            lists.append(el)

    return ret_body
desc_prod = destructuration(product)
[directs, dicts, lists] = desc_prod

for item1 in my_product:
    validate = filter_str_or(my_product[item1])
    if item1 in directs and validate == 1:
        product[item1] = my_product[item1]

    elif validate == 2:
        #si es un dict y no es vendor
        if item1 in dicts and item1 != "vendor":
            for x in my_product[item1]:
                if x in product[item1]:
                    product[item1][x] = my_product[item1][x]
                else:
                    print(f"{x} not founded on {item1}")
                    continue
        #si es vendor
        elif item1 in dicts and item1 == "vendor":
            for x in my_product["vendor"]:
                if x in product["vendor"]:
                    #breakpoint()
                    if x == "categoriesFood":
                        obj_val = product["vendor"]["categoriesFood"][0]
                        for y in my_product["vendor"]["categoriesFood"]:
                            index_y = my_product["vendor"]["categoriesFood"].index(y)
                            for w in y:

                                if w in obj_val:
                                    try:
                                        product["vendor"]["categoriesFood"][index_y][w] = my_product["vendor"]["categoriesFood"][index_y][w]
                                    except:
                                        product["vendor"]["categoriesFood"].append(my_product["vendor"]["categoriesFood"][index_y])
                                else:
                                    print(f"{w} is not in {obj_val}")
                                    continue
                    else:
                        product["vendor"][x] = my_product["vendor"][x]
                else:
                    print(f"{x} is not in vendor")
                    continue
    elif validate == 3:

        if item1 in lists and item1 == "images":
                breakpoint()
                images_ret = []
                for x in my_product["images"]:
                    images_ret.append(filter_dicts(x, product["images"][0]))
                product["images"] = images_ret
        #product[item1] = my_product[item1]

print(product)
