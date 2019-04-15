import webapp2
import jinja2
import os
import json
import re
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MWAGroup(ndb.Model):
    """A main model for representing an individual Guestbook entry."""
    user = ndb.StringProperty()
    group = ndb.StringProperty(default='notingroup')

class MWAOpinionHistory(ndb.Model):
    """A main model for representing an individual Guestbook entry."""
    username = ndb.StringProperty()
    group = ndb.StringProperty(default='notingroup')
    storytag = ndb.StringProperty()
    keywordtag = ndb.StringProperty()
    opinion = ndb.StringProperty()
    option = ndb.StringProperty()
    score = ndb.IntegerProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
# [STATRT main page servie that includes handling POST requests]

    def get(self):

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Basic'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Register'

        groupassigned = 0
        groupname = 'notingroup'

        if url_linktext == 'LOGOUT':

            qgroup = MWAGroup.query(MWAGroup.user == user.email())
            usergroup = qgroup.fetch(1)
            if qgroup.count(1):
            	groupname = usergroup[0].group
                if groupname == 'notingroup':
                    groupassigned = 0
                else:
                    groupassigned = 1

        template_values = {
            'user': user,
            'url': url,
            'groupassigned' : groupassigned,
            'groupname' : groupname,
            'url_linktext': url_linktext,
        }


        template = JINJA_ENVIRONMENT.get_template('usense_newdesign.html')
        self.response.write(template.render(template_values))


class Groupname(webapp2.RequestHandler):
# [STATRT main page servie that includes handling POST requests]
    def get(self):


        self.response.write("hello")


    def post(self):


        data = json.loads(self.request.body)
        user = users.get_current_user().email()
        groupname = data
        # storyvalue = data["storyvalue"]


        useringroup = MWAGroup(id=user)
        useringroup.group = groupname
        useringroup.user = user


        useringroup.put()


        mwa = MWAOpinionHistory(username=user, option=groupname)
        mwa.put()


        self.response.write(json.dumps({"message": "Sikeres adatbevitel"}))

 # [END main page



app = webapp2.WSGIApplication(
    [('/', MainPage),
    ('/groupname', Groupname),

    ],
    debug=True)
