# coding=utf-8
import os
import webapp2
import jinja2
import json
from models import DataList
from google.appengine.api import users


def configure_jinja2_environment():
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)


JINJA_ENVIRONMENT = configure_jinja2_environment()


class WebAppHandler(webapp2.RequestHandler):
    template_name = None

    def get(self):
        template = JINJA_ENVIRONMENT.get_template(self.get_template_name())
        self.response.write(template.render(self.get_template_values()))

    def get_template_values(self):

        is_user_login = False
        login_button_text = 'Register'
        user = users.get_current_user()

        if user:
            login_button_url = users.create_logout_url('/')
            is_user_login = True
            login_button_text = 'Logout'
        else:
            login_button_url = users.create_login_url(self.request.uri)

        group_assigned = 0
        group_name = 'notingroup'

        template_values = {

            'user': user,
            'login_button_url': login_button_url,
            'group_assigned': group_assigned,
            'group_name': group_name,
            'login_button_text': login_button_text,
            'is_user_login': is_user_login,
        }
        return template_values

    def get_template_name(self):
        return self.template_name


class DigitalizationView(WebAppHandler):
    template_name = 'digitalization.html'

    def get_template_values(self):
        template_values = super(DigitalizationView, self).get_template_values()
        digitalization = DataList.query().filter(DataList.type_name == 'digitalization')
        template_values['digitalization_list'] = digitalization
        return template_values


class InformationView(WebAppHandler):
    template_name = 'information.html'

    def get_template_values(self):
        template_values = super(InformationView, self).get_template_values()
        information = DataList.query().filter(DataList.type_name == 'information')
        template_values['information_list'] = information
        return template_values


class MotivationView(WebAppHandler):
    template_name = 'motivation.html'

    def get_template_values(self):
        template_values = super(MotivationView, self).get_template_values()
        motivation = DataList.query().filter(DataList.type_name == 'motivation')
        template_values['motivation_list'] = motivation
        return template_values

class About(WebAppHandler):
    template_name='about.html'


class Report1View(WebAppHandler):
    template_name ='report1.html'


class Report2View(WebAppHandler):
    template_name = 'report2.html'


class MyProfileView(WebAppHandler):
    template_name ='myprofile.html'

    def post(self):
        data = json.loads(self.request.body)
        story_tag = data["story_tag"]
        keyword_tag = data["keyword_tag"]
        comment_tag = data["comment_tag"]

        if story_tag == "" or keyword_tag == "" or comment_tag == "":

            message = "Please Fill all the fields"
        else:

            message = "Congratulations data successful created"

        self.response.write(json.dumps({"message": message}))


app = webapp2.WSGIApplication(
    [
        ('/', DigitalizationView),
        ('/information', InformationView),
        ('/motivation', MotivationView),
        ('/about', About),
        ('/report1', Report1View),
        ('/report2', Report2View),
        ('/MyProfile', MyProfileView),
    ],
    debug=True)
