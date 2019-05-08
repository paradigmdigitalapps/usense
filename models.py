from google.appengine.ext import ndb

class DataList(ndb.Model):
    type_name = ndb.StringProperty()
    description = ndb.TextProperty()
    link = ndb.TextProperty()
    

