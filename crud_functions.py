import sqlite3



def initiate_db():

    connection = sqlite3.connect('product.db')
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL);
    """)

    for i in range(1, 10):

        check_prod = cursor.execute('SELECT * FROM Products WHERE id = ?', (i, ))

        if check_prod.fetchone() is None:
            cursor.execute(f'''INSERT INTO Products VALUES("{i}", "Продукт {i}", "Описание {i}", {i * 100})''')

    connection.commit()
    connection.close()

def get_all_products():

    connection = sqlite3.connect('product.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products GROUP BY id')
    product_all = cursor.fetchall()

    connection.commit()
    connection.close()

    return product_all
