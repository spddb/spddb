#!/usr/bin/python
# Copyright (c) 2017 CVSC
# Distributed under the MIT/X11 software license, see the accompanying
# file license http://www.opensource.org/licenses/mit-license.php.

import logging 
import json
import os 


class ziverdb(dict):
    
    logfile = None 


    def __init__(self, path):
        self.path = os.path.expanduser(path)

        if os.path.isfile(path): self.self = eval(open(path).read())
        else: self.self = self


    def insert(self, key, value):
        """ Insert specified value to specified key """
        if not self.have(key):
            self[key] = value
            self.save()
            self.reload()
            if self.logfile:
                self.logg("Added key %s with value %s" %(key, value))
                
    
    def update(self, key, value):
        """ Update an existed key value """
        if self.have(key):
            self[key] = value 


    def delete(self, key):
        """ Delete specified key && value """
        if self.have(key):
            del self[key]
            self.save()
            if self.logfile:
                self.logg("Deleted key %s" %key)


    def have(self, key):
        """ Return True if the key already exists else return False """
        if key in self:
            return True
        return False


    def reload(self):
        """ Reload database """
        self.self = eval(open(self.path).read())


    def get(self, key):
        """ Return value of the specified key """
        if self.have(key):
            return self[key]
        return False


    def getkeys(self):
        """ Return a list with database keys """
        return self.keys()
    
    
    
    def lenkeys(self):
        """ Return a count of database key """
        return len(self)
    


    def getsize(self):
        """ Return database size in bytes """
        return os.stat(self.path).st_size

        
    def save(self):
        """ Save changes """
        json.dump(self, open(self.path, 'wt'))
        self.reload()


    def drop(self, db):
        """ Drop database """
        if os.path.isfile(db):
            os.remove(db)
    
    
    def logg(self, msg):
        logging.basicConfig(level=logging.INFO, 
                    filename=self.logfile,
                    format='%(asctime)s %(message)s')
        logging.info(msg)
