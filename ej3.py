
json_nuevo={
	'statusPromocion': True,
	'images': {
		'thumbnail': '2323',
		'product': '23123'
	},
	'currency': 'qqweqew',
	'id': 'qweqwe',
	'score': 0,
	'stockDisponible': False,
	'imageProductCarousel': 'qweqweqwe',
	'category': '',
	'promocion_Producto': {},
	'Reviews': [],
	'descriptionHTML': 'wqeqwe',
	'name': 'wqeqwe',
	'amount': 'qweqwe',
	'description': 'wqeqweqe'
}

#Modificar
json_firebase={
	'statusPromocion': True,
	'images': {
		'thumbnail': '/medias/D1-FoodProduct-QUETA-D1-2-7-Imagen-listas-80x80.jpg?context=bWFzdGVyfGltYWdlc3wyODc5fGltYWdlL2pwZWd8aGE3L2gwYi84ODY5NDUyNTc4ODQ2L0QxX0Zvb2RQcm9kdWN0X1FVRVRBX0QxXzJfN19JbWFnZW5fbGlzdGFzXzgweDgwLmpwZ3w2OGMyMTdhODVhYWZmNjU4Y2UwYjk3ODRmNTZjNzE3ZGE4M2VjYTMyODg1OTNlMjhmNWRkMDQ0ZGQ5NjljZWFl',
		'product': 'https://storage.googleapis.com/delivery-dev/delivery-dev/Carrousel/sucursal-default-515.jpg'
	},
	'currency': 'MXN',
	'id': 'D9_FoodProduct_QUETA_D1_2_7',
	'score': 0,
	'stockDisponible': True,
	'imageProductCarousel': '',
	'category': 'D9_2',
	'promocion_Producto': {},
	'Reviews': [],
	'descriptionHTML': '',
	'name': 'Alipapas Red Hot',
	'amount': '110.0',
	'description': 'Deliciosa salsa red hot cubriendo 6 alitas sobre una cama de lechuga con bastones de zanahoria y aderezo acompañadas con papas a la francesa'
}
def get_json(json_nuevo, json_firebase):
    excepts = ["", 0, 0.0, [], {}]
    for item in json_nuevo:
        if item in json_firebase:
            if item not in excepts:
                if isinstance(item,dict):
                    json_firebase[el] = get_json(json_nuevo[item],json_firebase[item])
                else:
                    json_firebase[item] = json_nuevo[item]
            else:
                print(f"{item} has some empty value")
                continue
        else:
            print(f"{item}is not in json_firebase")
    return json_firebase
#print(get_json(json_nuevo, json_firebase))

def update_product_firebase(json_nuevo,json_firebase):
  errors = ["", 0, 0.0, [], {}]
  #Actualizar datos - La condicion mientras sea diferente al dato default de la plantilla "",0, false
  for item in json_nuevo and item not in errors:
    if item == 'statusPromocion' and item not in errors:
          aux=json_nuevo['statusPromocion']
          try:
            if aux!=False:
              json_firebase['statusPromocion']=aux
          except:
            pass
    elif item == "images" and item not in errors:
        for x in item:
            try:
                json_firebase[item][x] = json_nuevo[item][x]
            except:
                pass
    elif item == "currency"  and item not in errors:
        try:
            json_firebase[item] = json_nuevo[item]
        except:
            pass
    elif item == "id"  and item not in errors:
        try:
            json_firebase[item] = json_nuevo[item]
        except:
            pass
    elif item == "score"  and item not in errors:
        try:
            json_firebase[item] = json_nuevo[item]
        except:
            pass
    elif item == "stockDisponible"  and item not in errors:
        try:
            json_firebase[item] = json_nuevo[item]
        except:
            pass
    elif item == "imageProductCarousel"  and item not in errors:
        try:
            json_firebase[item] = json_nuevo[item]
        except:
            pass
    elif item == "category" and item not in errors:
        try:
            json_firebase[item] = json_nuevo[item]
        except:
            pass
    elif item == "promocion_Producto" and item not in errors:
        try:
            json_firebase[item] = json_nuevo[item]
        except:
            pass
    elif item == "Reviews" and item not in errors:
        try:
            json_firebase[item] = json_nuevo[item]
        except:
            pass
    elif item == "descriptionHTML"  and item not in errors:
        try:
            json_firebase[item] = json_nuevo[item]
        except:
            pass
    elif item == "name"  and item not in errors:
        try:
            json_firebase[item] = json_nuevo[item]
        except:
            pass
    elif item == "amount"  and item not in errors:
        try:
            json_firebase[item] = json_nuevo[item]
        except:
            pass

    elif item == "description"  and item not in errors:
        try:
            json_firebase[item] = json_nuevo[item]
        except:
            pass
    elif item in errors:
        print(f"{item} esta vacio, regresando el existente")
    else:
        print(f"{item} no esta en body")

def get_boolean(string):
    if (string.lower()) == "true":
        return True
    elif (string.lower()) == "false":
        return False
    else:
        return "Not Boolean"

def week_days(week_list):
    days=["Domingo","Lunes","Martes", "Miercoles", "Jueves", "Viernes"]
    for data_day in week_list:
        pos_data = week_list.index(data_day)
        for day in days:
            if week_list[data_day]["day"] == day:
                continue
            else:
                 week_list[data_day]["day"] = day
                 continue
    return week_list

print(get_boolean("True"))
print(get_boolean("true"))
print(get_boolean("False"))
print(get_boolean("false"))
print(get_boolean("asdsad"))
