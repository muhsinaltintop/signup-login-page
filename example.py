import json

users = {
    'people': 
        {
            'userid': '01',
            'nameLastname' : 'Muhsin Altintop',
            'username' : 'muhsinaltintop',
            'password' : '2023Muhsin.'
        }
       
    
}

print(users.get('people', 'Not Found'))
print(users.keys())
print(users.values())
print(users['people'].items())
print(len(users['people']))

for item in users['people'].items():
    print(item)

for key, value in users['people'].items():
    print(key, value)