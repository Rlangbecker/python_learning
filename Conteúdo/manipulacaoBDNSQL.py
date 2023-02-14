import pymongo
from pymongo import MongoClient

def manipulacaoDadosMongoDB():
    cliente = pymongo.MongoClient("mongodb://localhost:27017")
    db = cliente.db_python

    for i in range(1,10):
        objDic = {'codigo' : i}
        db.db_python.insert_one(objDic)

    db.db_python.update_one({'codigo' : 2},{"$set" : {'codigoAdicional': 123}})
    db.db_python.delete_one({'codigo' : 1})

    resultadoConsulta = db.db_python.find({})
    for doc in resultadoConsulta:
        print(doc)

manipulacaoDadosMongoDB()


