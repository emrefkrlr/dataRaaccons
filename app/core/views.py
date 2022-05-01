from distutils.command.config import config
from django.shortcuts import render
from mongo.services import MongoService
import logging
logger = logging.getLogger(__name__)




def index(request):

    medicine_1 = {
        "medicine_id": "RR000123456",
        "common_name" : "EMRE TEST",
        "scientific_name" : "",
        "available" : "Y",
        "category": "fever"
    }
    medicine_2 = {
        "medicine_id": "RR000342522",
        "common_name" : "Fikirlier TEST",
        "scientific_name" : "",
        "available" : "Y",
        "category" : "type 2 diabetes"
    }
    try:
        x = MongoService().insert_many(db_name='EmreFikirlier', host='dataRaccoonsMongo', port='27017', username='root', password='root', collection='Market', document=[medicine_1, medicine_2])
        print(x)
    except Exception as e:
        print("\nExeption: \n{}".format(e))

    #x = collection_name.dataRaccoons.insert_many([medicine_1,medicine_2])
    # Check the count
    #count = collection_name.dataRaccoons.count()
    #print(count)

    

    # Read the documents
    med_details = MongoService().find(db_name='EmreFikirlier', host='dataRaccoonsMongo', port='27017', username='root', password='root', collection='Market', query={})

    
    
    # Print on the terminal
    for r in med_details:
        print(r["common_name"])
        

    # Update one document
    target = {'medicine_id':'RR000123456'}
    value = {'$set':{'common_name':'Fikirlier'}}
    emre = {}
    z = MongoService().update_one(db_name='EmreFikirlier', host='dataRaccoonsMongo', port='27017', username='root', password='root', collection='Market', target=target, value=value)
    
    # update_data = collection_name.dataRaccoons.update_one({'medicine_id':'RR000123456'}, {'$set':{'common_name':'Paracetamol 500'}})

    # Delete one document
    # delete_data = collection_name.dataRaccoons.delete_one({'medicine_id':'RR000342522'})
    delete = MongoService().delete_one(db_name='EmreFikirlier', host='dataRaccoonsMongo', port='27017', username='root', password='root', collection='Market', target={'medicine_id':'RR000342522'})
    print(delete)
    return render(request, 'index.html')