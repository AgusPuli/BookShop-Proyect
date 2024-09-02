import sqlite3
#code by AgusPuli

connection = sqlite3.connect('mi_base_de_datos.db')
cursor = connection.cursor()

print("Conexión establecida.")


#def space

#   F_Elimina la tabla
def EliminarTotal():
    cursor.execute('''
    delete from Base
    ''')
    connection.commit()

#   F_Crea la tabla
def creartabla():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Base (
        id INTEGER PRIMARY KEY,
        articulo TEXT,
        precio FLOAT,
        stock INTEGER
        
    )
    ''')

    print("Tabla creada.")
    connection.commit()



#   F_Agregar un articulo
def AgregarPersonalizado(articulo,stock,precio):
    cursor.execute('''
    insert into Base(articulo, stock, precio)
    VALUES (?,?,?)
    ''',(articulo,stock,precio))
    connection.commit()
    print("Registro insertado.")




# F_Mostrar     //Sin Uso por ahora



#   F_Elimina un elemento
def EliminarArticulo(articulo):
    if False:
        cursor.execute('''
        DELETE FROM Base
        WHERE articulo = ?
        ''',(articulo,))

        connection.commit()
        print("Articulo eliminado.")


#   F_Aumentar porecio por oporcentaje
def AumentarPrecio(articuloaux, num):
    cursor.execute('''
    select precio from Base
    where articulo=?
    ''',(articuloaux,))
    precio = (cursor.fetchone())[0]
    precio=precio+precio*(num/100)

    cursor.execute('''
    update Base
    set precio= ?
    where articulo=?
    ''',(precio, articuloaux))
    connection.commit()
#creartabla()
#Agregarbasic()
#AgregarLista()
#AgregarPersonalizado("aladin","hernan",3000,"puli")
#EliminarTotal()


#   F_Manejode datos
def Menu():
    while True:
        print()
        print()
        print("Ingrese 1 para crear una nueva tabla \nIngrese 2 para añadir un articulo o aumentar su precio\nIngrese 3 para eliminar un articulo o disminuir su precio")
        election = int(input("ingrese el numero: "))
        if election == 1:
            creartabla()

        elif election == 2:
            election = int(input("Ingrese 1 para añadir un articulo o 2 para aumentar su precio"))

            if election == 1:
                articuloaux, stockaux, precioaux = (str(input("Ingrese el articulo: ")),
                int(input("Ingrese el stock: ")), float(input("Ingrese el precio: ")))
                AgregarPersonalizado(articuloaux, stockaux, precioaux)

            elif election == 2:
                articulo, aumento = str(input("Ingrese el articulo: ")), int(
                input("Ingrese el porcentaje de aumento sin el simbolo -%: "))
                AumentarPrecio(articulo, aumento)


        elif election == 3:
            election = int(input("Ingrese 1 para eliminar un articulo o 2 para eliminar todo el contenido de la tabla"))
            if election == 1:
                EliminarArticulo(str(input("ingrese el articulo a eliminar")))

            elif election == 2:
                EliminarTotal()

        else:
            break

# F_Cajero
def MainFunction():
    print("iniciando Uso Normal")
    while True:
        ProductList = []
        while True:
            try:
                var = str(input("ingrese el nombre del articulo: "))
                cursor.execute('''
                select precio from Base
                where articulo = ?''',(var,))
                num = cursor.fetchone()[0]
                ProductList.append(num)
            except Exception as e:
                print(e)
                break
        resultado = sum(ProductList)
        print(f"El precio final es: {resultado}")
        election = int(input("Ingrese 1 si quiere volver a inciiar La funcion de escaneo: "))
        if election != 1:
            break


Menu()
MainFunction()

connection.close()
print("Conexión cerrada.")
