from spddb import * 



db = ziverdb("hello.db")

db.insert("hello", "world")



print db.have("hello") == True 
print db.get("hello") == "world"
print db.getsize() == 18 
print db.getkeys() == ['hello']


db.delete("hello")

print db.have("hello") == False 
print db.get("hello")  == False 
print db.getsize()  == 2


os.remove("hello.db")

db = ziverdb("hello.db")




db.insert("hello", "world")


db.drop("hello.db")


try:
	size = db.getsize()
except Exception, e:
	print True 
else:
	print False
