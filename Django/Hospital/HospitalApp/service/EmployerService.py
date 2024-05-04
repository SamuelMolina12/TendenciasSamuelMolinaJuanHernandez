import HospitalApp.models as models
import string,secrets



def createUser(name,id,genre,mail,telephone,birth,address,role,userName,password):
    user=models.Employer.objects.filter(id=id)
    if user.exists():
        raise Exception("ya existe una persona con esa cedula registrada")
    patient=models.Patient.objects.filter(id=id)
    if patient.exists():
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
    user = models.Employer.objects.filter(userName=userName).exclude(id=id)
    if user.exists():
        raise Exception("Ya existe un usuario con ese nombre de usuario")


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


def login(user,password):
    try:
        user=models.Employer.objects.get(userName=user)
    except:
        raise Exception("usuario o contraseña no existe")
    if user.password!=password:
        raise Exception("usuario o contraseña incorrectos")
    activeSession = models.Session.objects.filter(user=user)
    if activeSession.exists():
        raise Exception("ya se detecto una sesion activa")
    chars = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(chars) for _ in range(128))
    session=models.Session()
    session.user=user
    session.token=token
    session.save()
    return session


def getSession(token):
    try:
        return models.Session.objects.get(token = token)
    except:
        raise Exception("token no existe")
    
    
#especialista

def createSpecialist(nameSpecialist):
   
    user=models.Specialist.objects.filter(nameSpecialist=nameSpecialist)
    if user.exists():
        raise Exception("ya existe un usuario con ese user name")
    user=models.Specialist(nameSpecialist=nameSpecialist)
    user.save()    

def getSpecialists():
    Specialists = models.Specialist.objects.all()
    if Specialists:
        return Specialists
    else:
        raise Exception("No hay especialista para mostrar")

def getSpecialist(id):
    Specialist = models.Specialist.objects.filter(id=id).first()
    if Specialist:
        return Specialist
    else:
        raise Exception("No hay un especialista con ese id")
    

def deleteSpecialist(id):
    Specialist = models.Specialist.objects.filter(id=id).first()
    if Specialist:
        Specialist.delete()
    else:
        raise Exception("Especialista no encontrado")
    
def updateSpecialist(id, nameSpecialist):
    Specialist = models.Specialist.objects.filter(id=id).first()
    if Specialist:
        Specialist.nameSpecialist = nameSpecialist
        
        Specialist.save()
    else:
        raise Exception("Especialista no encontrado")    