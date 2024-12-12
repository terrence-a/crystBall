import sqlite3, json_stream

# Setup Stuff: 
# SQL Setup::
con = sqlite3.connect('./db/cardsDb.db');
cur = con.cursor();
cards_insert_fmt_s = "INSERT INTO Cards VALUES ('{id}', '{card_name}', '{set_name}', '{collector_num}', '{set_code}', '{img_uri}', '{scfl_uri}');"
cards_insert_fmt = "INSERT INTO Cards VALUES ('{}', '{}', '{}', '{}', '{}', '', '');"
cardfaces_insert_fms = "INSERT INTO CardFaces VALUES (NULL, '{}', '{}', '{}', '{}', '{}')"

# File Setup 
f = open('./input/cardList.json', 'r')
data = json_stream.load(f)

for item in data.persistent(): 
    id = item["id"]
    name = item["name"].replace("'", "''")
    set_nm = item["set_name"].replace("'", "''")
    set_cd = item["set"]
    collector_num = item["collector_number"]
    img_uri = ''
    scfl_uri = ''
    cards_inset_cmd = cards_insert_fmt.format(id, name, set_nm, collector_num, set_cd)
    cur.execute(cards_inset_cmd)
    if "oracle_text" in item:
        oracle_text = item["oracle_text"].replace("'", "''")
        mana_cost = item["mana_cost"]
        type_line = item["type_line"].replace("'", "''")
        cmc = item["cmc"]
        cardfaces_insert_cmd = cardfaces_insert_fms.format(id, oracle_text, mana_cost, type_line, cmc)
        print(cardfaces_insert_cmd)
        cur.execute(cardfaces_insert_cmd)
    elif "card_faces" in item: 
        for face in item["card_faces"]: 
            oracle_text = face["oracle_text"].replace("'", "''")
            mana_cost = face["mana_cost"]
            type_line = (face["type_line"] if "type_line" in face else item["type_line"]).replace("'", "''")
            cmc = face["cmc"] if "cmc" in face else item["cmc"]
            cardfaces_insert_cmd = cardfaces_insert_fms.format(id, oracle_text, mana_cost, type_line, cmc)
            print(cardfaces_insert_cmd)
            cur.execute(cardfaces_insert_cmd)
    con.commit()
    
    # cur.execute(cards_inset_cmd)
    