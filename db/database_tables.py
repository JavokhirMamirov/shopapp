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
        price REAL NOT NULL
    );""")