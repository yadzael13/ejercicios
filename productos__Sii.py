json_plantilla ={
    "availableForPickup": True,
    "averageRating": 0.0,
    "baseOptions": [],
    "categories": [
        {
            "code": "",
            "name": "",
            "url": ""
        },
        {
            "code": "D9_1",
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
                    "comparable": True,
                    "featureUnit": {
                        "name": "",
                        "symbol": "",
                        "unitType": ""
                    },
                    "featureValues": [
                        {
                            "value": ""
                        }
                    ],
                    "name": "",
                    "range": False
                }
            ],
            "name": ""
        }
    ],
    "code": "Dcafe_FoodProduct_CAFENEGRO_Dcafe_1_4",
    "configurable": False,
    "description": "D4",
    "galleryImages": [
        {
            "altText": "",
            "format": "product",
            "galleryIndex": 0,
            "galleryQualifier": "",
            "imageType": "",
            "url": ""
        },
        {
            "altText": "",
            "format": "thumbnail",
            "galleryIndex": 0,
            "galleryQualifier": "",
            "imageType": "",
            "url": ""
        }
    ],
    "images": [
        {}
    ],
    "manufacturer": "",
    "manufacturerName": "",
    "multimedia": {
        "img": "",
        "video": ""
    },
    "name": "",
    "numberOfReviews": 0,
    "offlineDate": "",
    "onlineDate": "",
    "potentialPromotions": [],
    "price": {
        "currencyIso": "",
        "formattedValue": "",
        "priceType": "",
        "value": 0
    },
    "priceRange": {},
    "productReferences": [],
    "purchasable": True,
    "reviews": [],
    "sku": "",
    "stock": {
        "stockLevel": 0,
        "stockLevelStatus": ""
    },
    "summary": ".",
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
        "code": "D99_20",
        "name": ""
    },
    "warranty": ""
}

