
import HospitalApp.validators.TypeValidator as validators
import HospitalApp.service.EmployerService as adminService



def createUser( name, id, genre, mail, telephone, birth, address, role, userName, password):
    # print("Ingreso a la creacion del rol " + role)
    validators.textValidator(name,"nombre  \n")
    id=validators.numberValidator(id,"id" )

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
    validators.numberValidator(id,"id")
    return adminService.getUser(id)

def getUsers():
    return adminService.getUsers()

def deleteUser(id):
    validators.numberValidator(id,"id" )
    return adminService.deleteUser(id)
 
def updateUser(id, name, genre, mail, telephone, birth, address, role, userName, password):
    validators.numberValidator(id,"id" )
    validators.textValidator(name,"nombre  \n")

    validators.textValidator(userName,"usuario de   \n" )
    validators.usernameValidator(userName,"usuario de    \n" )

    validators.textValidator(genre, "genero de    \n")
    validators.genreValidator(genre, "genero de    \n")

    validators.textValidator(mail, "correo de   \n")
    validators.emailValidator(mail, "correo de    \n")

    validators.phoneValidator(telephone, "numero telefono")

    birth=validators.dateValidator(birth,"fecha de nacimiento de")
   
   
    validators.textValidator(address, "direccion de    \n")
    validators.addressValidator(address, "direccion de  \n")

    validators.textValidator(role, "rol de \n")
   
    password=validators.passwordValidator(password, "contraseña de \n")

    return adminService.updateUser(id, name, genre, mail, telephone, birth, address, role, userName, password)




def login(username,password):
    validators.textValidator(username,"usuario o contraseña incorrecto")
    validators.textValidator(password,"usuario o contraseña incorrectos")
    return adminService.login(username,password)

def getSession(token):
    validators.textValidator(token,"token incorrecto")
    return adminService.getSession(token)

#especialista

def createSpecialist( nameSpecialist):
    # print("Ingreso a la creacion del rol " + role)
    validators.textValidator(nameSpecialist,"nombre especialista \n")
    adminService.createSpecialist( nameSpecialist)

def getSpecialist(id):
    return adminService.getSpecialist(id)

def getSpecialists():
    return adminService.getSpecialists()

def deleteSpecialist(id):
    return adminService.deleteSpecialist(id) 

def updateSpecialist(id, nameSpecialist):
    validators.textValidator(nameSpecialist,"nombre  \n")   
    return adminService.updateSpecialist(id, nameSpecialist)