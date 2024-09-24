# Examen Nava 22308051281096
class Provedor1096:
    ## Atributos
    id = 0
    Nombre = ""
    Producto = ""
    Sucursal = ""
    Horario = ""
    Producto_Cant = 0
    Direccion = ""
    ## Funcion para mostrar datos de Provedor
    def MostrarDatos(self, id, Nombre, Producto, Sucursal, Horario, Producto_Cant, Direccion):
        print("Resultados para Provedores")
        print(f"Id del Provedor {id}")
        print(f"Nombre del Provedor {Nombre}")
        print(f"Producto del Provedor {Producto}")
        print(f"Sucursal del Provedor {Sucursal}")
        print(f"Horario del Provedor {Horario}")
        print(f"Cantidad de Producto del Provedor {Producto_Cant}")
        print(f"Direccion del Provedor {Direccion}")
    ## Funcion para mostrar la lista Provedor
    def listar_provedor(self):
        print("Lista Provedores")
        Listaprovedor = ["Nestle","Dell","Chips","Coca-Cola","Intel"]
        for x in Listaprovedor:
            print(x)
    ## Funcion para mostrar Tupla Provedor
    def Tupla_provedor(self):
        print("Tupla Provedores")
        TuplaProvedores = ("Pepsi","Faber Castle","La Michoacana","Oxxo","Del Rio")
        for x in TuplaProvedores:
            print(x)
    ## Funcion para mostrar Diccionario Provedor
    def Diccionario_Rango_Provedores(self):
        print("Diccionario_Rango_Provedores")
        Diccionario_Rango_Provedores = {"Rosas -" : "bajo",
                    "Carbajal -" : "alto",
                    "Cerna -" : "bajo" , 
                    "Batres -" : "bajo",
                    "Romero -" : "medio"}
        for x,y in Diccionario_Rango_Provedores.items():
            print(x,y)
    ## Funcion para mostrar Funcion altas
    def Altas(self):
        print("Operacion realizada para la clase Provedor con exito")
    ## Funcion para mostrar Funcion Bajas
    def bajas(self):
        print("Datos borrados con exito")
## Uso de los objetos
Objeto=Provedor1096()
Objeto2=Provedor1096()
Objeto.id=1
Objeto.Nombre="Chips"
Objeto.Producto="Papas Fritas"
Objeto.Sucursal="San Villas"
Objeto.Horario="10am a 10pm"
Objeto.Producto_Cant=724
Objeto.Direccion="Calle san antonio 1945"
print("---------------------------------")
## Uso de las funciones con el objeto
Objeto.MostrarDatos(Objeto.id,Objeto.Nombre,Objeto.Producto,Objeto.Sucursal,Objeto.Horario,Objeto.Producto_Cant,Objeto.Direccion)
print("---------------------------------")
Objeto2.listar_provedor()
print("---------------------------------")
Objeto2.Tupla_provedor()
print("---------------------------------")
Objeto2.Diccionario_Rango_Provedores()
print("---------------------------------")
Objeto2.Altas()
print("---------------------------------")
Objeto2.bajas()
print("---------------------------------")
