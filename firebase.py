import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



def fireBaseInit():
    cred = credentials.Certificate("cred_config.json")
    firebase_admin.initialize_app(cred)


def fireBasePushTest(name):
    cFS = firestore.client()
    testName = {
        "12": name
    }

    doc_ref = cFS.collection(u'Test').document(u'NameTest')
    doc_ref.set(testName)

def fireBasePushPandasDataFrame(df, dataSetName):
    db = firestore.client()
    data = df.to_dict(orient='records')
    collection_ref = db.collection(dataSetName)

    row_i = 0
    for row in data:
        doc_ref = collection_ref.document(row_i)
        doc_ref.set(row)
        row_i += 1

    print(f"Dataset: '{dataSetName}' has been pushed to Firestore collection: NCEI.")

