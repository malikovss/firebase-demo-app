import os

import firebase_admin
from firebase_admin import messaging

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "serviceAccountKey.json"
default_app = firebase_admin.initialize_app()
message = messaging.Message(notification=messaging.Notification(
    title='title',
    body='body',
    image='https://i.dummyjson.com/data/products/10/1.jpg',
),
    token='device-token')
messaging.send(message)
