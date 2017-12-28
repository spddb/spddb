# spddb


Example Insert || Insert specified value to specified key

    >>> from spddb import ziverdb
    >>> db = ziverdb("hello.db")
    >>> db.insert("hello", "world")
    
    # insert with logging 
    
    >>> db.logfile = "hello.log"
    >>> db.insert("hello", "world")
    # cat hello.log Added key hello with value world

    
    

Example Get || Return the value of the specified key

    >>> db.get("hello")
    >>> 'world'

Example Have || Return True if the key already exists else return False

    >>> db.have("hello")
    >>> 'True'

Example getsize || Return the hello.db database size in bytes

    >>> db.getsize()
    >>> 18 


Example Delete || Delete specified key && value

    >>> db.delete("hello")

Example Drop || Drop specified database file

    >>> db.drop("hello.db")
    
