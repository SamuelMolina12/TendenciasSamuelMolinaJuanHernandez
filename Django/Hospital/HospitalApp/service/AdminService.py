import HospitalApp.models as models




# def validateId(hospital,id):
#     for person in hospital.persons:
#         if person.id==id:
#             return person
#     return None



# def validateUserName(hospital,userName):
#     for person in hospital.persons:
#         if person.userName==userName:
#             return person
#     return None

def createUser(name,id,genre,mail,telephone,birth,address,role,userName,password):
    user=models.Employer.objects.filter(id=id)
    if user.exists():
        raise Exception("ya existe una persona con esa cedula registrada")
    user=models.Employer.objects.filter(userName=userName)
    if user.exists():
        raise Exception("ya existe un usuario con ese user name")
    user=models.Employer(id,name,genre,mail,telephone,birth,address,role,userName,password)
    user.save()

# def deleteUser(hospital,id):
#     for user in hospital.persons:
#         if user.id == id:
#             return True
#     return False

# def updateUser(hospital,id):
#     for user in hospital.persons:
#         if user.id == int(id):
#             return user
#     return None
  
# def findUsersByRole(hospital, role):
#     users = hospital.persons
#     return [user for user in users if user.role == role]
