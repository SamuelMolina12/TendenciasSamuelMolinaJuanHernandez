
import Validators.TypeValidator as validators
import Service.AdminService as adminService



def createUser(hospital,role):
    print("Ingreso a la creacion del rol " + role)
    name=input("ingrese el nombre \n")
    validators.textValidator(name,"nombre  \n")
    id=validators.numberValidator(input("ingrese la cedula  \n"), "cedula de " + role )
    userName=input("ingrese el usuario  " + "máximo 15 caracteres, solo debe contener letras y numeros \n")
    validators.textValidator(userName,"usuario de   \n" )
    validators.usernameValidator(userName,"usuario de    \n" )
    genre=input("ingrese el genero: masculino o femenino \n")
    validators.textValidator(genre, "genero de    \n")
    validators.genreValidator(genre, "genero de    \n")
    mail=input("ingrese el correo " + " dominio y el @ \n")
    validators.textValidator(mail, "correo de   \n")
    validators.emailValidator(mail, "correo de    \n")
    telephone=validators.phoneValidator(input("ingrese el numero telefonico " + "Debe contener entre 1 y 10 dígitos\n"), "numero telefono")
    birth=validators.dateValidator(input("ingrese la fecha de nacimiento " + "Formato DD/MM/YYYY, max 150 años\n"),"fecha de nacimiento de")
    address=input("ingrese la direccion " + "Máximo 30 caracteres  \n")
    validators.textValidator(address, "direccion de    \n")
    validators.addressValidator(address, "direccion de  \n")
    role=role
    validators.textValidator(role, "rol de \n")
    password=input("Ingrese la contraseña  " + "8 caracteres, un numero, 1 letra Mayuscula y 1 caracter especial \n")
    validators.passwordValidator(password, "contraseña de \n")
    adminService.createUser(hospital, name, id, genre, mail, telephone, birth, address, role, userName, password)
    
def showUsers(hospital, role):
    users = adminService.findUsersByRole(hospital, role)
    if users:
        for user in users:
            print(f"Nombre: {user.name}")
            print(f"Cedula: {user.id}")
            print(f"Genero: {user.genre}")
            print(f"Email: {user.mail}")
            print(f"Telefono: {user.telephone}")
            print(f"Fecha de nacimiento: {user.birth}")
            print(f"Direccion: {user.address}")
            print(f"Rol: {user.role}")
            print(f"Usuario: {user.userName}")
            print("")
    else:
        print("No se encontraron usuarios con ese rol.")




def deleteUser(hospital, id):
    id = int(id)
    if adminService.deleteUser(hospital, id):
        deleteUser2(hospital, id)
    else:
        print("No se encontró ningún usuario con esa identificación.")

def deleteUser2(hospital, id):
    for i, user in enumerate(hospital.persons):
        if user.id == id:
            del hospital.persons[i]
            print("Usuario eliminado exitosamente.")
            return
def updateUser(hospital, id):
    try:
        
        user = adminService.updateUser(hospital, id)
        if user:
            print("Usuario encontrado. Introduzca los nuevos datos:")
            newName = input("Ingrese el nuevo nombre (presione Enter para mantener el mismo): ")
            newGenre = input("Introduzca: masculino o femenino// Ingrese el nuevo género o presione Enter para mantener el mismo: ")
            newMail = input("Ingrese el nuevo correo electrónico (dominio y el @): ")
            newTelephone = input("Ingrese el nuevo número de teléfono (debe contener entre 1 y 10 dígitos): ")
            newBirth = input("Ingrese la nueva fecha de nacimiento (formato DD/MM/YYYY): ")
            newAddress = input("Ingrese la nueva dirección (máximo 30 caracteres): ")
            newUserName = input("Ingrese el nuevo nombre de usuario (máximo 15 caracteres, solo letras y números): ")
            newPassword = input("Ingrese la nueva contraseña (8 caracteres, un número, una letra mayúscula y un carácter especial): ")
            #update_successful = True

            if newName:
                validators.textValidator(newName,"el nuevo nombre \n")
                user.name = newName
            if newGenre:
                validators.genreValidator(newGenre, "género")
            if newMail:
                newMail=validators.emailValidator(newMail, "correo electrónico")
            if newTelephone:
                newTelephone=validators.phoneValidator(newTelephone, "nuevo número de teléfono")
            if newBirth:
                newBirth=validators.dateValidator(newBirth, "nueva fecha de nacimiento")
            if newAddress:
                newAddress=validators.addressValidator(newAddress, "dirección")
            if newUserName:
                newUserName=validators.usernameValidator(newUserName, "nombre de usuario")
              
            

            
            #user.name = newName if newName else user.name
            user.genre = newGenre if newGenre else user.genre
            user.mail = newMail if newMail else user.mail
            user.telephone = newTelephone if newTelephone else user.telephone
            user.birth = newBirth if newBirth else user.birth
            user.address = newAddress if newAddress else user.address
            user.userName = newUserName if newUserName else user.userName
            

            if newPassword:
                newPassword=validators.passwordValidator(newPassword, "contraseña")
                user.password = newPassword if newPassword else user.password      


            
            
            #if update_successful:
            print("Usuario actualizado correctamente.")
            #else:
             #print("No se pudieron actualizar todos los campos debido a errores de validación.")
        else:
            print("No se encontró ningún usuario con ese ID.")
    except Exception as error:
        print(str(error))





  