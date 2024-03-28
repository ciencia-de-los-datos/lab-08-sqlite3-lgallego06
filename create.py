import sqlite3

def create_tables():
    # Conexión a la base de datos (creará el archivo si no existe)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Lee el contenido del archivo create_tables.sql
    with open('create_tables.sql', 'r') as f:
        create_tables_query = f.read()

    # Ejecuta las instrucciones para crear las tablas
    cursor.executescript(create_tables_query)

    # Guarda los cambios y cierra la conexión
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
