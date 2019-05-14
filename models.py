from google.appengine.ext import ndb


class DataList(ndb.Model):
    type_name = ndb.StringProperty()
    description = ndb.TextProperty()
    link = ndb.TextProperty()


class UserProfile(ndb.Model):
    leadership_role = ndb.StringProperty()
    story = ndb.StringProperty()
    keyword = ndb.StringProperty()
    comment = ndb.StringProperty()
