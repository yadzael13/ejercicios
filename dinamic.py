my_body = {

            "address": {
                "appartment": "",
                "billingAddress": False,
                "cellphone": "",
                "contactAddress": False,
                "country": {
                    "isocode": "",
                    "name": ""
                },
                "defaultAddress": False,
                "delegation": "",
                "district": "",
                "email": "",
                "firstName": "",
                "formattedAddress": "",
                "fullName": "",
                "id": "",
                "lastName": "",
                "line1": "",
                "line2": "",
                "phone": "",
                "postalCode": "",
                "region": {
                    "countryIso": "",
                    "isocode": "",
                    "isocodeShort": "",
                    "name": ""
                },
                "shippingAddress": False,
                "streetname": "",
                "streetnumber": "",
                "town": "",
                "visibleInAddressBook": False
            },
            "description": "",
            "displayName": "",
            "features": {},
            "geoPoint": {
                "latitude": 0.0,
                "longitude": 0.0
            },
            "mapIcon": {
                "format": "64Wx64H",
                "url": ""
            },
            "name": "",
            "openingHours": {
                "code": "delivery_madeira",
                "specialDayOpeningList": [],
                "weekDayOpeningList": [
                    {
                        "closingTime": {
                            "formattedHour": "",
                            "hour": 0,
                            "minute": 0
                        },
                        "openingTime": {
                            "formattedHour": "",
                            "hour": 0,
                            "minute": 0
                        },
                        "closed": False,
                        "weekDay": "dom."
                    },
                    {
                        "closingTime": {
                            "formattedHour": "",
                            "hour": 0,
                            "minute": 0
                        },
                        "openingTime": {
                            "formattedHour": "",
                            "hour": 0,
                            "minute": 0
                        },
                        "closed": False,
                        "weekDay": "lun."
                    },
                    {
                        "closingTime": {
                            "formattedHour": "",
                            "hour": 0,
                            "minute": 0
                        },
                        "openingTime": {
                            "formattedHour": "",
                            "hour": 0,
                            "minute": 0
                        },
                        "closed": False,
                        "weekDay": "mar."
                    },
                    {
                        "closingTime": {
                            "formattedHour": "",
                            "hour": 0,
                            "minute": 0
                        },
                        "openingTime": {
                            "formattedHour": "",
                            "hour": 0,
                            "minute": 0
                        },
                        "closed": False,
                        "weekDay": "mié."
                    },
                    {
                        "closingTime": {
                            "formattedHour": "",
                            "hour": 0,
                            "minute": 0
                        },
                        "openingTime": {
                            "formattedHour": "",
                            "hour": 0,
                            "minute": 0
                        },
                        "closed": False,
                        "weekDay": "jue."
                    },
                    {
                        "closingTime": {
                            "formattedHour": "",
                            "hour": 0,
                            "minute": 0
                        },
                        "openingTime": {
                            "formattedHour": "",
                            "hour": 0,
                            "minute": 0
                        },
                        "closed": False,
                        "weekDay": "vie."
                    },
                    {
                        "closingTime": {
                            "formattedHour": "",
                            "hour": 0,
                            "minute": 0
                        },
                        "openingTime": {
                            "formattedHour": "",
                            "hour": 0,
                            "minute": 0
                        },
                        "closed": False,
                        "weekDay": "sáb."
                    }
                ]
            },
            "storeImages": [
                {
                    "format": "store",
                    "url": ""
                }
            ],
            "warehouseCodes": [
                ""
            ],
            "warehousesDetail": [
                {
                    "vendor": {
                        "catalog": {
                            "id": "",
                            "name": "",
                            "catalogVersions": [
                                {
                                    "id": ""
                                }
                            ]
                        },
                        "categoriesFood": [],
                        "code": "",
                        "description": "",
                        "idProveedorBRM": "",
                        "logo": [
                            {
                                "format": "64Wx64H",
                                "imageType": "GALLERY",
                                "url": ""
                            },
                            {
                                "format": "128Wx128H",
                                "imageType": "GALLERY",
                                "url": ""
                            },
                            {
                                "format": "192Wx192H",
                                "imageType": "GALLERY",
                                "url": ""
                            }
                        ],
                        "name": ""
                    },
                    "warehouseCode": ""
                }
            ]
}
#Para strings, enteros, booleanos, y flotantes se hace asignacion directa
#para listas, dicts hay que iterar
#para dict asignar el dict como body, pasar parametros
#Si es list, itera y asigna
my_new = {
    "address" : {
        "appartment" : "2asd",
        "billingAddress": True
    },
    "description": "Yadzaaa",
    "displayName": "asdasdsadasd",
    "features": {},
    "geoPoint": {
        "latitude": 12.213123,

    },
    "warehousesDetail": [
        {
            "vendor": {
                "catalog": {
                    "id": "myidyes",

                    "catalogVersions": [
                        {
                            "id": "12345"
                        }
                    ]
                },
                "categoriesFood": [],
                "code": "D2tes",
                "description": "lkashdkjsahdiuashdiuasd",
                "idProveedorBRM": "asdasdqwqeqwe123431324324",
                    "logo": [

                        {
                            "format": "128Wx128H",
                            "imageType": "GALLERY",
                            "url": "https/vergasPutosasdasdasd/asdasdads/pasidopidsa"
                        },
                        {
                            "format": "192Wx192H",
                            "imageType": "GALLERY",
                            "url": "https/vergasPutosasdasdasd/asdasdads"
                        }
                    ],
                    "name": "Tu padre"
                    }
            }]

}

