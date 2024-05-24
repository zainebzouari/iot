import firebase_admin
from firebase_admin import credentials,auth,db

cred = credentials.Certificate("iot-project-df5b3-firebase-adminsdk-n31x9-c0b5422442.json")
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {'databaseURL': 'https://iot-project-df5b3-default-rtdb.firebaseio.com/'})


ref = db.reference('/')
ref.set({
"emploi":{
  'emp1':{"first":"1", "last":"0"}
}
})