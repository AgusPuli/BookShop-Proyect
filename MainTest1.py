import sqlite3
#code by AgusPuli

connection = sqlite3.connect('mi_base_de_datos.db')
cursor = connection.cursor()

print("Conexión establecida.")


#def space
def EliminarTotal():        #delet libros info
    cursor.execute('''
    delete from Base
    ''')
    connection.commit()


def creartabla():               #crea la tabla primaria
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Base (
        id INTEGER PRIMARY KEY,
        articulo TEXT,
        stock INTEGER,
        precio FLOAT
    )
    ''')
    print("Tabla creada.")

    connection.commit()




def AgregarPersonalizado(articulo,stock,precio):
    cursor.execute('''
    insert into Base(articulo, stock, precio)
    VALUES (?,?,?)
    ''',(articulo,stock,precio))
    connection.commit()
    print("Registro insertado.")





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

def AumentarPrecio(articuloaux, num):
    cursor.execute('''
    update Base
    set precio= precio+precio*(?/100)
    where articulo=?
    ''',(num,articuloaux))
    connection.commit()
#creartabla()
#Agregarbasic()
#AgregarLista()
#AgregarPersonalizado("aladin","hernan",3000,"puli")
#EliminarTotal()
print("Enter:1 to create table ")
print("Enter:2 to add articulo ")
print("Enter:3 to delete all info from Base ")
print("Enter:any else to quit")

while True:
    election=int(input("ingrese el numero: "))
    if election == 1:
        creartabla()
    elif election == 2:
        print()
        articuloaux,stockaux,precioaux=str(input("Ingrese el articulo: ")),int(input("Ingrese el stock: ")),float(input("Ingrese el precio: "))
        AgregarPersonalizado(articuloaux,stockaux,precioaux)
    elif election == 3:
        EliminarTotal()
    elif election == 4:
        articulo=str(input("Ingrese el articulo: "))
        AumentarPrecio(articulo,100)
    else:
        break





connection.close()
print("Conexión cerrada.")
