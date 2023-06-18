import sqlite3

db_path = "eatup.db"

def connect_to_db(path):
    conn = sqlite3.connect(path)
    # Converting tuples to dictionaries
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

def read_eatup_by_region(region):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM eatup WHERE region = ?'
    value = region
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results

def read_eatup_by_id(id):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM eatup WHERE id = ?'
    value = id
    result = cur.execute(query,(value,)).fetchone()
    conn.close()
    return result

def insert_establishment(establishment_data):
    conn, cur = connect_to_db(db_path)
    query = 'INSERT INTO eatup (region, name, image, color, description, address, contact) VALUES (?,?,?,?,?,?,?)'
    values = (establishment_data['region'], 
              establishment_data['name'],
              establishment_data['image'], 
              establishment_data['color'], 
              establishment_data['description'],
              establishment_data['address'],
              establishment_data['contact'])
    cur.execute(query,values)
    conn.commit()
    conn.close()

def update_establishment(establishment_data):
    conn, cur = connect_to_db(db_path)
    query = "UPDATE eatup SET region=?, name=?, image=?, color=?, description=?, address=?, contact=? WHERE id=?"
    values = (establishment_data['region'], 
              establishment_data['name'],
              establishment_data['image'],
              establishment_data['color'],  
              establishment_data['description'],
              establishment_data['address'],
              establishment_data['contact'],
              establishment_data['establishment_id'])
    cur.execute(query, values)
    conn.commit()
    conn.close()

def delete_establishment(establishment_data):
    conn, cur = connect_to_db(db_path)
    query = "DELETE FROM eatup WHERE id=?"
    values = ((establishment_data['establishment_id'],))
    cur.execute(query, values)
    conn.commit()
    conn.close()