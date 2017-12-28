from spddb import * 



db = ziverdb("hello.db")




db.insert("hello", "world")

print db.have("hello") == True 
print db.get("hello") == "world"
print db.getsize() == 18 

db.delete("hello")

print db.have("hello") == False 
print db.get("hello")  == False 
print db.getsize()  == 2

os.remove("hello.db")

