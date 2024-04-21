
import HospitalApp.validators.TypeValidator as validators
import HospitalApp.service.EmployerService as adminService



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



