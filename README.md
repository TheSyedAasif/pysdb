# pysdb
pysdb is a lightweight , portable, embeddable database management library


### Import first:

```
import pysdb
```

## concepts

SDB_STORE
--------
SDB_STORE is a group of Databases

it's the directory where all the Databases exists.

SDB_STORE can be created by the following command:
```
$ mkdir /path/to/SDB_STORE/ && touch /path/to/SDB_STORE/sdbstore
```
if you prefer a different directory name change DB_STORE to whatever name you like , for example:
```
$ mkdir /path/to/MY_STORE/ && touch /path/to/MY_STORE/sdbstore

```
DATABASE
--------
group of Collections is a Database

COLLECTIONS
-----------

a bundle of Records is a collection (it's kinda like a Table)

Records
-------

Records are like a row in a table

Record is pure python Dictionary

example:

```
student_record1  = {
  "name": "student1_name1",
  "age":19
 }
 ```


## example

```
import pysdb

store = sdb.UseStore('/path/to/DB_STORE/') # use the created store (returns a pointer to store)

store.CreateDB('db') # creates a db in store (returns true or false)

db = store.OpenDB('db') # opens a db in store (return a pointer to db)

store.CloseDB('db') # closes an opened db

store.DropDB('db') # deletes the entire database (return true or false)

store.LookForDB('db') # checks if a Database exists (returns true or false)

db.CreateCl('cl')  # creates a collection in db (returns true or false)

cl = db.OpenCl('cl') # opens a collection in db (returns a pointer to the collection)

db.CloseCl('cl') # closes the collection

db.DropCl('cl') # deletes a collection in db (returns true or false)

db.LookForCl('cl') # checks if a collection exists (returns true or false)

# create a record (pure python dictionary)
student_record1  = {
  "name": "student_name1",
  "age":19
 }
 
 
student_record2  = {
  "name": "student_name2",
  "age":20
 }
 
 
 cl.AddRec('student_record_1', student_record1) # adds a record to cl

 cl.UpdateRect('student_record_1', student_record2) # updates the record in cl
 
 cl.ReadRec('student_record_1') # returns a Record ( python dictionary - same as above student_record1 )
 
 cl.RemoveRect('student_record_1') # removes a Record in cl


