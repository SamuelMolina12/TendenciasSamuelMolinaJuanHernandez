def searchUser(hospital,username):
    for person in hospital.persons:
        if person.username==username:
            return person
    return None