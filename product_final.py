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
def product_filter(giv_body, body):
    def dict_assig(el_body, s_body):
        for x in el_body:
            if x in s_body:
                body[x] = el_body[x]
            else:
                print(f"{x} is not in body -- function - dict_assig")
        return s_body
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
        #asigna dinamicamente en old_body, pide una tupla copn la ub, y el elemento

    for element in giv_body:
        validate = filter_type(element)
        if validate == 1:
            body[element] = giv_body
        elif validate == 2:
            if element == "multimedia" or "stock" or "price":
                
                body[element] = dict_assig(giv_body[element], body[element])
            elif element == "vendor":
                for y in giv_body[element]:
                    if y in body[element]:
                        validate = filter_type(giv_body[element][y])
                        if validate == 3:
                            for w in y:
                                try:
                                    index_w = y.index(w)
                                    body[element][y][index_w] = dict_assig(w, body[element][y][index_w])
                                except:
                                    body[element][y].append(dict_assig(w, body[element][y][0]))
                        elif validate == 1:
                            body[element][y] = giv_body[element][y]
                        elif  validate == 4:
                            continue
                    else:
                        print(f"{x}not in vendor")
    return body

print(product_filter(my_product, product))
