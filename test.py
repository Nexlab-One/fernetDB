from src import fernetdb
db = securedb.Db("db", '.key', force=True)


print(db.write_many({"test": "test", "test2": "test2"}))



#db.delete("lol")


#print(db.get("lol"))
