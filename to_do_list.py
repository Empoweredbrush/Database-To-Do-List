import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# certifies the credentials. One time use to initialize credentials before using the database
cred = credentials.Certificate('/Users/shonashby/Downloads/to-do-list-tracker-ac8d0-61d2abcc605a.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection("To-do List")

#Starts up the program, asking the user for their name to be a bit more personalized, and allows the user to choose what they wish to do with their to-do list
def Start():
    print("Welcome to the To-Do list tracker to get started:")
    name = input("What is your name? ")

    print("Welcome " + name + ", to begin do you wish to A) add items to your To-Do list, B) Alter an item, or C) delete or complete an item?")
    answer = input("(Please type A, B, or C) ")

    if answer.lower() == "a":

        Add()
    
    if answer.lower() == "b":

        overwrite()
    
    if answer.lower() == "c":
        
        delete()

#adds tasks to the to-do list, using input to take those tasks and adding them to database
def Add():
    user = input("What are you calling today's task? ")
    doc_ref = db.document(user)

    task = input("What task do you wish to add? (Please give a description not just a name) ")
    doc_ref.set({"Task" : task})

#overwrites selected document task in database and changes it to given input by the user
def overwrite():
    user = input("What is the task name you are overwriting today? ")
    doc_ref = db.collection("To-do List").document(user)
    doc_ref.delete()

    new_name = input("What will be the new name of the task? ")
    change = input("What are you changing the task to? ")
    db.collection("To-do List").document(new_name).set({"Task" : change})

    

#deletes task within database
def delete():
    user = input("What item are you deleting? ")
    doc_ref = db.collection("To-do List").document(user)
    doc_ref.delete()


Start()