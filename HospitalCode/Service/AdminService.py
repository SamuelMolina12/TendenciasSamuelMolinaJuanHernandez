import Models.models as models

def validateId(vet,id):
    for person in vet.persons:
        if person.id==id:
            return person
    return None
def validateUserName(vet,userName):
    for person in vet.persons:
        if person.userName==userName:
            return person
    return None

def createAdmin(hospital,name,id,genre,mail,telephone,birth,address,role,userName,password):
    user=validateId(hospital,id)
    if user:
        raise Exception("ya existe una persona con esa cedula registrada")
    user=validateUserName(hospital,userName)
    if user:
        raise Exception("ya existe un usuario con ese user name")
    user=models.Employer(name,id,genre,mail,telephone,birth,address,role,userName,password)
    hospital.persons.append(user)

def deleteUser(hospital,id):
    for user in hospital.persons:
        if user.id == id:
            return True
    return False

def updateUser(hospital,id):
    for user in hospital.persons:
        if user.id == int(id):
            return user
    return None
  