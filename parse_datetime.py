
import urllib2
import json
import datetime

def parse_time_string(str):
	"""	Takes in a timestamp string. 
		Returns a python date object."""
	
	elements = str.split() #[date, time]
	date= elements[0]
	time = elements[1]

	year, month, day = map(int, date.split("-"))
	hour, minute, second = map(int, time.split(":"))

	return datetime.date(year, month, day)

def retrieve_error_data():
	req = urllib2.Request('Home')
	response = urllib2.urlopen(req)
	error_data = json.load(response)

	return error_data

def generate_date_n_error(error_data):
	"""
	Takes in a list of error record in dict-like objects.

	Returns a dict: {date object: num of errors}
	"""

	dates_n_errors = {}
	for record in error_data:
		for time in record:
			date = parse_time_string(time)
			dates_n_errors[date] = dates_n_errors.get(date, 0)+1

	return dates_n_errors

def analyze_specific_errors(error_data):
	
	error_types = {"Type Error":{},
					"Index Error":{},
					"Syntax Error":{},
					"IO Error":{},
					"Key Error":{},
					"Attribute Error":{},
					"Indentation Error":{},
					"Name Error":{}
					}

	for record in error_data:
		for time, error in record.items():
			key = parse_time_string(time)
			error_types[error][key] = error_types[error].get(key, 0)+1

	return error_types 


if __name__ == "__main__":
	error_data = retrieve_error_data()
	#Retrieves error data
	print error_data

	date_n_error = generate_date_n_error(error_data)
	#Generates a dictionary {date: aggregate count of num}
	print date_n_error

	specific_errors =  analyze_specific_errors(error_data)
	#Generates a dictionary { "Type Error": {date1: 3, date2: 2}, "Syntax Error": {date1:1}}
	print specific_errors

