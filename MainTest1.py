import sqlite3

connection = sqlite3.connect('mi_base_de_datos.db')
cursor = connection.cursor()

print("Conexión establecida.")


#def space
def EliminarTotal():
    cursor.execute('''
    delete from libros
    ''')
    connection.commit()
def creartabla():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS libros (
        id INTEGER PRIMARY KEY,
        titulo TEXT,
        puli TEXT,
        autor TEXT,
        precio REAL
    )
    ''')

    connection.commit()


def Agregarbasic():
    cursor.execute('''
    INSERT INTO libros (titulo, autor, precio, puli)
    VALUES ('Cien Años de Soledad', 'Gabriel García Márquez', 15000.99,'si')
    ''')

def AgregarPersonalizado(titulo,autor,precio,nombre):
    cursor.execute('''
    INSERT INTO libros (titulo, autor, precio, puli)
    VALUES (?,?,?,?)
    ''',(titulo,autor,precio,nombre))
    connection.commit()
    print("Registro insertado.")


def AgregarLista():
    libros = [
        ('Don Quijote de la Mancha', 'Miguel de Cervantes', 12.99),
        ('El Principito', 'Antoine de Saint-Exupéry', 8.99),
        ('1984', 'George Orwell', 14.99)
    ]

    cursor.executemany('''
    INSERT INTO libros (titulo, autor, precio)
    VALUES (?, ?, ?)
    ''', libros)

    connection.commit()

    print("Varios registros insertados.")

def PrintTablas():
    cursor.execute('SELECT * FROM libros')
    libros = cursor.fetchall()

    for libroff in libros:
        print(libroff)

def EliminarTitulo():
    if False:
        cursor.execute('''
        DELETE FROM libros
        WHERE titulo = 'Cien Años de Soledad'
        ''')

        connection.commit()

#creartabla()
#Agregarbasic()
#AgregarLista()
#AgregarPersonalizado("aladin","hernan",3000,"puli")
#EliminarTotal()
print("Enter:1 to ")
print("Enter:1 to ")
print("Enter:1 to ")
print("Enter:1 to ")

while True:
    election=int(input("ingrese el numero: "))
    if election == 1:
        creartabla()
    elif election == 2:
        AgregarPersonalizado("hola","hola",3500,"hola")
    elif election == 3:
        EliminarTotal()
    else:
        break





connection.close()
print("Conexión cerrada.")