#Body destructuration ----                         Alll are dicts except *#
warehousesDetail = my_body["warehousesDetail"]
address = my_body["address"]
address_country = my_body["address"]["country"]
address_region = my_body["address"]["region"]
features = my_body["features"]
geoPoint =  my_body["geoPoint"]
mapIcon = my_body["mapIcon"]
openingHours = my_body["openingHours"]
openingHours_specialDayOpeningList = my_body["openingHours"]["specialDayOpeningList"] #List
openingHours_weekDayOpeningList = my_body["openingHours"]["weekDayOpeningList"] #List
storeImages = my_body["storeImages"] #List with just one dict
warehouseCodes = my_body["warehouseCodes"] #list
warehousesDetail = my_body["warehousesDetail"]  #List with just one dict
warehousesDetail_vendor = my_body["warehousesDetail"][0]["vendor"]
warehousesDetail_vendor_catalog = my_body["warehousesDetail"][0]["vendor"]["catalog"]
warehousesDetail_vendor_catalog_catalogVersions = my_body["warehousesDetail"][0]["vendor"]["catalog"]["catalogVersions"]# List
warehousesDetail_vendor_categoriesFood = my_body["warehousesDetail"][0]["vendor"]["categoriesFood"] #list
warehousesDetail_vendor_logo = my_body["warehousesDetail"][0]["vendor"]["logo"] #list

master_list = [
        warehousesDetail, address, address_country, address_region, features, geoPoint, mapIcon,
        openingHours, openingHours_specialDayOpeningList, openingHours_weekDayOpeningList,
        storeImages,
        warehouseCodes,
        warehousesDetail, warehousesDetail_vendor, warehousesDetail_vendor_catalog, warehousesDetail_vendor_catalog_catalogVersions,
            warehousesDetail_vendor_categoriesFood, warehousesDetail_vendor_logo
         ]
my_list_ret = []

def filter_str_etc(my_new, my_body):
    my_ret =  my_body
    for x in my_new:
        #print(my_new[x])
        if x in my_body:
            if isinstance(my_new[x], str) or isinstance(my_new[x], bool) or isinstance(my_new[x], int) or isinstance(my_new[x], float):

                my_ret[x] = my_new[x]

            elif isinstance(my_new[x], dict):

                my_list_ret.append(filter_str_etc(my_new[x], my_ret[x]))
            elif isinstance(my_new[x], list):
                if len(my_new[x]) == 1:

                        my_list_ret.append(filter_str_etc(my_new[x][0], my_ret[x]))


            else:
                print(x, "is not a str, or int, or bool, or float, weird")

        else:
            print(x, "is not in given body")
            continue
    for x in my_body:
        if x in my_ret:
            continue
        else:
            my_ret[x] = my_body[x]
    return my_ret


filter_str_etc(my_new, my_body)
print(my_list_ret)










"""
#2nd round, close but failed, yet
def principal_funct(lazy_body,body):
    my_ret_body = body
    def filter_vergas(el):
        if el in body:
            if type(lazy_body[el]) == type(body[el]):
                if isinstance(lazy_body[el],str) or isinstance(lazy_body[el],int) or isinstance(lazy_body[el],bool) or isinstance(lazy_body[el],float):
                    my_ret_body[el] = lazy_body[el]
                elif isinstance(lazy_body[el], list):
                    if len(lazy_body[el])<2 and len(lazy_body[el])!=0:
                        #for x in lazy_body[el]:
                            principal_funct(lazy_body[el], body[el])
                        else:
                            my_ret_body[el] = lazy_body[el]

                elif isinstance(lazy_body[el], dict):
                    principal_funct(lazy_body[el], body[el])
            else:
                print(f"El tipo de dato de  '{el}' no corresponde al del body ")
        else:
            print(el, "No encontrado en body")
    for x in lazy_body:
        filter_vergas(x)


principal_funct(my_new, my_body)
print(my_ret_body)

"""

"""
#Lo voy a borrar de la deseperacion!!!!
def principal_funct(input, body):
    body_ret = body
    def validate(param, val_body):
        if param in val_body:
            if type(input[param]) == type(val_body[param]):
                if isinstance(input[param], str) or isinstance(input[param], int) or isinstance(input[param], bool) or isinstance(input[param], float):
                    body_ret[param] = input[param]
                    return body_ret
                else:
                    #Recursividad
                    print("not.. yet")
            else:
                print(input[param], "has not type", type(val_body[param]), "on", param)
        else:
            print(param, "not found on given body")


    for x in input:
        validate(x, body)
    return body_ret
print(principal_funct(my_new, my_body))
"""
