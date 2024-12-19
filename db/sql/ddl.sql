-- DDL FOR CrystBal

CREATE TABLE Cards (
    id TEXT PRIMARY KEY NOT NULL,
    card_name TEXT NOT NULL,
    set_name TEXT NOT NULL,
    collector_num TEXT NOT NULL,
    set_code TEXT NOT NULL,
    card_img_uri TEXT, 
    scryfall_uri TEXT
);

CREATE TABLE CardFaces (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    card_id TEXT NOT NULL, 
    oracle_text TEXT NOT NULL, 
    mana_cost TEXT NOT NULL, 
    type_line TEXT NOT NULL, 
    cmc REAL, 
    FOREIGN KEY(card_id) REFERENCES Cards(id)
);