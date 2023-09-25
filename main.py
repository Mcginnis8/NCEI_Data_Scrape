import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



def fireBaseInit():
    cred = credentials.Certificate("cred_config.json")
    firebase_admin.initialize_app(cred)


def fireBasePush():
    cFS = firestore.client()
    testName = {
        "12": "bob"
    }

    doc_ref = cFS.collection(u'Test').document(u'NameTest')
    doc_ref.set(testName)


