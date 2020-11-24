
from tinydb import TinyDB, Query

db = TinyDB('db.json')

Boek = Query()

  
#hier voeg je boeken toe of verwijdert men boeken
while True:
    result  = input("kies i of r (c om te sluiten): ")
    

    if result == 'i':
        naam_boek = input('naam boek?: ')
        auteur = input('naam auteur?: ')
        omschrijving = input('omschrijving boek?: ')

        db.insert({'naamBoek': naam_boek, 'auteur': auteur, 'omschrijving': omschrijving})
        
    elif result =='r':
        verwijder_boek = input('naam boek?: ')

        gezocht_boek = db.search(Boek.naamBoek == verwijder_boek)

        if len(gezocht_boek) == 1:
            db.remove(Boek.naamBoek == verwijder_boek)
        else:
            print('Boek bestaat niet!')


    elif result =='c':
        break
    
    else:
        print('pick i of r')















