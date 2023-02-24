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
    
    cur.execute("""CREATE TABLE if not exists basket(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        savdo_id INTEGER NULL,
        product_id INTEGER NOT NULL,
        name VARCHAR NOT NULL,
        brend VARCHAR NULL,
        model VARCHAR NULL,
        factory VARCHAR NULL,
        birlik VARCHAR NULL,
        narxi_dollor REAL NOT NULL,
        narxi INTEGER NOT NULL,
        soni INTEGER NOT NULL,
        summa INTEGER NOT NULL);""")

    cur.execute("""CREATE TABLE if not exists savdo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER NULL,
        client VARCHAR NOT NULL,
        summa INTEGER NOT NULL,
        sana VARCHAR NOT NULL);""")
