from google.cloud import ndb

class Contact(ndb.Model):
    identification = ndb.StringProperty()
    name = ndb.StringProperty()
    gender = ndb.StringProperty()
    age = ndb.StringProperty()
    company = ndb.StringProperty()
    currentdate = ndb.StringProperty()
    test1 = ndb.StringProperty()
    test2 = ndb.StringProperty()
    test3 = ndb.StringProperty()
    test4 = ndb.StringProperty()
    time = ndb.StringProperty()