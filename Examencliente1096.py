# Examen Nava 22308051281096
class Cliente1096:
    ## Atributos
    id = 0
    Nombre = ""
    Membresia = ""
    Fecha_nac = 0
    Telefono = 0
    Correo = ""
    Curp = ""
    ## Funcion para mostrar datos
    def MostrarDatos(self, id, Nombre, Membresia, Fecha_nac, Telefono, Correo, Curp):
        print("Resultados para clientes")
        print(f"Id del Cliente {id}")
        print(f"Nombre del Cliente {Nombre}")
        print(f"Membresia del Cliente {Membresia}")
        print(f"Fecha nac del Cliente {Edad}")
        print(f"Telefono del Cliente {Telefono}")
        print(f"Correo del Cliente {Correo}")
        print(f"Curp del Cliente {Curp}")
    ## Funcion para mostrar la lista cliente
    def listar_Cliente(self):
        print("Lista Cliente")
        ListaCliente = ["Cristian","Kevin","Karen","Roberto","Casandra"]
        for x in ListaCliente:
            print(x)
    ## Funcion para mostrar Tupla cliente
    def Tupla_Clientes(self):
        print("Tupla Cliente")
        TuplaCliente = ("Rosio","Alfredo","Javier","Juan","Carlos")
        for x in TuplaCliente:
            print(x)
    ## Funcion para mostrar Diccionario Cliente
    def Dicc_Clientes(self):
        print("Dicc Cliente")
        DiccCli = {"Romo" : "VIP",
                    "Emilio" : "MVP",
                    "Edwin" : "SENIOR" , 
                    "Miriam" : "PRO",
                    "Edgar" : "GUEST"}
        for x,y in DiccCli.items():
            print(x,y)
    ## Funcion para mostrar Funcion altas
    def Altas(self):
        print("Operacion realizada para la clase cliente con exito")
    ## Funcion para mostrar Funcion Bajas
    def bajas(self):
        print("Datos borrados con exito")
## Uso de los objetos
Objeto=Cliente1096()
Objeto2=Cliente1096()
Objeto.id=1
Objeto.Nombre="Cristian"
Objeto.Membresia="VIP"
Objeto.Fecha_nac=17
Objeto.Telefono=6563194064
Objeto.Correo="a.22308051281096@cbtis128.edu.mx"
Objeto.Curp="UYWL240820HOCTJZ41"
print("---------------------------------")
## Uso de las funciones con el objeto
Objeto.MostrarDatos(Objeto.id,Objeto.Nombre,Objeto.Membresia,Objeto.Fecha_nac,
                    Objeto.Telefono,Objeto.Correo,Objeto.Curp)
print("---------------------------------")

Objeto2.listar_Cliente()
print("---------------------------------")
Objeto2.Tupla_Clientes()
print("---------------------------------")
Objeto2.Dicc_Clientes()
print("---------------------------------")
Objeto2.Altas()
print("---------------------------------")
Objeto2.bajas()
print("---------------------------------")
