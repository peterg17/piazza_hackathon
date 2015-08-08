
import urllib2
import json

from datetime import date

def retrieve_user_profile_data():
	req = urllib2.Request('Home')
	response = urllib2.urlopen(req)
	error_data = json.load(response)

	return error_data

def generate_timestamp(error_data):
	"""
	Takes in a list of error record in dict-like objects.

	Returns a dict with key: date object and num of errors
	"""

	dates_n_errors = {}
	for record in error_records:
		for time in record:
			date = parse_time_string(time)
			dates_n_errors[date] = dates_n_errors[date].get(date, 0)+1

	return dates_n_errors

def parse_time_string(str):
	"""	Takes in a timestamps. 
		Returns a python date object."""
	
	elements = str.split() #[date, time]
	date= elements[0]
	time = elements[1]

	year, month, day = map(int, date.split("-"))
	hour, minute, second = map(int, time.split(":"))

	return date(year, month, day)

user_data = retrieve_user_profile_data()
times = generate_timestamp(user_data)

#user_data is a list of python date objects


