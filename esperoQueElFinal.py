json_nuevo = {
	'schedule': [
        {
		'closingTime': '111111',
		'closed': False,
		'openingTime': '1111111',
		'day': 'Domingo'
	}, {
		'day': 'Lunes',
		'closingTime': '11111111',
		'openingTime': '11111',
		'closed': False
	}, {
		'openingTime': '111111111111',
		'closingTime': '11111111111',
		'day': 'Martes',
		'closed': False
	}, {
		'closingTime': '',
		'openingTime': '111111111',
		'closed': False,
		'day': 'Miercoles'
	}],
	'categoryFilter': {
		'name': '12332',
		'id': '3242342'
	},
	'typeCommerce': 'yadza',
	'geoPoint': {
		'latitude': 123.098980,
		'longitude': 123.98789790
	},
	'address': {
		'formattedAddress': '123',
		'streetname': '',
		'streetnumber': '',
		'postalCode': '',
		'town': ''
	},
	'phone': '1111111111111111111111111',
	'name': '1111111111111111111111',
	'nameCommerce': '111111111111111111111111',
	'description': '',
	'score': '0',
}
json_firebase = {
	'imagesCommerce': {
		'mapIcon': 'https://backoffice.c6exvb10-totalplay1-s1-public.model-t.cc.commerce.ondemand.com',
		'logo192Wx192H': 'https://backoffice.c6exvb10-totalplay1-s1-public.model-t.cc.commerce.ondemand.com',
		'storeImages': 'https://backoffice.c6exvb10-totalplay1-s1-public.model-t.cc.commerce.ondemand.com'
	},
	'schedule': [
        {
		'closingTime': '2222222222222',
		'closed': True,
		'openingTime': '222222222222',
		'day': 'Domingo'
	}, {
		'day': 'Lunes',
		'closingTime': '22222222222222',
		'openingTime': '222222222222222',
		'closed': True
	}, {
		'openingTime': '2222222222222222',
		'closingTime': '2222222222222222',
		'day': 'Martes',
		'closed': True
	}, {
		'closingTime': '222222222222222',
		'openingTime': '2222222222222',
		'closed': True,
		'day': 'Miercoles'
	}, {
		'closed': True,
		'openingTime': '2222222222222',
		'day': 'Jueves',
		'closingTime': '22222222222222222'
	}, {
		'closingTime': '2222222222222222',
		'openingTime': '2222222222222222',
		'day': 'Viernes',
		'closed': True
	}, {
		'openingTime': '2222222222222222222222',
		'closingTime': '2222222222222222222222',
		'day': 'Sábado',
		'closed': True
	}],
	'categoryFilter': {
		'name': '',
		'id': ''
	},
	'typeCommerce': 'Restaurante',
	'geoPoint': {
		'latitude': 0.0,
		'longitude': 0.0
	},
	'address': {
		'formattedAddress': '',
		'streetname': 'Jardín Centenario ',
		'streetnumber': '2',
		'postalCode': '12',
		'town': 'COYOACAN'
	},
	'phone': '',
	'name': '',
	'nameCommerce': '',
	'description': '',
	'score': '0',

}



def firebase_funct(new_body, firebase):
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
    def asignar(poss, el):
        try:
            if len(poss) == 1:
                firebase[poss[0]] = el
            elif len(poss) == 2:
                firebase[poss[0]][poss[1]] = el
            elif len(poss) == 3:
                firebase[poss[0]][poss[1]][poss[2]] = el
            elif len(poss) == 4:
                firebase[poss[0]][poss[1]][poss[2]][poss[3]] = el
            elif len(poss) == 5:
                firebase[poss[0]][poss[1]][poss[2]][poss[3]][poss[4]] = el
            else:
                print("bad possition function - asignar")
        except:
            print("Error en asignar, verificar elementos enviados") #ya sirve

    asignar(("typeCommerce"),new_body["typeCommerce"])
    print(new_body["typeCommerce"])
    def dict_assing(dict_in, dict):
        for x in dict_in:
            if x in dict:
                dict[x] = dict_in[x]
            else:
                print(f"{x} is not in body -- funcion dict_assign")
                continue
        return dict
    #asignar(("dos", "dos_1"), "uno")

    for el in new_body:
        #breakpoint()
        if el in firebase:
            my_el = new_body[el]
            fb_rt = [el]
            firebase1 = firebase[el]
            try:
                    validate = filter_type(my_el)
                    #si es assig, primer nivel
                    if validate == 1:
                        asignar(tuple(fb_rt), my_el)
                    #caso dict, primer nivel
                    elif validate == 2 or validate == 3:
                        for el_1 in my_el:
                            if el_1 in firebase_1:
                                validate = filter_type(el_1)
                                #si es un dict
                                if validate == 2:
                                    #breakpoint()
                                    a = dict_assign(el_1, firebase_1[el_1])
                                    fb_rt.append(el_1)
                                    asignar(tuple(fb_rt),a)
                                else:
                                    #valida el otro campo
                                    validate = filter_type(my_el[el_1])
                                    #si es un assig 2do nivel
                                    if validate == 1:
                                        a = my_el[el_1]
                                        fb_rt.append(el_1)

                                        asignar(tuple(fb_rt),a)
                            else:
                                print(f"{el_1} is not in level 2 firebase")
                    #elif validate == 3:
                        #print("not ready for lists")
                        #lists_assign(body_1, firebase_1)
                    elif validate == 4:
                        continue
            except:
                print("el elemento es un dict completo")
        else:
            print(f"{el} is not on given body")
    return firebase
firebase_funct(json_nuevo, json_firebase)
print(firebase_funct(json_nuevo, json_firebase))
