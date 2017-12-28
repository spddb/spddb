spddb 
========

==================
Installation guide
==================

.. highlight:: sh


The recommended (and easiest) way to install spddb::

   $ git clone https://github.com/spddb/spddb
   $ python setup.py install 






==================
Commannds
==================


.. highlight:: sh


The recommended (and easiest) way to install spddb::

   $ insert <key> <value> → Add specified key value 
   $ get <key> → Return the value of the specified key
   $ delete <key> → Delete specified key
   $ have <key> → Return True if the key exists False if not 
   $ getsize → Return the database size in bytes






==================
Usage guide
==================

.. highlight:: py

Look how easy it is to use:

    >>> from spddb import ziverdb
    >>> db = ziverdb("test.db")
    >>> db.insert("hello", "world")
    >>> db.have("hello")
    >>> True
    >>> db.get("hello")
    >>> "world"
    >>> db.getsize()
    >>> 18 
    >>>
    >>> db.delete("hello")
    >>> db.have("hello")
    >>> False 


