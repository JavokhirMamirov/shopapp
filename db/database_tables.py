def DataBaseTableCreate(cur):
    cur.execute("""CREATE TABLE if not exists client(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL,
        company VARCHAR NULL,
        phone VARCHAR NULL
    )""")
    
    cur.execute("""CREATE TABLE if not exists product(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL,
        brend VARCHAR NULL,
        model VARCHAR NULL,
        factory VARCHAR NULL,
        price_box REAL NOT NULL,
        price_one REAL NOT NULL);""")
    
    cur.execute("""CREATE TABLE if not exists dollor(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        now_summa INTEGER NOT NULL,
        now_date VARCHAR NOT NULL,
        old_summa INTEGER NULL,
        old_date VARCHAR NULL);""")