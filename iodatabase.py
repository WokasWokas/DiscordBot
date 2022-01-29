import sqlite3, classes

__DB_PATH__ = './db'

def create_connection(dbname: str):
    return sqlite3.connect(f'{__DB_PATH__}/{dbname}.db')

def close_connection(connection: sqlite3.Connection):
    connection.close()

def create_table(connection: sqlite3.Connection, tablename: str):
    cursor = connection.cursor()
    table = {
        'log': '''CREATE TABLE log (Time text, Type text, Channel text, User text, Content text)''',
        'bank': '''CREATE TABLE bank (userid integer, value real, regtime text)'''
    }
    cursor.execute(table[tablename])

def execute(connection: sqlite3.Connection, data):
    cursor = connection.cursor()
    if data.tablename == 'log':
        execution = f"""INSERT INTO log VALUES ('{data.TimeStamp}', '{data.Type}', '{data.Channel}',
                                                 '{data.User}', '{data.Content}')"""
    elif data.tablename == 'bank':
        execution = f"""INSERT INTO bank VALUES ('{data.UserId}', '{data.Value}')"""
    cursor.execute(execution)
    connection.commit()

def get_data(connection: sqlite3.Connection, name: str, tablename: str):
    cursor = connection.cursor()
    data = cursor.execute(f'SELECT * FROM {tablename} WHERE name={name}')
    return data.fetchone()
