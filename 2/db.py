from pymongo import MongoClient

URL = ""
CONNECT = 'localhost', 27017

class MongoConnect():

    def save(self, json):
        try:
            prova = MongoClient(URL)
            banco = prova.music  # nome do banco
            id = banco.insert_one(json).inserted_id
        except Exception as e:
            print("Problema ao salvar registro")
            print(json)
            print(e)
