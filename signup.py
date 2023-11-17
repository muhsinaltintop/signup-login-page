people = {
    'user1': {
        'user_id': '001',
        'nameLastname' : 'Muhsin Altintop',
        'username': 'muhsinaltintop',
        'password': '123456'
    },
     'user2': {
        'user_id': '002',
        'nameLastname' : 'Imran Altintop',
        'username': 'imranaltintop',
        'password': '234567'
    },

}
usernumber = str(int(list(people)[-1][4:])+1)
print(usernumber)


#signup
nameLastName = input("Please enter your Name and Lastname. ")
username = input("Please choose a username: ")
password = input("Please choose a password")

if nameLastName and username and password :
    people.update(
    
        {
            'user' + usernumber: {
            'user_id': '00' + usernumber,
            'nameLastname' : nameLastName,
            'username': username,
            'password': password

            }
        }
    )
else:
    print("Unsuccesful")

print(people.items())