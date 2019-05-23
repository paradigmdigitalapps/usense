# coding=utf-8
import os
import webapp2
import jinja2
import json
from google.appengine.ext import ndb
from forms import ProfileForm
from google.appengine.api import users
from models import DataList, UserProfile, UserDestribution, TopListWord, User
from webapp2_extras.appengine.users import login_required


def configure_jinja2_environment():
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)


JINJA_ENVIRONMENT = configure_jinja2_environment()


class WebAppHandler(webapp2.RequestHandler):
    template_name = None
    login_required = False

    def dispatch(self):
        if self.login_required:
            if users.get_current_user():
                super(WebAppHandler, self).dispatch()
            else:
                self.abort(403)
        else:
            super(WebAppHandler, self).dispatch()

    def get_template_name(self):
        return self.template_name

    def get(self):
        template = JINJA_ENVIRONMENT.get_template(self.get_template_name())
        self.response.write(template.render(self.get_template_values()))

    def register_user(self):
        login_user_email = users.get_current_user().email()
        if not User.query().filter(User.email == login_user_email).get():
            user_obj = User(email=login_user_email)
            user_obj.put()

    def get_template_values(self):
        user = users.get_current_user()

        if user:
            login_button_url = users.create_logout_url('/')
            is_user_login = True
            login_button_text = 'Logout'
            self.register_user()
        else:
            is_user_login = False
            login_button_text = 'Register'
            login_button_url = users.create_login_url(self.request.uri)


        template_values = {
            'user': user,
            'login_button_url': login_button_url,
            'login_button_text': login_button_text,
            'is_user_login': is_user_login,
        }

        return template_values


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
    template_name = 'about.html'


class Report1View(WebAppHandler):
    template_name = 'report1.html'
    login_required = True

    def get_template_values(self):
        template_values = super(Report1View, self).get_template_values()
        report_data = TopListWord.query()
        template_values['report_data'] = report_data
        return template_values


class Report2View(WebAppHandler):
    template_name = 'report2.html'
    login_required = True

    def get_template_values(self):
        template_values = super(Report2View, self).get_template_values()
        report_data = UserDestribution.query()
        template_values['report_data'] = report_data
        return template_values


class UserProfileView(WebAppHandler):
    template_name = 'myprofile.html'
    login_required = True

    def get_template_values(self):
        template_values = super(UserProfileView, self).get_template_values()
        form = ProfileForm()
        template_values['form'] = form
        return template_values

    def save_profile(self):
        user_obj_key = ndb.Key(User, users.get_current_user().email())
        user_profile_obj = UserProfile(
            user=user_obj_key,
            leadership_role=self.request.get('country'),
            story=self.request.get('story'),
            keyword=self.request.get('keyword'),
            comment=self.request.get('comment'),
        )
        user_profile_obj.put()
        
    def post(self):
        form = ProfileForm(self.request.POST)
        success_message = ''
        if form.validate():
            self.save_profile()
            form = ProfileForm()
            success_message = 'Your request submited successfully'

        template = JINJA_ENVIRONMENT.get_template(self.get_template_name())
        template_value = self.get_template_values()
        template_value['success_message'] = success_message
        self.response.write(template.render(template_value))


app = webapp2.WSGIApplication(
    [
        ('/', About),
        ('/digitalization', DigitalizationView),
        ('/information', InformationView),
        ('/motivation', MotivationView),
        ('/report1', Report1View),
        ('/report2', Report2View),
        ('/MyProfile', UserProfileView),
    ],
    debug=True)
