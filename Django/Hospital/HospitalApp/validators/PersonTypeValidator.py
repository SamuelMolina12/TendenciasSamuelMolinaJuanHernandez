
import HospitalApp.validators.TypeValidator as validators
import HospitalApp.service.AdminService as adminService



def createUser( name, id, genre, mail, telephone, birth, address, role, userName, password):
    # print("Ingreso a la creacion del rol " + role)
    validators.textValidator(name,"nombre  \n")
    id=validators.numberValidator(id,"cedula de " + role )

    validators.textValidator(userName,"usuario de   \n" )
    validators.usernameValidator(userName,"usuario de    \n" )

    validators.textValidator(genre, "genero de    \n")
    validators.genreValidator(genre, "genero de    \n")

    validators.textValidator(mail, "correo de   \n")
    validators.emailValidator(mail, "correo de    \n")
    telephone=validators.phoneValidator(telephone, "numero telefono")
    birth=validators.dateValidator(birth,"fecha de nacimiento de")
   
   
    validators.textValidator(address, "direccion de    \n")
    validators.addressValidator(address, "direccion de  \n")

    validators.textValidator(role, "rol de \n")
   
    password=validators.passwordValidator(password, "contraseña de \n")

    adminService.createUser( name, id, genre, mail, telephone, birth, address, role, userName, password)
    
def getUser(id):
    return adminService.getUser(id)

def getUsers():
    return adminService.getUsers()

def deleteUser(id):
    return adminService.deleteUser(id)
 
def updateUser(id, name, genre, mail, telephone, birth, address, role, userName, password):
    validators.textValidator(name,"nombre  \n")

    validators.textValidator(userName,"usuario de   \n" )
    validators.usernameValidator(userName,"usuario de    \n" )

    validators.textValidator(genre, "genero de    \n")
    validators.genreValidator(genre, "genero de    \n")

    validators.textValidator(mail, "correo de   \n")
    validators.emailValidator(mail, "correo de    \n")
    telephone=validators.phoneValidator(telephone, "numero telefono")
    birth=validators.dateValidator(birth,"fecha de nacimiento de")
   
   
    validators.textValidator(address, "direccion de    \n")
    validators.addressValidator(address, "direccion de  \n")

    validators.textValidator(role, "rol de \n")
   
    password=validators.passwordValidator(password, "contraseña de \n")

    return adminService.updateUser(id, name, genre, mail, telephone, birth, address, role, userName, password)



# def updateUser(hospital, id):
#     try:
        
#         user = adminService.updateUser(hospital, id)
#         if user:
#             print("Usuario encontrado. Introduzca los nuevos datos:")
#             newName = input("Ingrese el nuevo nombre (presione Enter para mantener el mismo): ")
#             newGenre = input("Introduzca: masculino o femenino// Ingrese el nuevo género o presione Enter para mantener el mismo: ")
#             newMail = input("Ingrese el nuevo correo electrónico (dominio y el @): ")
#             newTelephone = input("Ingrese el nuevo número de teléfono (debe contener entre 1 y 10 dígitos): ")
#             newBirth = input("Ingrese la nueva fecha de nacimiento (formato DD/MM/YYYY): ")
#             newAddress = input("Ingrese la nueva dirección (máximo 30 caracteres): ")
#             newUserName = input("Ingrese el nuevo nombre de usuario (máximo 15 caracteres, solo letras y números): ")
#             newPassword = input("Ingrese la nueva contraseña (8 caracteres, un número, una letra mayúscula y un carácter especial): ")
#             #update_successful = True

#             if newName:
#                 validators.textValidator(newName,"el nuevo nombre \n")
#                 user.name = newName
#             if newGenre:
#                 validators.genreValidator(newGenre, "género")
#             if newMail:
#                 newMail=validators.emailValidator(newMail, "correo electrónico")
#             if newTelephone:
#                 newTelephone=validators.phoneValidator(newTelephone, "nuevo número de teléfono")
#             if newBirth:
#                 newBirth=validators.dateValidator(newBirth, "nueva fecha de nacimiento")
#             if newAddress:
#                 newAddress=validators.addressValidator(newAddress, "dirección")
#             if newUserName:
#                 newUserName=validators.usernameValidator(newUserName, "nombre de usuario")
              
            

            
#             #user.name = newName if newName else user.name
#             user.genre = newGenre if newGenre else user.genre
#             user.mail = newMail if newMail else user.mail
#             user.telephone = newTelephone if newTelephone else user.telephone
#             user.birth = newBirth if newBirth else user.birth
#             user.address = newAddress if newAddress else user.address
#             user.userName = newUserName if newUserName else user.userName
            

#             if newPassword:
#                 newPassword=validators.passwordValidator(newPassword, "contraseña")
#                 user.password = newPassword if newPassword else user.password      


            
            
#             #if update_successful:
#             print("Usuario actualizado correctamente.")
#             #else:
#              #print("No se pudieron actualizar todos los campos debido a errores de validación.")
#         else:
#             print("No se encontró ningún usuario con ese ID.")
#     except Exception as error:
#         print(str(error))





  