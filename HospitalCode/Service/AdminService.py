import Models.Models as Models

def validateId(hospital,id):
    for person in hospital.persons:
        if person.id==id:
            return person
    return None
def validateUserName(hospital,username):
    for person in hospital.persons:
        if person.username==username:
            return person
    return None

def createAdmin(hospital,name,id,genre,mail,telephone,birth,address,role,username,password):
    user=validateId(hospital,id)
    if user:
        raise Exception("ya existe una persona con esa cedula registrada")
    user=validateUserName(hospital,username)
    if user:
        raise Exception("ya existe un usuario con ese user name")
    user=Models.Employer(name,id,genre,mail,telephone,birth,address,role,username,password)
    hospital.persons.append(user)