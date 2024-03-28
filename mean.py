import sqlite3

def execute_queries():
    # Conexión a la base de datos
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Obtener la lista de archivos SQL de consultas en el directorio actual
    pregunta_files =['pregunta_01.sql','pregunta_02.sql','pregunta_03.sql','pregunta_04.sql'
                     , 'pregunta_05.sql', 'pregunta_06.sql', 'pregunta_07.sql', 'pregunta_08.sql',
                     'pregunta_09.sql', 'pregunta_10.sql', 'pregunta_11.sql', 'pregunta_12.sql'
                     , 'pregunta_13.sql', 'pregunta_14.sql']

    # Ejecutar las consultas en cada archivo
    for file in pregunta_files:
        with open(file, 'r') as f:
            queries = f.read()

        # Ejecutar las consultas una por una
        for query in queries.split(';'):
            cursor.execute(query)
            # Imprimir los resultados de cada consulta
            print(cursor.fetchall())

    # Cierra la conexión
    conn.close()

if __name__ == "__main__":
    execute_queries()