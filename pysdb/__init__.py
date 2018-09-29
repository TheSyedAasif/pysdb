name = "pysdb"
import sys
import os
import shutil
import json


class Cln:

	__clnPath = ''
	__recs = {}

	def __init__(self, clnPath):
		self.__clnPath = clnPath
		with open(self.__clnPath) as f:
			self.__recs = json.load(f)
	

	def getName(self):
		return os.path.basename(self.__clnPath)
	
	def getPath(self):
		return self.__clnPath

	def AddRec(self, recName, rec):
		self.__recs[recName] = rec
	
	def ReadRec(self, recName):
		return self.__recs[recName]
	
	def RemoveRec(self, recName):
		del self.__recs[recName]

	def UpdateRec(self, recName, rec):
		self.__recs[recName] = rec

	def LookForRec(self, recName):
		return recName in self.__recs.keys()

	def Persist(self):
		with open(self.__clnPath, 'w') as f:
			json.dump(self.__recs, f)

	def CountRec(self):
		return len(self.__recs)

	


class Sdb:

	__sdbPath = ''


	def __init__(self, sdbPath):
		self.__sdbPath = sdbPath


	def getName(self):
		return os.path.basename(os.path.normpath(self.__sdbPath)) # gets path from this/is/a/path


	def CloseCl(self, clName):
		del clName


	def LookForCl(self, clName):
		if os.path.exists(self.__sdbPath + clName):
			return True
		else:
			return False
		

	def DropCl(self, clName):
		os.remove(self.__sdbPath + clName)

	def CreateCl(self, clName):
		#open(self.__sdbPath + clName, 'a').close()
		f = open(self.__sdbPath + clName, 'wb')
		f.write(bytes("{}", 'uTF-8'))
		del f
		return self.LookForCl(clName)

	def OpenCl(self, clName):
		if self.LookForCl(clName):
			return Cln(self.__sdbPath + clName)
		else:
			sys.exit('The Cl can\'t be opened. It may not exist!')




class SdbStore:
	
	__storePath = ''


	def LookForDB(self, dbName):	
		if os.path.isdir(self.__storePath + dbName) and  os.path.exists(self.__storePath + dbName + '/' + 'sdb'):
			return True
		else:
			return False
	

	def OpenDB(self, dbName):
		if self.LookForDB(dbName):
			return Sdb(self.__storePath + dbName + '/')
		else:
			sys.exit('The DB can\'t be opened. It may not exist!')
	

	def CreateDB(self, dbName):
		if self.LookForDB(dbName):
			sys.exit('The DB already exists')
		else:
			os.mkdir(self.__storePath + dbName)
			open(self.__storePath + dbName + '/sdb', 'a').close()
			return self.LookForDB(dbName)



	def CloseDB(self, dbName):
		del dbName
		

	def DropDB(self, dbName):
		shutil.rmtree(self.__storePath + dbName) 		
	

	def __init__(self, storePath):
		self.__storePath = storePath


def UseStore(storePath):
	#check if storePath dir exists
	if os.path.isdir(storePath):

		# check if dbstore exists in storePath and its not a file
		if os.path.exists(storePath + 'sdbstore'):
			# return SdbStore object
			return SdbStore(storePath)
		else:
			sys.exit("The provided directory for UseStore() is not configured as sdb_store!")
	else:
		sys.exit("The provided directory for UseStore() does not exist!")





"""
def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


 basedir = os.path.dirname(path)

os.path.exists(path)

os.path.isdir(path)

shutil.rmtree(path)


with open('states.json') as f:
	data = json.load(f)


with open('__new__sates.json', 'w') as f:
	json.dump(data, f)

import urllib.request import urlopen

with urlopen(path) as response:

	source  = response.read()


	json.dumps()
	json.loads()

 """

 """
	def getPath(self): ( was in Sdb)
		return self.__sdbPath
"""	

"""	def getName(self): ( was in SdbStore)
		return os.path.basename(os.path.normpath(self.__storePath)) # gets path from this/is/a/path
"""