json_fragmento = {
   "price": {
        "priceType": "11111111",
        "prdddddddddddiceType": "11111111",
        "value": 105.0
    },
   "galleryImages": [
       {
           "altText": "213",
           "format": "zoom",
           "imageType": "PRIMARY",
           "originalImageCode": "905y904",
           "url": "lkjdfjlsd"
       },
       {
           "altText": "fgfdg",
           "format": "product",
           "imageType": "PRIMARY",
           "originalImageCode": "879789",
           "url": "dsflkjf"
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
   "vendor": {
       "categoriesFood": [
           {
               "id": "123",
               "name": "56546"
           },
           {
               "id": "as123",
               "name": "asdsad",
               "qwe" : "qwe"
           }
       ],
       "code": "",
       #"name": ""
   },
   "warranty": "555"
}

for item in json_fragmento:
    if item == "availableForPickup":
        try:
            json_plantilla["availableForPickup"]=json_fragmento["availableForPickup"]
        except:
            pass
    elif item == "averageRating":
        try:
            json_plantilla["averageRating"]=json_fragmento["averageRating"]
        except:
            pass
    elif item == "baseOptions":
        try:
            json_plantilla["baseOptions"]=json_fragmento["baseOptions"]
        except:
            pass
    elif item == "categories":
        try:
            json_plantilla["categories"][0]["code"]=json_fragmento["categories"][0]["code"]
        except:
            pass

        try:
            json_plantilla["categories"][0]["name"]=json_fragmento["categories"][0]["name"]
        except:
            pass

        try:
            json_plantilla["categories"][0]["url"]=json_fragmento["categories"][0]["url"]
        except:
            pass
    elif item == "characteristics":
        try:
            json_plantilla["characteristics"]=json_fragmento["characteristics"]
        except:
            pass
            #pendiente
    elif item == "classifications":
        for item2 in json_fragmento[item][0]:
            try:
                json_plantilla["classifications"][0][item2] = json_fragmento["classifications"][0][item2]
            except:
                pass
    elif item == "code":
         try:
             json_plantilla["code"]=json_fragmento["code"]
         except:
             pass
    elif item == "configurable":
         try:
            json_plantilla["configurable"]=json_fragmento["configurable"]
         except:
              pass
    elif item == "description":
         try:
            json_plantilla["description"]=json_fragmento["description"]
         except:
              pass
    elif item == "galleryImages":
         
         for item2 in json_fragmento[item]:
             pos_item2 = json_fragmento[item].index(item2)

             for item3 in json_fragmento[item][pos_item2]:
                try:
                    json_plantilla[item][pos_item2][item3] = json_fragmento[item][pos_item2][item3]
                except:
                    pass
    elif item == "images":
          for item2 in json_fragmento[item]:
              pos_item2 = json_fragmento[item].index(item2)

              for item3 in json_fragmento[item][pos_item2]:
                 try:
                     json_plantilla[item2][pos_item2][item3] = json_fragmento[item2][pos_item2][item3]
                 except:
                     pass
    elif item == "manufacturer":
         try:
            json_plantilla["manufacturer"]=json_fragmento["manufacturer"]
         except:
              pass
    elif item == "manufacturerName":
         try:
            json_plantilla["manufacturerName"]=json_fragmento["manufacturerName"]
         except:
              pass
    elif item == "multimedia":
         for item2 in json_fragmento[item]:
             try:
                 json_plantilla[item][item2] = json_fragmento[item][item2]
             except:
                pass
    elif item == "name":
         try:
            json_plantilla["name"]=json_fragmento["name"]
         except:
              pass
    elif item == "numberOfReviews":
         try:
            json_plantilla["numberOfReviews"]=json_fragmento["numberOfReviews"]
         except:
              pass
    elif item == "offlineDate":
         try:
            json_plantilla["offlineDate"]=json_fragmento["offlineDate"]
         except:
              pass
    elif item == "onlineDate":
         try:
            json_plantilla["onlineDate"]=json_fragmento["onlineDate"]
         except:
              pass
    elif item == "potentialPromotions":
         try:
            json_plantilla["potentialPromotions"]=json_fragmento["potentialPromotions"]
         except:
              pass
    elif item == "price":
        for item2 in json_plantilla["price"]:
            try:
                json_plantilla["price"][item2]=json_fragmento["price"][item2]
            except:
                pass
    elif item == "priceRange":
            try:
                json_plantilla["priceRange"]=json_fragmento["priceRange"]
            except:
                pass
    elif item == "productReferences":
            try:
                json_plantilla["productReferences"]=json_fragmento["productReferences"]
            except:
                pass

    elif item == "purchasable":
            try:
                json_plantilla["purchasable"]=json_fragmento["purchasable"]
            except:
                pass

    elif item == "reviews":
            try:
                json_plantilla["reviews"]=json_fragmento["reviews"]
            except:
                pass

    elif item == "sku":
            try:
                json_plantilla["sku"]=json_fragmento["sku"]
            except:
                pass
    elif item == "stock":
        for item2 in item:
            try:
                json_plantilla["stock"][item2]=json_fragmento["stock"][item2]
            except:
                pass
    elif item == "summary":
            try:
                json_plantilla["summary"]=json_fragmento["summary"]
            except:
                pass
    elif item == "url":
            try:
                json_plantilla["url"]=json_fragmento["url"]
            except:
                pass
    elif item == "vendor":
            for item2 in json_fragmento[item]:
                if item2 == "categoriesFood":
                    for item3 in json_fragmento[item][item2]:
                        pos_item3 = json_fragmento[item][item2].index(item3)
                        try:
                            json_plantilla[item][item2][pos_item3] = json_fragmento[item][item2][pos_item3]
                        except:
                            pass
                else:
                    try:
                        json_plantilla[item][item2] = json_fragmento[item][item2]
                    except:
                        pass
    elif item == "warranty":
            try:
                json_plantilla["warranty"]=json_fragmento["warranty"]
            except:
                pass
print(json_plantilla)
