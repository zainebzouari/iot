import firebase_admin

import RPi.GPIO as GPIO
import time
import math
from firebase_admin import credentials,auth,db

GPIO.setMode(GPIO.BCM)
cred = credentials.Certificate("iot-project-df5b3-firebase-adminsdk-n31x9-c0b5422442.json")
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {'databaseURL': 'https://iot-project-df5b3-default-rtdb.firebaseio.com/'})

ref = db.reference('/')


while True:
  temp=ref.get()
    

  print(temp['emploi']['emp1'])
  time.sleep(0.2)