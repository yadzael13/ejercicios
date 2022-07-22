json_nuevo={
    "geoPoint" :
        {
            "latitude" : 0,
            "longitude" : 0
        }
}
json_firebase={
	'geoPoint': {
		'latitude': 0.0,
		'longitude': 0.0
	},
 	'address': {
 		'formattedAddress': '',
 		'streetname': 'Jardín Centenario ',
 		'streetnumber': '2',
 		'postalCode': '',
 		'town': 'COYOACAN'
 	},
}
def body_restaurant(new, exis):
    if "geoPoint" in new:
        excepts = [0,0,0.0,"0","0.0"]
        if (new["geoPoint"]["latitude"] not in excepts) and (new["geoPoint"]["longitude"] not in excepts):
            return update_product(new, exis)
        else:
            print("Values not valid to GeoPoint")
            pass
    else:
        print("You most giveme a GeoPoint")
        pass
def update_product(new, exis):
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
    #en caso de listas ...
    def case_list(list, empty_dict):
        ret_list = []
        for x in list:
                posx = list.index(x)
                if isinstance(x, dict):
                    my_dict= {}
                    for y in x:
                        if y in empty_dict:
                            my_dict |= {y : list[posx][y]}
                        else:
                            print(f"{y} is not in body -- (list_case funct)")
                            continue
                    for w in empty_dict:
                        if w not in my_dict:
                             my_dict |= {w : empty_dict[w]}
                    ret_list.append(my_dict)
                else:
                    ret_list = update_product(x, empty_dict)
        return ret_list

    for el in new:
     try:
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
                    if len(new[el]) > 1:
                        ls = []
                        ls.append(exis[el][0])
                        if len(new[el]) == len(exis[el]):
                            exis[el] = case_list(new[el], ls[0])
                        else:
                            long1 = len(exis[el])
                            exis[el] = case_list(new[el], ls[0])
                            while len(exis[el]) < long1:
                                exis[el].append(ls[0])
                    elif len(new[el]) == 1:
                        exis[el] = [update_product(new[el][0], exis[el][0])]
                    else:
                        continue
            else:
                print(f"{el} is not the same data type of given body")
        else:
            print(f"{el} is not in given body")
     except:
         print(f"error in {el}")
    return exis
print(update_product(json_nuevo, json_firebase))
