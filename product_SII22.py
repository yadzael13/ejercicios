def pruducto_dos(json_fragmento, json_plantilla):
    errors = ["",0,0.0,[],{}]
    for item in json_fragmento and item not in errors:
          if item == "availableForPickup" and item not in errors:
              try:
                  json_plantilla["availableForPickup"]=json_fragmento["availableForPickup"]
              except:
                  pass
          elif item == "averageRating" and item not in errors:
              try:
                  json_plantilla["averageRating"]=json_fragmento["averageRating"]
              except:
                  pass
          elif item == "baseOptions" and item not in errors:
              try:
                  json_plantilla["baseOptions"]=json_fragmento["baseOptions"]
              except:
                  pass
          elif item == "categories" and item not in errors:
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
          elif item == "characteristics" and item not in errors:
              try:
                  json_plantilla["characteristics"]=json_fragmento["characteristics"]
              except:
                  pass
                  #pendiente
          elif item == "classifications"  and item not in errors:
              for item2 in json_fragmento[item][0]:
                  try:
                      json_plantilla["classifications"][0][item2] = json_fragmento["classifications"][0][item2]
                  except:
                      pass
          elif item == "code"  and item not in errors:
               try:
                   json_plantilla["code"]=json_fragmento["code"]
               except:
                   pass
          elif item == "configurable"  and item not in errors:
               try:
                  json_plantilla["configurable"]=json_fragmento["configurable"]
               except:
                    pass
          elif item == "description"  and item not in errors:
               try:
                  json_plantilla["description"]=json_fragmento["description"]
               except:
                    pass
          elif item == "galleryImages" and item not in errors:

               for item2 in json_fragmento[item]:
                   pos_item2 = json_fragmento[item].index(item2)

                   for item3 in json_fragmento[item][pos_item2]:
                      try:
                          json_plantilla[item][pos_item2][item3] = json_fragmento[item][pos_item2][item3]
                      except:
                          pass
          elif item == "images" and item not in errors:
                for item2 in json_fragmento[item]:
                    pos_item2 = json_fragmento[item].index(item2)

                    for item3 in json_fragmento[item][pos_item2]:
                       try:
                           json_plantilla[item2][pos_item2][item3] = json_fragmento[item2][pos_item2][item3]
                       except:
                           pass
          elif item == "manufacturer" and item not in errors:
               try:
                  json_plantilla["manufacturer"]=json_fragmento["manufacturer"]
               except:
                    pass
          elif item == "manufacturerName" and item not in errors:
               try:
                  json_plantilla["manufacturerName"]=json_fragmento["manufacturerName"]
               except:
                    pass
          elif item == "multimedia" and item not in errors:
               for item2 in json_fragmento[item]:
                   try:
                       json_plantilla[item][item2] = json_fragmento[item][item2]
                   except:
                      pass
          elif item == "name" and item not in errors:
               try:
                  json_plantilla["name"]=json_fragmento["name"]
               except:
                    pass
          elif item == "numberOfReviews" and item not in errors:
               try:
                  json_plantilla["numberOfReviews"]=json_fragmento["numberOfReviews"]
               except:
                    pass
          elif item == "offlineDate" and item not in errors:
               try:
                  json_plantilla["offlineDate"]=json_fragmento["offlineDate"]
               except:
                    pass
          elif item == "onlineDate" and item not in errors:
               try:
                  json_plantilla["onlineDate"]=json_fragmento["onlineDate"]
               except:
                    pass
          elif item == "potentialPromotions" and item not in errors:
               try:
                  json_plantilla["potentialPromotions"]=json_fragmento["potentialPromotions"]
               except:
                    pass
          elif item == "price" and item not in errors:
              for item2 in json_plantilla["price"]:
                  try:
                      json_plantilla["price"][item2]=json_fragmento["price"][item2]
                  except:
                      pass
          elif item == "priceRange" and item not in errors:
                  try:
                      json_plantilla["priceRange"]=json_fragmento["priceRange"]
                  except:
                      pass
          elif item == "productReferences" and item not in errors:
                  try:
                      json_plantilla["productReferences"]=json_fragmento["productReferences"]
                  except:
                      pass
          elif item == "purchasable" and item not in errors:
                  try:
                      json_plantilla["purchasable"]=json_fragmento["purchasable"]
                  except:
                      pass
          elif item == "reviews" and item not in errors:
                  try:
                      json_plantilla["reviews"]=json_fragmento["reviews"]
                  except:
                      pass
          elif item == "sku" and item not in errors:
                  try:
                      json_plantilla["sku"]=json_fragmento["sku"]
                  except:
                      pass
          elif item == "stock" and item not in errors:
              for item2 in item:
                  try:
                      json_plantilla["stock"][item2]=json_fragmento["stock"][item2]
                  except:
                      pass
          elif item == "summary" and item not in errors:
                  try:
                      json_plantilla["summary"]=json_fragmento["summary"]
                  except:
                      pass
          elif item == "url" and item not in errors:
                  try:
                      json_plantilla["url"]=json_fragmento["url"]
                  except:
                      pass
          elif item == "vendor" and item not in errors:
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
          elif item == "warranty" and item not in errors:
                  try:
                      json_plantilla["warranty"]=json_fragmento["warranty"]
                  except:
                      pass
          elif item in error:
              print(f"{item} not in body")
          else:
              print(f"{item} not in body")
    return json_plantilla

week_list =  [
    {
    'closingTime': '2222222222222',
    'closed': True,
    'openingTime': '222222222222',
    'day': 'Domingo'
}, {
    'day': 'Domingo',
    'closingTime': '22222222222222',
    'openingTime': '222222222222222',
    'closed': True
}, {
    'openingTime': '2222222222222222',
    'closingTime': '2222222222222222',
    'day': 'Domingo',
    'closed': True
}, {
    'closingTime': '222222222222222',
    'openingTime': '2222222222222',
    'closed': True,
    'day': 'Domingo'
}, {
    'closed': True,
    'openingTime': '2222222222222',
    'day': 'Domingo',
    'closingTime': '22222222222222222'
}, {
    'closingTime': '2222222222222222',
    'openingTime': '2222222222222222',
    'day': 'Domingo',
    'closed': True
}, {
    'openingTime': '2222222222222222222222',
    'closingTime': '2222222222222222222222',
    'day': 'Domingo',
    'closed': True
}]
def week_days(week_list):
    days=["Domingo","Lunes","Martes", "Miercoles", "Jueves", "Viernes", "Sabado"]
    i = 0
    for data_day in week_list:
        week_list[i]["day"] = days[i]
        i += 1

    return week_list
print(week_days(week_list))
