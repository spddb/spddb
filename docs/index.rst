spddb 
========


Spddb is a simple python dictionary key-value based database, spddb allow you to log insert and remove operations


==================
Installation guide
==================


.. highlight:: sh


The recommended (and easiest) way to install spddb::

   $ git clone https://github.com/spddb/spddb
   $ cd spddb 
   $ python setup.py install 






==================
Commannds
==================


.. highlight:: sh


::

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


==================
Using Logging
================== 

Using spddb you can log insert and remove operations

.. highlight:: py

>>> from spddb import ziverdb
>>> db = ziverdb("test.db")
>>> db.logfile = "test.log"
>>> db.insert("hello", "world")
>>> db.delete("hello")

.. highlight:: sh

::

$ cat test.log
$ 2017-12-29 23:37:06,685 Added key hello with value world
$ 2017-12-29 23:37:06,686 Deleted key hello
