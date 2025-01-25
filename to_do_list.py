import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# certifies the credentials. One time use to initialize credentials before using the database
cred = credentials.Certificate('/Users/shonashby/Downloads/to-do-list-tracker-ac8d0-61d2abcc605a.json')
app = firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection("To-do List")

def Start():
    print("Welcome to the To-Do list tracker to get started:")
    name = input("What is your name? ")
    print("Welcome " + name + " to begin do you wish to A) add items to your To-Do list, B) Alter an item, C) delete or complete an item, or D) to view an item in your to-do list (Note make sure to have the name of the task)?")
    answer = input("(Please type A, B, C, or D) ")
    if answer.lower() == "a":
        Add()
    
    if answer.lower() == "b":
        overwrite()
    
    if answer.lower() == "c":
        
        delete()
    
    if answer.lower() == "d":
        view()

#adds tasks to the to-do list, using input to take those tasks and adding them to database
def Add():
    user = input("What are you calling today's task? ")
    doc_ref = db.collection("To-do List").document(user)

    task = input("What task do you wish to add? (Please give a description not just a name) ")
    doc_ref.set({"Task" : task})

#overwrites selected document task in database and changes it to given input
def overwrite():
    user = input("What is the task name you are overwriting today? ")
    doc_ref = db.collection("To-do List").document(user)
    change = input("What are you changing the task to? ")
    doc_ref.update({"Task" : change})
    
#deletes task within database
def delete():
    user = input("What item are you deleting? ")
    doc_ref = db.collection("To-do List").document(user)
    doc_ref.delete()

def view():
    user = input("What item would you like to view? ")
    doc_ref = db.collection("To-do List").document(user)

    doc = doc_ref.get()

    if doc.exists:
        print(doc.to_dict())
    else:
        print("That task does not exist please try a different name or try a new task.")

Start()