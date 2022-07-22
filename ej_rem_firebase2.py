firebase ={
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
}

my_input= {
    "vendor": {
        "categoriesFood": [
            {
                #"id": "",
                "name": "sd",
                "sadds" : "2"
            },
            {
                #"id": "",
                "name": "8998"
            }
        ],
        "code": "12233",
        #"name": ""
    }
    }
def case_dict(give_body, body):
    for x in give_body:
        if x in body:
            validate = filter_type(give_body[x])
            if give_body[x] == 1 and give_body[x] != "":
                body[x] = give_body[x]
            else:
                continue
        else:
            print(f"{x} is not in given body-- function case_dict")
