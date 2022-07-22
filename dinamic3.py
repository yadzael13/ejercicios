import pdb
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
                "code": "",
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
def filter_str_or(param):
    if isinstance(param, str) or isinstance(param, bool) or isinstance(param, int) or isinstance(param, float):
        return 1
    elif isinstance(param, dict):
        return 2
    elif isinstance(param, list):
        return 3
#convierte la lista en un solo dict

def fusion(l1,l2):
    for x in range(2):
        l2[x] |= l1[x]
    return l2


def destructuration(body):
    ret_body = [[],[],[]]
    [elements, dicts, lists] = ret_body
    for el in body:
        if filter_str_or(body[el]) == 1:
            elements.append({el : body[el]})
        if filter_str_or(body[el]) == 2:
            dicts.append({el: body[el]})
        if filter_str_or(body[el]) == 3:
            lists.append({el: body[el]})
    for x in ret_body:
            ret_body[ret_body.index(x)] = union(x)
    return ret_body
#breakpoint()
body_destr = destructuration(my_body)
input_destr = destructuration(my_new)
breakpoint()
print(fusion(input_destr, body_destr))
#def final_funct(my_new, my_body):
