import pdb
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
    "code": "weeey",
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
    "availableForPickup": True,
    "averageRating": 10.0,
    "characteristics": "sadsadsadasd",
    "classifications": [
        {
            "code": "123123",
            "features": [
                {
                    "code": "asdasd",
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
                    "name": "Yadza",
                    "range": True
                }]}],
    "code": "weeey",
    "configurable": True,
    "multimedia": {
        "img": "ipowerrteiurte",
        "video": "nmb,vfjklfdk"
    },
    "name": "oiqpr",
    "numberOfReviews": 67,
    "price": {
        "currencyIso": "MXN",
        "formattedValue": "$",
        "priceType": "BUY",
        "value": 0.0
    }
}

def filter_str_or(param):
    if isinstance(param, str) or isinstance(param, bool) or isinstance(param, int) or isinstance(param, float):
        return 1
    elif isinstance(param, dict):
        return 2
    elif isinstance(param, list):
        return 3
#ingresas parametro, elemento
def direct_assign(param, elem):
    validate = filter_str_or(elem)

    if validate == 1:
        product[param] = elem
    elif validate == 2:
        for x in elem:
            validate = filter_str_or(elem[x])
            if validate == 1:
                product[param][x] = elem
    elif validate == 3:
        print("i'm not ready to list!")




def get_body(plantilla_body):
    for item in plantilla_body:
        if item in product:
            direct_assign(item, plantilla_body[item])
    return product
breakpoint()
print(get_body(my_product))
