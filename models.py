from google.appengine.ext import ndb


class User(ndb.Model):
    email = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now=True)


class DataList(ndb.Model):
    type_name = ndb.StringProperty()
    description = ndb.TextProperty()
    link = ndb.TextProperty()


class UserProfile(ndb.Model):
    leadership_role = ndb.StringProperty()
    story = ndb.StringProperty()
    keyword = ndb.StringProperty()
    comment = ndb.StringProperty()
    user = ndb.KeyProperty(kind=User)

class TopListWord(ndb.Model):
    location = ndb.StringProperty()
    parent = ndb.StringProperty()
    size = ndb.StringProperty()
    color = ndb.StringProperty()

class UserDestribution(ndb.Model):
    task = ndb.StringProperty()
    hour = ndb.StringProperty()