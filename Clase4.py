class Paciente:

    def __init___(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ""

    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula

    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema:
    def __init__(self):
        
        self.__lista_Pacientes= []

        self.__numero_pacientes = len(self.__lista_Pacientes)
    def ingresarPaciente(self):
        nombre= input("Ingrese Nombre: ")
        cedula= input("Ingrese ID: ")
        genero= input("Ingrese Genero: ")
        servicio= input("Ingrese Servicio: ")

        p=Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)

        self.__lista_Pacientes.append(p)

        self.__numero_pacientes = len(self.__lista_Pacientes)

    def verNumeroPaciente(self): 
        return self.__numero_pacientes
    def verDatosPaciente(self):
        cedula= int(input("Ingrese ID paciente para buscar: "))

        for paciente in self.__lista_Pacientes:
            if cedula== paciente.verCedula():

                print("Nombre: " +paciente.verNombre())
                print("Cedula: " +str(paciente.verCedula()))
                print("Genero: " + paciente.verGenero())
                print("Genero: " + paciente.verGenero())

mi_sistema = Sistema()

while True:

    opcion = int(input(" 1. Nuevo paciente \n 2. Numero de pacientes \n 3. Datos Paciente \n 4. Salir"))
    if opcion== 1:
        mi_sistema.ingresarPaciente()
    elif opcion==2:
        print("Ahora hay:" + str(mi_sistema.verNumeroPaciente()))
    elif opcion==3:
        mi_sistema.verDatosPaciente()
    elif opcion==4:
        break
    else:
        print("Opcion invalida") 

        print("subio")    
