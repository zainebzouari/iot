import firebase_admin
from firebase_admin import credentials, storage


cred = credentials.Certificate("iot-project-df5b3-firebase-adminsdk-n31x9-c0b5422442.json")  
firebase_admin.initialize_app(cred, {'storageBucket': 'iot-project-df5b3.appspot.com'})  

bucket = storage.bucket()

image = "image.png"
firebase = "ImageF.png"  

send = bucket.blob(firebase)
send.upload_from_filename(image)