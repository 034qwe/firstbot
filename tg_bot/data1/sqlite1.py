import sqlite3 as sq



def data_start():
    global base,curs
    base = sq.connect('my_isq_bot.db')
    curs = base.cursor()
    if base:
        print('data1 connect')
    base.execute('CREATE TABLE IF NOT EXISTS data1(photo TEXT, name TEXT PRIMARY KEY,category TEXT)')
    base.commit()
    base.execute("""CREATE TABLE IF NOT EXISTS data2(id INTEGER PRYMARY KEY)""")
    base.commit()

async def sql_add(state):
    async with state.proxy() as data:
        curs.execute('INSERT INTO data1 VALUES (?,?,?)',tuple(data.values()))
        print('complete add in data')     
        base.commit()

async def sql_add2(text):
        curs.execute(f'INSERT INTO data2 VALUES({text})')
        print('complete add in data')     
        base.commit()

async def id_admin():      
    a = base.execute("""SELECT id FROM data2""")
    lst = []
    for i in a:
        lst.append(*i)
    return lst   