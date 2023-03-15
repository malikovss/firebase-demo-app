import os

import firebase_admin
from firebase_admin import messaging

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
default_app = firebase_admin.initialize_app()
message = messaging.Message(
    data={'test': 'test', 'language': 'uz'},
    notification=messaging.Notification(
        title='title',
        body='body',
        image='https://i.dummyjson.com/data/products/10/1.jpg',
    ),
    token='eQwo94QrT6mAcxZ-EiE5vq:APA91bHhZrFLXgzHORjpg02eF-P9e-Bxalw7YGvni-3xwPFFrZ6U948rp-5iwxdbzURBJHnpoTBCCKW2q8FSie_fMocOb7vwVpEFyLEY5lfMtJADWXciDzQHI2r2myGKgLyiMkAEdrB0')
messaging.send(message)
