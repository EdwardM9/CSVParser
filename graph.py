"""
Data Visualization

Takes in parsed data from a CSV file and renders it onto a chart.

Copyright(c) 2014 Edward Moreno
Distributed under the Creative Commons Attribution 3.0 Unported license.
"""

from collections import Counter

import matplotlib.pyplot as plt
import numpy.numarray as na

import parse as p

def visualize_days(file_path):
	#Parse data
	self.data_file, self.headers = p.parse(file_path, ",")

	#Make a counter from each day of the week
	counter = Counter(item["DayOfWeek"] for item in self.data_file)
	#seperate counter for ordering
	data_list = [
				counter["Sunday"],
				counter["Monday"],
				counter["Tuesday"],
				counter["Wednesday"],
				counter["Thursday"],
				counter["Friday"],
				counter["Saturday"]]
	day_tuple = tuple(["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"])

	# Assign the data to a plot
	plt.plot(self.data_list)
	plt.xticks(range(len(day_tuple)), day_tuple)
	plt.savefig("Days.png")
	plt.clf()
	return self.headers
