
from tinydb import  Query
import tinydb as db
from tinydb.operations import delete

import os


boeken = Query()

  
#hier voeg je boeken toe of verwijdert men boeken
while True:
    result  = input("kies i of r!: ")





    if result == 'i':
        x = input('naam boek?: ')
        y = input('naam auteur?: ')
        z= input('omschrijving boek?: ')
        break
        
    elif result =='r':
        verwijder_boek = input('naam boek?: ')
        break
    
    
    else:
        print('pick i of r')
        continue











      







