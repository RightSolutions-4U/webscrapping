from pymongo import MongoClient

# Create connection to MongoDB
client = MongoClient('mongodb+srv://mohtashim:Mohtashim098@cluster0.v5mw4.mongodb.net/?retryWrites=true&w=majority', 27017)
db = client['dbScrapper']
collection = db['coll_Scrapper']
print(collection)
# Build a basic dictionary
d = {'actor':'actor',	'demandado':'demandado',	'entidad':'entidad',	'expediente':'expediente',	'fecha':'fecha',	'fuero':'fuero',	'juzgado':'juzgado',	'tipo':'tipo',	'acuerdos':'acuerdos',	'monto':'monto',	'fecha_presentacion':'fecha_presentacion',	'actos_reclamados':'actos_reclamados',	'actos_reclamados_especificos':'actos_reclamados_especificos',	'Naturaleza_procedimiento':'Naturaleza_procedimiento',	'Prestación_demandada':'Prestación_demandada',	'Organo_jurisdiccional_origen':'Organo_jurisdiccional_origen',	'expediente_origen':'expediente_origen',	'materia':'materia',	'submateria':'submateria',	'fecha_sentencia':'fecha_sentencia',	'sentido_sentencia':'sentido_sentencia',	'resoluciones':'resoluciones',	'origen':'origen',	'fecha_insercion':'fecha_insercion',	'fecha_tecnica':'fecha_tecnica'}

# Insert the dictionary into Mongo
#db.collection.insert(d)
x = collection.insert_one(d)
print('End')