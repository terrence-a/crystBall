import json_stream

f = open('input/smallSample.json', 'r')
data = json_stream.load(f)

m = 0
for item in data.persistent(): 
    m += 1
    print(item["name"])
    print(item["id"])
    print("\t" + item["set_name"])
    print("\t" + item["set"])
    print("\t" + item["collector_number"])
    if "oracle_text" in item:
        print("\t" + item["oracle_text"])
        print("\t" + item["mana_cost"])
        print("\t" + item["type_line"])
        print("\t" + str(item["cmc"]))
    else:
        for face in item["card_faces"]:
            print("\t face")
            print("\t\t" + face["oracle_text"])
            print("\t\t" + face["mana_cost"])
            print("\t\t" + (face["type_line"] if "type_line" in face else item["type_line"]))
            print("\t\t" + (str(face["cmc"]) if "cmc" in face else str(item["cmc"])))
    
    
    # print("\t" + item["scryfall_uri"])
    # print("\t" + item["legalities"])

''''   ' 
   ''  '
   ' ' '
   '  ''
   '   ' E X T: 

        Setup SQLite on mac, 
            Model This data into SqlDB.
                Define Schema
        Connect python to SQLite
            use this code to stream the card data ~> DB.
'''

