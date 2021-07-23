from scarletdb import ScarletDB

db = ScarletDB([])
db.replit("data") # data is replit db the key that the database is stored in

db.clear()

db.insert_many([
  {
    "name": "AJ",
    "pet": "Rabbit"
  },
  {
    "name": "Jack",
    "pet": "Dog"
  }
])

db.update({"name": "Jack"}, {"name": "Tom"})

print(db.get({
  "pet": "Dog"
}))