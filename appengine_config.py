# coding=utf-8
# appengine_config.py
from google.appengine.ext import vendor

# Add any libraries install in the "lib" folder.
vendor.add('lib')

# autofill initial data

import csv
import time
import os
from google.appengine.ext import ndb
from models import DataList, UserDestribution, TopListWord


######################  Being DataList  ######################
# delete old data
keys = DataList.query().fetch(keys_only=True)
ndb.delete_multi(keys)
time.sleep(5)

try:
	with open('csv/data_list.csv') as csvfile:
		csvread = csv.reader(csvfile, delimiter=',')
		for row in csvread:
			data_list = DataList(type_name=row[0], description= row[1].decode('iso-8859-1') , link=row[2])
			data_list.put()
except AssertionError as error:
	print"error"

###################### End DataList  ########################


##################### Being Report1 #######################
# delete old data
keys = TopListWord.query().fetch(keys_only=True)
ndb.delete_multi(keys)

with open('csv/report1.csv') as csvfile:
	csvread = csv.reader(csvfile, delimiter=',')
	for row in csvread:
		data_list = TopListWord(location=row[0], parent= row[1], size=row[2], color=row[3])
		data_list.put()

###################### End Report1  ##########################


###################### Being Report2  ######################
# delete old data
keys = UserDestribution.query().fetch(keys_only=True)
ndb.delete_multi(keys)


with open('csv/report2.csv') as csvfile:
	csvread = csv.reader(csvfile, delimiter=',')
	for row in csvread:
		data_list = UserDestribution(task=row[0], hour= row[1])
		data_list.put()

######################### End Report2 ##########################