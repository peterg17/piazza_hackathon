import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date
import numpy as np


#Creates and saves a pie_chart


def create_pie_chart(pie_chart_data):
	count_list = []
	label_list = []
	for label, count in pie_data.items():
		label_list.append(label)
		count_list.append(count)

	plt.axis("equal")
	plt.pie(
	        count_list,
	        labels=label_list,
	        autopct="%1.1f%%"
	        )
	plt.title("Error Distribution")
	plt.savefig('pie.png')#saves it at the current directory
	plt.show()

#Creates and saves line_graph


def create_scatter_chart(date_n_error):
	date_list = []
	count_list = []
	for date, count in date_n_error.items():
		date_list.append(date)
		count_list.append(count)

	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
	plt.plot_date(date_list,count_list)
	plt.gcf().autofmt_xdate()

	plt.ylabel('Total num of errors')
	plt.xlabel('Dates')

	plt.title("Progress Over Time")
	plt.savefig('scatter.png')#saves it at the current directory
	plt.show()
	#determines the range of the x-axis and y-axis




sample_data = [{"2015-08-03 07:25:45":"Type Error"},
				{"2015-08-03 08:28:20":"Indentation Error"},
				{"2015-08-04 09:37:28":"Syntax Error"},
				{"2015-08-06 07:31:42":"Syntax Error"},
				{"2015-08-07 11:20:47":"Syntax Error"},
				{"2015-08-08 10:30:28":"Syntax Error"},
				{"2015-08-08 10:31:08":"Type Error"},
				{"2015-08-08 10:35:45":"Syntax Error"},
				{"2015-08-08 10:36:44":"Attribute Error"},
				{"2015-08-08 10:38:27":"Name Error"},
				{"2015-08-08 10:39:24":"Syntax Error"},
				{"2015-08-08 10:41:43":"Syntax Error"},
				{"2015-08-08 11:13:48":"Name Error"},
				{"2015-08-09 09:32:23":"Name Error"}]


aggregate_data = {date(2015, 8, 3):2,
					date(2015, 8, 4):1,
					date(2015, 8, 6):1,
					date(2015, 8, 7):1,
					date(2015, 8, 8):8, 
					date(2015, 8, 9):1}

if __name__ == "__main__":
	pie_data = {"Type Error": 2, "Indentation Error": 1, "Syntax Error": 7,
						"Attribute Error": 1, "Name Error": 3, }
	create_pie_chart(pie_data)

	date_n_error = {date(2015, 8, 5):10, date(2015, 8, 6):7, date(2015, 8, 7):5, date(2015, 8, 8):2}

	create_scatter_chart(date_n_error)





