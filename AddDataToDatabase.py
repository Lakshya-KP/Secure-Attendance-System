import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-2a4e2-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')
data = {}

with open('students.json', 'r') as f:
    new_data = json.load(f)

# Add new data to existing data dictionary
data.update(new_data)

# Print the updated data dictionary
print(data)


for key,value in data.items():
    ref.child(key).set(value)







