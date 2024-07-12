import sqlite3

connection = sqlite3.connect('user.db')

cursor = connection.cursor()

create_table_query = """
    CREATE TABLE IF NOT EXISTS users(
        id integer primary key,
        first_name text,
        last_name text,
        phone_number text
    ); 
"""


cursor.execute(create_table_query)
connection.commit()
connection.close()  #dar akhar bayad hatman DB ra bebandim

sample_data_query = """
    INSERT INTO users(id , first_name , last_name , phone_number )
    VALUES ( ? , ? , ? , ? )
"""

sample_data = [(1544 , "Mahan" , "Mazaheri" , "123456789"),
               (4567 , "Homa" , "Lotfi" , "123456789"),
               (7865 , "Shayan" , "Mazaheri" , "123456789"),
               (7878 , "Parsa" , "Abdolkarimi" , "123456789"),]

# with sqlite3.connect('user.db') as connection:
#     cursor = connection.cursor()
#     # cursor.execute(sample_data_query,sample_data) --> baraye tak data az in estefadeh mishe
#     cursor.executemany(sample_data_query,sample_data)

#zamani ke az with estefade mikonim 

fetch_data_query = """
    SELECT id, first_name , last_name , phone_number FROM users
"""

rows = []

with sqlite3.connect('user.db') as connection:
    cursor = connection.cursor()
    cursor.execute(fetch_data_query)
    rows = cursor.fetchall()

for row in rows:
    print(f"ID:{row[0]} , FN:{row[1]} , LN:{row[2]} , PN:{row[3]}")