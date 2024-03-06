from Validators import NurseTypeValidator

def nurseMenu(hospital,user):
    while True:
        
        option = input("1. Mostrar paciente \n2. Mostar historia de visitas del paciente \n3. Agregar historia de visitas \n4. Editar historia de visitas \n5. cerrar sesion\n")
        if option == "1":
            id = int(input("Ingrese el ID del paciente: "))
            showPatient(hospital,id)
        elif option == "2":
           
            print("editar")
        elif option == "3":
            id = int(input("Ingrese el ID del paciente: "))
            createHistoryVisitsQuery(hospital,id)                        
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
        NurseTypeValidator.showPatient(hospital,id)
    except Exception as error:
        print(str(error))              

def createHistoryVisitsQuery(hospital,id):
    try:
        NurseTypeValidator.createHistoryVisitsQuery(hospital,id)
        print("se creo nueva visita correctamente")
    except Exception as error:
        print(str(error))     