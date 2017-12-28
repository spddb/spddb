#!/usr/bin/python
# Copyright (c) 2017 CVSC
# Distributed under the MIT/X11 software license, see the accompanying
# file license.blockt or http://www.opensource.org/licenses/mit-license.php.


import json
import os 


class ziverdb(dict):


    def __init__(self, path):
        self.path = os.path.expanduser(path)

        if os.path.isfile(path): self.self = eval(open(path).read())
        else: self.self = self


    def insert(self, key, value):
        """ Insert specified value to specified key """
        self[key] = value
        self.save()
        self.reload()


    def delete(self, key):
        """ Delete specified key && value """
        del self[key]
        self.save()


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


    def getsize(self):
        """ Return database size in bytes """
        return os.stat(self.path).st_size

        
    def save(self):
        """ Save changes """
        json.dump(self, open(self.path, 'wt'))
        self.reload()