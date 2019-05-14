# appengine_config.py
from google.appengine.ext import vendor

# Add any libraries install in the "lib" folder.
vendor.add('lib')



# autofill initial data

from google.appengine.ext import ndb
from models import DataList
from data_list import *

# delete old data
keys = DataList.query().fetch(keys_only=True)
ndb.delete_multi(keys)


for r in digitalization:
    data_list = DataList(type_name='digitalization', description= r['description'], link=r['link'])
    data_list.put()

for r in information:
    data_list = DataList(type_name='information', description= r['description'], link=r['link'])
    data_list.put()

for r in motivation:
    data_list = DataList(type_name='motivation', description= r['description'], link=r['link'])
    data_list.put()
