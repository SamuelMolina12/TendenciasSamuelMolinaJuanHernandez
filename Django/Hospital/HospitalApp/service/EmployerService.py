import HospitalApp.models as models




def createUser(name,id,genre,mail,telephone,birth,address,role,userName,password):
    user=models.Employer.objects.filter(id=id)
    if user.exists():
        raise Exception("ya existe una persona con esa cedula registrada")
    user=models.Employer.objects.filter(userName=userName)
    if user.exists():
        raise Exception("ya existe un usuario con ese user name")
    user=models.Employer(id,name,genre,mail,telephone,birth,address,role,userName,password)
    user.save()




def getUsers():
    employers = models.Employer.objects.all()
    if employers:
        return employers
    else:
        raise Exception("No hay  empleados para mostrar")

def getUser(id):
    employer = models.Employer.objects.filter(id=id).first()
    if employer:
        return employer
    else:
        raise Exception("No hay un empleado con ese id")



def deleteUser(id):
    employer = models.Employer.objects.filter(id=id).first()
    if employer:
        employer.delete()
    else:
        raise Exception("Empleado no encontrado")


def updateUser(id, name, mail,genre, telephone, birth, address, role, userName, password):
    employer = models.Employer.objects.filter(id=id).first()
    if employer:
        employer.name = name
        employer.genre = genre
        employer.mail = mail
        employer.telephone = telephone
        employer.birth = birth
        employer.address = address
        employer.role = role
        employer.userName = userName
        employer.password = password
        employer.save()
    else:
        raise Exception("Empleado no encontrado")
