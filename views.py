# coding=utf-8
import os
import webapp2
import jinja2
import json

from data_list import digitalization, information, motivation
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
        template_values['digitalization_list'] = digitalization
        return template_values


class InformationView(WebAppHandler):
    template_name = 'information.html'

    def get_template_values(self):
        template_values = super(InformationView, self).get_template_values()
        template_values['information_list'] = information
        return template_values


class MotivationView(WebAppHandler):
    template_name = 'motivation.html'

    def get_template_values(self):
        template_values = super(MotivationView, self).get_template_values()
        template_values['motivation_list'] = motivation
        return template_values




app = webapp2.WSGIApplication(
    [
        ('/', DigitalizationView),
        ('/information', InformationView),
        ('/motivation', MotivationView),
    ],
    debug=True)
