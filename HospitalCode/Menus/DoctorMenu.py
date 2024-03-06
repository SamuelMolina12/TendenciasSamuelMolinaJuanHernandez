from Validators import DoctorTypeValidator

# def checkPatient(hospital,id):
#     DoctorTypeValidator.checkPatientExistence(hospital)
#     print(id)
#     doctorMenu(hospital,id)


def doctorMenu(hospital):
    while True:
        
        option = input("1. Mostrar paciente \n2. Agregar historia clinica \n3. Agregar historia clinica \n4. Editar historia clinica \n5. cerrar sesion\n")
        if option == "1":
            id = int(input("Ingrese el ID del paciente: "))
            showPatient(hospital,id)
        elif option == "2":
            print("show")                
        elif option == "3":
            print("add")
        elif option == "4":
            print("editar")
            return    
        elif option == "5":
            print("Cerrando sesión")
            return
        else:
            print("Opción inválida. Intente de nuevo.")

def showPatient(hospital,id):
    try:
        DoctorTypeValidator.showPatient(hospital,id)
    except Exception as error:
        print(str(error))            